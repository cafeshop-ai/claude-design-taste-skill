// Render one output and run automated checks.
//   node audit.mjs <run-dir>     (expects <run-dir>/output/index.html)
// Writes <run-dir>/audit.json and <run-dir>/shots/{desktop-light,desktop-dark,mobile-light}.jpg
//
// The checks are proxies for what the skill teaches, not a measure of taste:
// accessibility (axe-core, WCAG 2.2 AA tags), mobile overflow, dark-mode
// support, visible keyboard focus, reduced-motion handling, common generic
// tells, and how many distinct sizes/colors/radii the page uses.
import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const axeSource = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
const runDir = path.resolve(process.argv[2]);
const url = "file://" + path.join(runDir, "output", "index.html");
const shots = path.join(runDir, "shots");
fs.mkdirSync(shots, { recursive: true });

const browser = await chromium.launch({ args: ["--no-sandbox"] });

async function open(width, scheme) {
  const page = await browser.newPage({ viewport: { width, height: 900 }, colorScheme: scheme });
  const errors = [];
  page.on("pageerror", e => errors.push(e.message));
  page.on("console", m => { if (m.type() === "error") errors.push(m.text()); });
  await page.goto(url, { waitUntil: "networkidle", timeout: 45000 }).catch(e => errors.push("load: " + e.message));
  // Scroll through once so scroll-triggered reveals fire, then settle at the top.
  await page.evaluate(async () => {
    for (let y = 0; y < document.documentElement.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
    scrollTo(0, 0);
  });
  await page.waitForTimeout(900);
  return { page, errors };
}

async function axe(page) {
  await page.addScriptTag({ content: axeSource });
  const res = await page.evaluate(() => axe.run(document, {
    runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] }, preload: false,
  }));
  return res.violations.map(v => ({ id: v.id, impact: v.impact, nodes: v.nodes.length }));
}

// Mean luminance of the viewport, measured from a real screenshot.
async function meanLuminance(page) {
  const b64 = (await page.screenshot({ type: "jpeg", quality: 60 })).toString("base64");
  return page.evaluate(async src => {
    const img = new Image(); img.src = src; await img.decode();
    const c = document.createElement("canvas"); c.width = 144; c.height = 90;
    const ctx = c.getContext("2d"); ctx.drawImage(img, 0, 0, 144, 90);
    const d = ctx.getImageData(0, 0, 144, 90).data; let sum = 0;
    for (let i = 0; i < d.length; i += 4) sum += (0.2126 * d[i] + 0.7152 * d[i + 1] + 0.0722 * d[i + 2]) / 255;
    return +(sum / (d.length / 4)).toFixed(3);
  }, "data:image/jpeg;base64," + b64);
}

async function focusCheck(page) {
  const stops = [];
  for (let i = 0; i < 10; i++) {
    await page.keyboard.press("Tab");
    const r = await page.evaluate(() => {
      const el = document.activeElement;
      if (!el || el === document.body) return null;
      const read = () => { const s = getComputedStyle(el); return [s.outlineStyle, s.outlineWidth, s.boxShadow, s.borderColor, s.backgroundColor, s.textDecorationLine].join("|"); };
      const s = getComputedStyle(el);
      const outline = s.outlineStyle !== "none" && parseFloat(s.outlineWidth) > 0;
      const focused = read(); el.blur(); const blurred = read(); el.focus();
      return { tag: el.tagName.toLowerCase(), visible: outline || focused !== blurred };
    });
    if (r) stops.push(r);
  }
  return { stops: stops.length, visible: stops.filter(s => s.visible).length };
}

const pageFacts = () => {
  const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none" && +s.opacity > 0; };
  const all = [...document.body.querySelectorAll("*")].filter(vis);
  const textEls = all.filter(el => [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim()));
  const text = document.body.innerText;

  // Computed colors -> OKLCH (for hue/chroma of the colors in use). Chromium
  // reports colors in the space they were authored in: rgb(), oklch(), oklab(), color(srgb …).
  const lin = v => v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
  const fromSrgb = (r, g, b) => {
    const [R, G, B] = [lin(r), lin(g), lin(b)];
    const l = Math.cbrt(0.4122214708 * R + 0.5363325363 * G + 0.0514459929 * B);
    const m = Math.cbrt(0.2119034982 * R + 0.6806995451 * G + 0.1073969566 * B);
    const s = Math.cbrt(0.0883024619 * R + 0.2817188376 * G + 0.6299787005 * B);
    const A = 1.9779984951 * l - 2.428592205 * m + 0.4505937099 * s;
    const Bb = 0.0259040371 * l + 0.7827717662 * m - 0.808675766 * s;
    return { C: Math.hypot(A, Bb), H: (Math.atan2(Bb, A) * 180 / Math.PI + 360) % 360 };
  };
  const oklch = str => {
    const m = str.match(/^(rgba?|oklch|oklab|color)\(([^)]*)\)/); if (!m) return null;
    let parts = m[2].replace("srgb", "").split("/");
    const alpha = parts[1] === undefined ? 1 : parseFloat(parts[1]) / (parts[1].includes("%") ? 100 : 1);
    if (alpha < 0.5) return null;
    const v = parts[0].split(/[ ,]+/).filter(Boolean).map(x => x === "none" ? 0 : parseFloat(x));
    if (m[1].startsWith("rgb")) { if (m[2].split(/[ ,/]+/).filter(Boolean).length === 4 && parseFloat(m[2].split(/[ ,/]+/).filter(Boolean)[3]) < 0.5) return null; return fromSrgb(v[0] / 255, v[1] / 255, v[2] / 255); }
    if (m[1] === "color") return fromSrgb(v[0], v[1], v[2]);
    if (m[1] === "oklch") return { C: v[1], H: v[2] };
    return { C: Math.hypot(v[1], v[2]), H: (Math.atan2(v[2], v[1]) * 180 / Math.PI + 360) % 360 }; // oklab
  };
  const chromatic = new Map(); // 30-degree hue bucket -> weight (element count)
  for (const el of all) {
    const s = getComputedStyle(el);
    for (const c of [s.backgroundColor, ...(textEls.includes(el) ? [s.color] : [])]) {
      const o = oklch(c); if (o && o.C > 0.06) { const k = Math.round(o.H / 30) * 30 % 360; const b = chromatic.get(k) || { n: 0, h: 0 }; b.n++; b.h += o.H; chromatic.set(k, b); }
    }
  }
  // Dominant hue = mean hue of the most-used 30-degree bucket (not the bucket's center,
  // which would file a 264-degree blue under 270).
  const hues = [...chromatic.entries()].sort((a, b) => b[1].n - a[1].n);
  const dominant = hues[0] ? Math.round(hues[0][1].h / hues[0][1].n) : null;

  const gradientText = all.filter(el => { const s = getComputedStyle(el); return (s.webkitBackgroundClip === "text" || s.backgroundClip === "text") && s.backgroundImage.includes("gradient"); }).length;
  const emoji = (text.match(/\p{Extended_Pictographic}/gu) || []).length;
  const buzz = (text.toLowerCase().match(/\b(unlock|supercharge|seamless(ly)?|revolutioni[sz]e|elevate|empower|effortless(ly)?|cutting-edge|next-level|game-chang\w*|all-in-one|blazing)\b/g) || []);
  const paras = [...document.querySelectorAll("p")].filter(vis).filter(p => p.innerText.trim().length >= 40);
  const centered = paras.filter(p => getComputedStyle(p).textAlign === "center").length;
  const small = new Set(["a", "an", "the", "and", "or", "for", "to", "of", "in", "on", "with", "per", "vs", "at", "by"]);
  const labels = [...document.querySelectorAll("h1,h2,h3,h4,button,a")].filter(vis).map(e => e.innerText.trim()).filter(t => t.split(/\s+/).length >= 3 && t.length < 80);
  const titleCase = labels.filter(t => t.split(/\s+/).filter(w => /^[a-z]/i.test(w) && !small.has(w.toLowerCase())).every(w => /^[A-Z]/.test(w))).length;

  const fontSizes = new Set(textEls.map(el => Math.round(parseFloat(getComputedStyle(el).fontSize))));
  const families = new Set(textEls.map(el => getComputedStyle(el).fontFamily.split(",")[0].replace(/["']/g, "").trim()));
  const radii = new Set(all.map(el => getComputedStyle(el).borderTopLeftRadius).filter(r => r !== "0px"));
  const shadows = all.filter(el => getComputedStyle(el).boxShadow !== "none").length;

  const numeric = textEls.filter(el => /^[\s$€£¥+\-−]*[\d.,]{3,}\s*%?$/.test([...el.childNodes].filter(n => n.nodeType === 3).map(n => n.textContent).join("").trim()));
  const tabular = numeric.filter(el => getComputedStyle(el).fontVariantNumeric.includes("tabular")).length;

  const fields = [...document.querySelectorAll("input:not([type=hidden]):not([type=submit]):not([type=button]):not([type=radio]):not([type=checkbox]), select, textarea")];
  const unlabeled = fields.filter(f => !(f.labels && f.labels.length) && !f.getAttribute("aria-label") && !f.getAttribute("aria-labelledby"));

  // Content: how much is there, and does it assert things nobody supplied?
  const claims = text.match(/\b\d[\d,.]*\s?[kKmM]?\+(?=\s|$|\W)|\b\d(?:\.\d)?\s?\/\s?5\b|[★⭐]|\b(trusted|loved|used) by\b|\bjoin (over )?\d|\b\d+%\s(of|faster|more|less|fewer|increase|reduction)\b/gi) || [];
  const testimonials = document.querySelectorAll("blockquote, [class*=testimonial i], [id*=testimonial i]").length;
  const content = {
    words: text.split(/\s+/).filter(Boolean).length,
    headings: [...document.querySelectorAll("h1,h2,h3")].filter(vis).length,
    sections: [...document.querySelectorAll("section, main > div, body > div > section")].filter(vis).length,
    claims, testimonials,
  };

  return {
    content,
    tells: { gradientText, emoji, buzzwords: buzz, centeredParagraphs: `${centered}/${paras.length}`, titleCaseLabels: `${titleCase}/${labels.length}`,
             dominantHue: dominant, violetDominant: dominant !== null && dominant >= 275 && dominant <= 320 },
    system: { fontSizes: fontSizes.size, fontFamilies: [...families], chromaticHueBuckets: hues.length, radii: radii.size, elementsWithShadow: shadows },
    numbers: { numericCells: numeric.length, tabular },
    forms: { fields: fields.length, unlabeled: unlabeled.length, placeholderOnly: unlabeled.filter(f => f.placeholder).length },
  };
};

const motionFacts = () => {
  let motion = 0, reducedQuery = false;
  for (const sheet of document.styleSheets) {
    let rules; try { rules = sheet.cssRules; } catch { continue; }
    const walk = list => { for (const r of list) {
      if (r.type === CSSRule.KEYFRAMES_RULE) motion++;
      if (r.style && ((r.style.transitionDuration && !/^0s/.test(r.style.transitionDuration)) || (r.style.animationName && r.style.animationName !== "none"))) motion++;
      if (r.conditionText && r.conditionText.includes("prefers-reduced-motion")) reducedQuery = true;
      if (r.cssRules) walk(r.cssRules);
    } };
    walk(rules);
  }
  const scripts = [...document.scripts].map(s => s.textContent).join("\n");
  return { motionRules: motion, reducedMotionHandled: reducedQuery || scripts.includes("prefers-reduced-motion") };
};

const result = { url: path.relative(process.cwd(), runDir) };
try {
  // Desktop, light
  const d = await open(1440, "light");
  result.consoleErrors = [...d.errors]; // before axe, which can log its own errors
  result.axeDesktopLight = await axe(d.page);
  Object.assign(result, await d.page.evaluate(pageFacts));
  result.motion = await d.page.evaluate(motionFacts);
  result.luminanceLight = await meanLuminance(d.page);
  await d.page.screenshot({ path: path.join(shots, "desktop-light.jpg"), type: "jpeg", quality: 72, fullPage: true });
  await d.page.reload({ waitUntil: "networkidle" }).catch(() => {});
  result.focus = await focusCheck(d.page);
  await d.page.close();

  // Desktop, dark
  const k = await open(1440, "dark");
  result.luminanceDark = await meanLuminance(k.page);
  result.axeDesktopDark = (await axe(k.page)).filter(v => v.id === "color-contrast");
  await k.page.screenshot({ path: path.join(shots, "desktop-dark.jpg"), type: "jpeg", quality: 72, fullPage: true });
  await k.page.close();
  const L = result.luminanceLight, D = result.luminanceDark;
  result.darkMode = L - D > 0.25 ? "follows system" : D < 0.35 && L < 0.35 ? "dark only" : "light only";

  // Mobile
  const m = await open(390, "light");
  result.overflow390 = await m.page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  result.axeMobile = (await axe(m.page)).filter(v => ["target-size", "color-contrast", "meta-viewport"].includes(v.id));
  await m.page.screenshot({ path: path.join(shots, "mobile-light.jpg"), type: "jpeg", quality: 72, fullPage: true });
  await m.page.close();
} catch (e) {
  result.auditError = String(e);
}
await browser.close();
fs.writeFileSync(path.join(runDir, "audit.json"), JSON.stringify(result, null, 2));
console.log(path.basename(path.dirname(path.dirname(runDir))), path.basename(path.dirname(runDir)), path.basename(runDir),
  result.auditError ? "AUDIT ERROR " + result.auditError : `axe ${result.axeDesktopLight.length} · overflow ${result.overflow390} · ${result.darkMode}`);
