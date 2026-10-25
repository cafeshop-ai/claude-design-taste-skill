// Heuristic walkthrough of a form flow on a phone-sized screen.
//   node interact.mjs <run-dir>      (expects <run-dir>/output/index.html)
// 1. Presses the primary button with nothing filled in: are errors shown? Does it wrongly advance?
// 2. Fills each step with plausible values and continues until a confirmation appears (max 8 steps).
// Writes <run-dir>/interaction.json and <run-dir>/shots/flow-NN.jpg.
// Generic by design, so it can miss custom widgets; treat "stuck" as "look at the screenshots".
import { chromium } from "playwright";
import fs from "node:fs";
import path from "node:path";

const runDir = path.resolve(process.argv[2]);
const shots = path.join(runDir, "shots");
fs.mkdirSync(shots, { recursive: true });
for (const f of fs.readdirSync(shots)) if (f.startsWith("flow-")) fs.rmSync(path.join(shots, f));

const browser = await chromium.launch({ args: ["--no-sandbox"] });
const page = await browser.newPage({ viewport: { width: 390, height: 844 }, hasTouch: true });
const errors = [];
page.on("pageerror", e => errors.push(e.message));
await page.goto("file://" + path.join(runDir, "output", "index.html"), { waitUntil: "networkidle" }).catch(() => {});
await page.waitForTimeout(600);

const PRIMARY = /\b(continue|next|send|submit|rsvp|book|review|confirm|request|finish|done|sign up|reserve|schedule)\b/i;
const SECONDARY = /\b(back|previous|edit|cancel|change)\b/i;
const DONE = /\b(thank|thanks|confirmed|you're booked|you’re booked|booking (is )?(confirmed|requested)|received|see you|all set|on the list|request sent|we'll be in touch|we’ll be in touch)\b/i;

const state = () => page.evaluate(() => {
  const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
  const fields = [...document.querySelectorAll("input:not([type=hidden]), select, textarea")].filter(vis).length;
  const errs = [...document.querySelectorAll("[aria-invalid=true], [role=alert], .error, .field-error, [class*=error i]")]
    .filter(el => vis(el) && (el.matches("input,select,textarea") || el.innerText.trim().length > 2)).length;
  const nativeInvalid = document.querySelectorAll("form :invalid:not(form)").length;
  return { text: document.body.innerText.replace(/\s+/g, " ").slice(0, 4000), fields, errs, nativeInvalid };
});

// The forward action, found the way a person would: a visible, enabled, filled
// button that isn't "Back", isn't in the header, and isn't an option chip or
// stepper. Keywords only break ties, so descriptive labels ("Choose date & time")
// aren't penalized.
async function clickPrimary() {
  const idx = await page.evaluate(([primarySrc, secondarySrc]) => {
    const PRIMARY = new RegExp(primarySrc, "i"), SECONDARY = new RegExp(secondarySrc, "i");
    const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
    const all = [...document.querySelectorAll("button, input[type=submit], a[role=button], [role=button]")];
    let best = -1, bestScore = 0;
    all.forEach((b, i) => {
      if (!vis(b) || b.disabled || b.getAttribute("aria-disabled") === "true") return;
      const label = (b.innerText || b.value || b.getAttribute("aria-label") || "").trim();
      if (!label || SECONDARY.test(label) || /^[+\-−–]$/.test(label)) return;
      if (b.closest("header, nav") || b.matches("[aria-pressed], [aria-checked], [role=radio], [role=option], [role=tab]")) return;
      if (/option|slot|chip|pill|stepper|counter|tab|toggle|day|date|time/i.test(b.className) && !/primary|submit|cta|next/i.test(b.className)) return;
      const m = getComputedStyle(b).backgroundColor.match(/[\d.]+/g) || [];
      const filled = m.length >= 3 && (m[3] === undefined || +m[3] > 0.5) && !(+m[0] > 235 && +m[1] > 235 && +m[2] > 235);
      const score = (filled ? 2 : 0) + (PRIMARY.test(label) ? 2 : 0) + (b.type === "submit" ? 1 : 0);
      if (score >= bestScore && score > 0) { best = i; bestScore = score; }
    });
    return best;
  }, [PRIMARY.source, SECONDARY.source]);
  if (idx < 0) return null;
  const b = (await page.$$("button, input[type=submit], a[role=button], [role=button]"))[idx];
  const label = ((await b.innerText().catch(() => "")) || (await b.getAttribute("value")) || "").trim();
  await b.scrollIntoViewIfNeeded().catch(() => {});
  await b.click({ timeout: 3000 }).catch(() => {});
  await page.waitForTimeout(700);
  return label;
}

async function fillVisible() {
  await page.evaluate(() => {
    const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== "hidden" && s.display !== "none"; };
    const set = (el, v) => { const proto = Object.getPrototypeOf(el); const d = Object.getOwnPropertyDescriptor(proto, "value"); d.set.call(el, v); el.dispatchEvent(new Event("input", { bubbles: true })); el.dispatchEvent(new Event("change", { bubbles: true })); el.dispatchEvent(new Event("blur", { bubbles: true })); };
    for (const el of document.querySelectorAll("input, textarea, select")) {
      if (el.disabled || el.readOnly || el.type === "hidden") continue;
      const label = (el.labels?.[0]?.innerText || el.name || el.id || el.placeholder || "").toLowerCase();
      if (el.tagName === "SELECT") { if (el.options.length > 1 && el.selectedIndex <= 0) { el.selectedIndex = 1; el.dispatchEvent(new Event("change", { bubbles: true })); } continue; }
      if (el.type === "radio") {
        const group = [...document.getElementsByName(el.name)];
        if (group.some(r => r.checked)) continue;
        const yes = group.find(r => /yes|accept|attend|joyful|coming|be there/i.test((r.labels?.[0]?.innerText || r.value || ""))) || group[0];
        (yes.labels?.[0] || yes).click(); continue;
      }
      if (el.type === "checkbox") {
        // Tick only what the flow requires (terms, consent); leave optional extras alone.
        if (!el.checked && vis(el.labels?.[0] || el) && (el.required || /agree|accept|terms|consent/i.test(el.labels?.[0]?.innerText || ""))) (el.labels?.[0] || el).click();
        continue;
      }
      if (!vis(el) || el.value) continue;
      const t = el.type;
      const v = t === "email" || /email/.test(label) ? "jordan@example.com"
        : t === "tel" || /phone/.test(label) ? "5551234567"
        : t === "number" ? String(Math.max(Number(el.min || 1), 2))
        : t === "date" ? (() => { const d = new Date(Date.now() + 5 * 864e5); return d.toISOString().slice(0, 10); })()
        : t === "time" ? "10:00"
        : /zip|postal/.test(label) ? "97214"
        : /address|street/.test(label) ? "12 Elm Street"
        : /city/.test(label) ? "Portland"
        : el.tagName === "TEXTAREA" ? "No nuts, please."
        : /last/.test(label) ? "Lee" : /first/.test(label) ? "Jordan" : "Jordan Lee";
      set(el, v);
    }
    // Custom option widgets (time slots, date tiles, chips): pick the first enabled
    // option in each row of siblings that has nothing selected yet.
    const groups = new Set();
    for (const el of document.querySelectorAll("[role=radio], [aria-pressed], [aria-checked], [role=option], [data-slot], [data-date], [data-time], button[class*=slot i], button[class*=day i]")) {
      if (!vis(el) || el.disabled || el.getAttribute("aria-disabled") === "true" || el.tagName === "INPUT") continue;
      let g = el.parentElement;
      while (g && g.children.length === 1 && g.parentElement) g = g.parentElement;
      if (!g || groups.has(g)) continue;
      groups.add(g);
      if (g.querySelector("[aria-checked=true], [aria-pressed=true], [aria-selected=true], .selected, .is-selected, .active")) continue;
      el.click();
    }
  });
  await page.waitForTimeout(300);
}

const result = { steps: [] };
const shot = async n => page.screenshot({ path: path.join(shots, `flow-${String(n).padStart(2, "0")}.jpg`), type: "jpeg", quality: 70, fullPage: true });

// 1. Empty submit
const before = await state();
await shot(0);
const label0 = await clickPrimary();
const afterEmpty = await state();
result.emptySubmit = { button: label0, errorsShown: afterEmpty.errs > before.errs ? "custom" : afterEmpty.nativeInvalid > 0 && afterEmpty.text === before.text ? "native browser bubble" : "none", advanced: label0 !== null && afterEmpty.text !== before.text && afterEmpty.errs <= before.errs && !DONE.test(afterEmpty.text) && afterEmpty.fields !== before.fields };
await shot(1);

// 2. Walk through
let n = 2, completed = DONE.test(afterEmpty.text) && afterEmpty.fields === 0;
for (let i = 0; i < 8 && !completed; i++) {
  const s0 = await state();
  await fillVisible();
  const label = await clickPrimary();
  const s1 = await state();
  await shot(n++);
  result.steps.push({ button: label, advanced: s1.text !== s0.text, errorsAfter: s1.errs });
  if (!label || s1.text === s0.text) break;
  // Finished if a final-sounding action led to a screen with no form fields, or
  // whose only way forward is starting over; or if the page says so.
  const finalAction = /\b(confirm|book|send|submit|request|finish|place|rsvp)\b/i.test(label);
  const nextLabel = await page.evaluate(() => [...document.querySelectorAll("button, a")].filter(b => b.offsetParent).map(b => b.innerText.trim()).join(" | "));
  completed = DONE.test(s1.text) || (finalAction && (s1.fields === 0 || /\b(another|again|start over|new booking|book again|done|close)\b/i.test(nextLabel)));
}
result.completed = completed;
result.stepsTaken = result.steps.filter(s => s.advanced).length;
result.pageErrors = errors;
await browser.close();
fs.writeFileSync(path.join(runDir, "interaction.json"), JSON.stringify(result, null, 2));
console.log(path.relative(process.cwd(), runDir), JSON.stringify({ empty: result.emptySubmit, steps: result.stepsTaken, completed }));
