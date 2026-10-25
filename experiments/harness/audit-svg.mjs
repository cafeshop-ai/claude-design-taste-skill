// Present and audit SVG deliverables the same way for every run.
//   node audit-svg.mjs <run-dir> logo            (expects output/logo.svg, output/mark.svg)
//   node audit-svg.mjs <run-dir> svg-animation   (expects output/caught-up.svg, loader.svg, or one .svg)
// Writes <run-dir>/audit.json, <run-dir>/preview.html, and <run-dir>/shots/*.jpg
import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const runDir = path.resolve(process.argv[2]);
const kind = process.argv[3];
const tabLabel = process.argv[4] || "Fernway Books"; // brand name shown in the browser-tab mockup
const out = path.join(runDir, "output");
const shots = path.join(runDir, "shots");
fs.mkdirSync(shots, { recursive: true });

// Find a deliverable even if the agent named it slightly differently.
function find(name, fallbackPattern) {
  const exact = path.join(out, name);
  if (fs.existsSync(exact)) return exact;
  const svgs = fs.readdirSync(out, { recursive: true }).filter(f => f.endsWith(".svg"));
  const hit = svgs.find(f => fallbackPattern.test(path.basename(f)));
  return hit ? path.join(out, hit) : null;
}

function svgFacts(file) {
  const src = fs.readFileSync(file, "utf8");
  const colors = new Set((src.match(/#[0-9a-f]{3,8}\b|rgba?\([^)]*\)|oklch\([^)]*\)|hsla?\([^)]*\)/gi) || []).map(c => c.toLowerCase()));
  return {
    file: path.relative(out, file), bytes: Buffer.byteLength(src),
    elements: (src.match(/<(path|circle|rect|ellipse|line|polyline|polygon|text|use|g|image)\b/g) || []).length,
    distinctColors: colors.size,
    usesText: /<text\b/.test(src), usesWebFont: /@import|@font-face|fonts\.googleapis/.test(src),
    embedsRaster: /<image\b|data:image\/(png|jpe?g|webp)/.test(src),
    hasViewBox: /viewBox=/.test(src), hasTitle: /<title\b/.test(src) || /aria-label=/.test(src),
    css: { keyframes: (src.match(/@keyframes/g) || []).length, reducedMotion: /prefers-reduced-motion/.test(src) },
    smil: (src.match(/<animate(Transform|Motion)?\b|<set\b/g) || []).length,
    script: /<script\b/.test(src),
    durations: [...new Set((src.match(/(?<![\w-])\d*\.?\d+m?s\b/g) || []).slice(0, 20))],
  };
}

const page = html => `<!doctype html><meta charset="utf-8"><style>
  body{margin:0;font:13px/1.4 system-ui,sans-serif;color:#555;background:#fff}
  .sheet{display:grid;gap:24px;padding:32px;width:1100px}
  .row{display:flex;gap:24px;align-items:stretch}
  .panel{flex:1;display:grid;place-items:center;gap:12px;padding:40px;border:1px solid #e5e5e5;border-radius:8px;min-height:180px}
  .dark{background:#151515;border-color:#151515;color:#aaa}
  .sizes{display:flex;gap:28px;align-items:end}
  .sizes figure{margin:0;display:grid;justify-items:center;gap:6px}
  .tab{display:flex;align-items:center;gap:8px;width:220px;padding:8px 12px;border-radius:8px 8px 0 0;background:#f1f1f1;color:#222}
  .tab.d{background:#2a2a2a;color:#eee}
  img{display:block}
</style><div class="sheet">${html}</div>`;

const result = { kind };
const browser = await chromium.launch({ args: ["--no-sandbox"] });
try {
  if (kind === "logo") {
    const logo = find("logo.svg", /logo|lockup|full/i);
    const mark = find("mark.svg", /mark|icon|favicon|symbol/i);
    // Dark panels show the designer's own dark-background version when they made one.
    const variant = (main, re) => {
      if (!main) return null;
      const dir = path.dirname(main), base = path.basename(main, ".svg");
      const hit = fs.readdirSync(dir).find(f => f.endsWith(".svg") && f !== path.basename(main) && f.startsWith(base) && re.test(f));
      return hit ? path.join(dir, hit) : null;
    };
    const DARK = /reversed|dark|inverse|negative|white|light|knockout/i;
    const logoDark = variant(logo, DARK) || logo, markDark = variant(mark, DARK) || mark;
    result.darkVariants = { logo: logoDark !== logo ? path.basename(logoDark) : null, mark: markDark !== mark ? path.basename(markDark) : null };
    result.logo = logo && svgFacts(logo);
    result.mark = mark && svgFacts(mark);
    const rel = f => path.relative(runDir, f);
    const sizes = (dark) => [128, 64, 32, 16].map(s => `<figure><img src="${rel(dark ? markDark : mark)}" width="${s}" height="${s}" alt=""><figcaption>${s}px</figcaption></figure>`).join("");
    const cap = f => `<figcaption style="font-size:11px;opacity:.7">${path.basename(f)}</figcaption>`;
    fs.writeFileSync(path.join(runDir, "preview.html"), page(`
      <div class="row"><div class="panel">${logo ? `<img src="${rel(logo)}" style="width:440px;max-height:220px;object-fit:contain" alt="">` : "logo.svg missing"}</div>
      <div class="panel dark">${logo ? `<img src="${rel(logoDark)}" style="width:440px;max-height:220px;object-fit:contain" alt="">${cap(logoDark)}` : ""}</div></div>
      <div class="row"><div class="panel">${mark ? `<div class="sizes">${sizes()}</div>` : "mark.svg missing"}</div>
      <div class="panel dark">${mark ? `<div class="sizes">${sizes(true)}</div>` : ""}</div></div>
      <div class="row"><div class="panel">${mark ? `<div class="tab"><img src="${rel(mark)}" width="16" height="16" alt="">${tabLabel}</div>` : ""}</div>
      <div class="panel dark">${mark ? `<div class="tab d"><img src="${rel(markDark)}" width="16" height="16" alt="">${tabLabel}</div>` : ""}</div></div>`));
    const p = await browser.newPage({ viewport: { width: 1164, height: 800 } });
    await p.goto("file://" + path.join(runDir, "preview.html"), { waitUntil: "networkidle" });
    await p.screenshot({ path: path.join(shots, "sheet.jpg"), type: "jpeg", quality: 85, fullPage: true });
    await p.close();
  }

  if (kind === "svg-animation") {
    const anim = find("caught-up.svg", /caught|empty|inbox|done|loader|loading|spinner|buffer|payment|sent|\.svg$/i);
    result.animation = anim && svgFacts(anim);
    if (anim) {
      // Inline the SVG so CSS, SMIL, and scripted animation all run.
      const inline = fs.readFileSync(anim, "utf8").replace(/<\?xml[^>]*>/, "");
      fs.writeFileSync(path.join(runDir, "preview.html"), page(`<div class="row">
        <div class="panel" id="stage" style="flex:none;width:420px;height:320px"><div id="art" style="width:240px">${inline}</div></div></div>`)
        .replace("</style>", "#art svg{width:100%;height:auto;max-height:240px}</style>"));
      const frames = [];
      for (const reduce of ["no-preference", "reduce"]) {
        const p = await browser.newPage({ viewport: { width: 1164, height: 420 }, reducedMotion: reduce });
        await p.goto("file://" + path.join(runDir, "preview.html"), { waitUntil: "domcontentloaded" });
        const stage = p.locator("#stage");
        const n = reduce === "reduce" ? 2 : 10;
        const local = [];
        for (let i = 0; i < n; i++) {
          await p.waitForTimeout(i === 0 ? 100 : (reduce === "reduce" ? 1200 : 650)); // first frame catches entrances
          local.push((await stage.screenshot({ type: "png" })).toString("base64"));
        }
        // Pixel difference between first and last frame, measured in the page.
        const diff = await p.evaluate(async ([a, b]) => {
          const load = async s => { const i = new Image(); i.src = "data:image/png;base64," + s; await i.decode(); return i; };
          const [ia, ib] = await Promise.all([load(a), load(b)]);
          const c = document.createElement("canvas"); c.width = ia.width; c.height = ia.height; const x = c.getContext("2d");
          x.drawImage(ia, 0, 0); const da = x.getImageData(0, 0, c.width, c.height).data;
          x.drawImage(ib, 0, 0); const db = x.getImageData(0, 0, c.width, c.height).data;
          let changed = 0; for (let k = 0; k < da.length; k += 4) if (Math.abs(da[k] - db[k]) + Math.abs(da[k + 1] - db[k + 1]) + Math.abs(da[k + 2] - db[k + 2]) > 30) changed++;
          return +(changed / (da.length / 4)).toFixed(4);
        }, [local[0], local[local.length - 1]]);
        result[reduce === "reduce" ? "changedPixelsReduced" : "changedPixels"] = diff;
        if (reduce !== "reduce") frames.push(...local);
        await p.close();
      }
      result.stopsUnderReducedMotion = result.changedPixelsReduced < 0.002;
      // Filmstrip: 10 frames, 650ms apart from load (entrance plus a 6s loop), 5 per row.
      const strip = await browser.newPage({ viewport: { width: 1720, height: 200 } });
      await strip.setContent(`<body style="margin:0;display:grid;grid-template-columns:repeat(5,340px);gap:4px;background:#ddd">${frames.map(f => `<img src="data:image/png;base64,${f}" style="width:340px;height:auto">`).join("")}</body>`);
      await strip.screenshot({ path: path.join(shots, "filmstrip.jpg"), type: "jpeg", quality: 85, fullPage: true });
      await strip.close();
    }
  }
} catch (e) {
  result.auditError = String(e);
}
await browser.close();
fs.writeFileSync(path.join(runDir, "audit.json"), JSON.stringify(result, null, 2));
console.log(path.relative(process.cwd(), runDir), result.auditError ? "AUDIT ERROR " + result.auditError : "ok");
