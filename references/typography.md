# Typography

Most of an interface is text. Get the type right and a plain layout looks considered. Get it wrong and nothing else can rescue it.

## Contents
1. Choosing typefaces
2. Pairing
3. A shortlist of good faces
4. The type scale
5. Line height, line length, letter spacing
6. Weight and emphasis
7. Building hierarchy with type
8. Numbers
9. Typographic details that signal care
10. Loading web fonts
11. Fluid type
12. Base CSS

---

## 1. Choosing typefaces

Pick for the job first and the personality second.

**Practical criteria**
- **Legible at small sizes.** A generous x-height, open apertures (c, e, s don't close up), and clearly different I/l/1 and O/0. Interfaces live at 13–16px.
- **A real family.** At least regular, medium, semibold, and bold, ideally with italics. A variable font gives every weight in one file.
- **Tabular figures** (`tnum`) if you show numbers in tables, prices, or timers.
- **Language coverage** for every script the product needs.
- **Licensing and hosting.** Google Fonts and system fonts are free to use; commercial faces need a license.

**Personality.** Every face carries associations. Geometric sans (Futura, Poppins): modern, friendly, sometimes naive. Grotesque/neo-grotesque (Helvetica, Inter, Geist): neutral, rational, technical. Humanist sans (Source Sans, Fira Sans, Gill Sans): warm, readable, approachable. Transitional/old-style serif (Source Serif, Newsreader, Garamond): literary, trustworthy, editorial. Slab (Roboto Slab, Zilla Slab): sturdy, mechanical. Mono: code, technical, raw.

**The system font stack** (`system-ui, -apple-system, "Segoe UI", Roboto, …`) is a legitimate choice for apps. It loads instantly, feels native, and is tuned for screens. Choose it for tools; choose a custom face when the brand needs a voice.

**Defaults are fine; unexamined defaults are not.** Inter is excellent. But "Inter, because it's what everything uses" makes your product look like everything. If brand character matters (marketing sites, consumer products, editorial), choose a face with intent.

## 2. Pairing

- **One family is usually enough.** Get contrast from size, weight, and color. Fewer faces means more coherence and faster loading.
- **For two faces, contrast them along one clear axis**, typically a serif for display and a sans for text (or the reverse), with similar proportions (x-height, width) so they sit well together.
- **Don't pair two similar faces** (two neo-grotesques, two geometric sans). The near-miss reads as a mistake.
- **Superfamilies are safe pairings:** IBM Plex (Sans/Serif/Mono), Source (Sans/Serif/Code), Roboto (Sans/Serif/Mono/Slab), Noto, Merriweather (Serif/Sans), Literata.
- **A monospace is a third voice** for code, IDs, and technical data, not decoration. Using mono for headings to look "technical" is a cliché unless the product really is a developer tool.
- **Display faces belong only at display sizes.** An expressive face for a 64px headline will be illegible at 14px.

## 3. A shortlist of good faces

All of these are on Google Fonts unless noted. Ones marked ⚠ are overused enough to read as "default"; fine to use, but on purpose.

**Neutral UI sans:** Inter ⚠, Geist, IBM Plex Sans, Public Sans, Source Sans 3, Figtree, Onest, Instrument Sans, Hanken Grotesk, Schibsted Grotesk.
**Sans with character:** Manrope, DM Sans ⚠, Plus Jakarta Sans ⚠, Bricolage Grotesque (expressive), Space Grotesk ⚠ (quirky/tech), Familjen Grotesk, Archivo (has widths), Sora, Outfit (geometric), Red Hat Display/Text, Work Sans.
**Readable serifs for text:** Source Serif 4, Newsreader, Literata, Spectral, Crimson Pro, Lora, Merriweather, Alegreya, EB Garamond.
**Display serifs:** Fraunces (soft, variable "wonk"), Instrument Serif (elegant, condensed), DM Serif Display, Playfair Display ⚠, Cormorant (very high contrast, display only), Young Serif, Gloock.
**Mono:** JetBrains Mono, IBM Plex Mono, Geist Mono, Source Code Pro, Fira Code, Space Mono (display only), Commit Mono (self-host; not on Google Fonts).
**Accessibility-focused:** Atkinson Hyperlegible (strongly distinct characters), Lexend.

**Starting pairings**
| Feel | Display | Text |
|---|---|---|
| Precise product UI | Geist or Inter (tighter tracking) | same |
| Calm, trustworthy | IBM Plex Sans | IBM Plex Sans (+ Plex Mono) |
| Editorial, literary | Newsreader or Fraunces | Source Serif 4 or same serif; sans for UI |
| Modern editorial | Instrument Serif | Instrument Sans or Inter |
| Warm, friendly | Bricolage Grotesque or Fraunces | Figtree or DM Sans |
| Swiss, graphic | Archivo (expanded/black) or Inter Display | Inter |
| Technical, dev tool | Geist or JetBrains Mono for accents | Geist |
| Luxurious, quiet | Cormorant or Instrument Serif, light, large | a restrained sans, small, tracked |

## 4. The type scale

Use a fixed set of sizes and nothing between them. A scale makes hierarchy legible because the jumps between levels are distinct and consistent.

**Choose a ratio based on context** (`scripts/scale.py` computes any of these):
- **1.125–1.2**: dense app UI, dashboards. Small, steady jumps.
- **1.25**: general web, docs.
- **1.333**: marketing, landing pages.
- **1.5+**: editorial and expressive display. Dramatic contrast between headline and body.

A hand-tuned scale that rounds to whole pixels is also fine and often better. A dependable one:

| Role | Size | Line height | Notes |
|---|---|---|---|
| Caption, meta | 12px | 16px | sparingly; never for anything someone must read carefully |
| Small / UI secondary | 14px | 20px | table cells, helper text, secondary labels |
| Body | 16px | 24px | the default for reading on the web |
| Large body / lead | 18–20px | 28px | intros, editorial body |
| H4 / card title | 20px | 28px | |
| H3 | 24px | 32px | |
| H2 | 30px | 36px | |
| H1 (app) | 36px | 40px | |
| H1 (site) / display | 48–72px | 1.0–1.1 | marketing heroes, editorial |

Rules of thumb:
- **Body text is 16px on the web.** 14–15px is acceptable for dense, frequently used apps; 18–21px for long-form reading. Never go below 12px for anything meaningful.
- **Most screens need 4–6 sizes.** If you count more than 8 distinct sizes, consolidate.
- **Adjacent levels must be clearly different.** 16 vs 17px is noise; if two levels look nearly the same size, separate them by weight or color, or merge them.
- **App headings are smaller than you think.** A settings page title at 24px semibold looks more professional than one at 40px bold. Big type belongs on marketing and editorial pages.

## 5. Line height, line length, letter spacing

**Line height (leading)** scales inversely with size:
- Body 14–18px: 1.5 (1.6–1.7 for long-form reading with long lines).
- Subheadings 20–30px: 1.25–1.35.
- Headings 30–48px: 1.1–1.2.
- Display 60px+: 1.0–1.1 (check that descenders and ascenders don't collide on multi-line headings).
- UI labels on a single line (buttons, nav) can use 1–1.25, since there's no second line to separate.
- Use unitless values (`line-height: 1.5`) so leading scales with the font size.

**Line length (measure):** 45–75 characters per line for body text; ~65ch is the sweet spot. Longer lines make the eye lose its place on the return sweep; shorter lines break up phrases. Set `max-width: 65ch` on prose. Narrow columns (sidebars, cards) can go down to ~35ch with slightly tighter leading.

**Letter spacing (tracking):**
- Large display type gets **tighter** tracking: −0.02em at 32–48px, −0.03 to −0.04em at 60px+. Fonts are spaced for text sizes, so at display sizes the gaps look loose.
- Body text: leave it at 0. The designer of the font set it.
- Very small text (≤12px) can take a touch of **positive** tracking (+0.01–0.02em).
- **UPPERCASE text always needs positive tracking** (+0.05–0.1em), and should be short: labels, eyebrows, small buttons. Never set sentences in caps.
- Some families ship display/text optical sizes (e.g. Inter Display, Fraunces with `opsz`). Use `font-optical-sizing: auto` with variable fonts that support it.

## 6. Weight and emphasis

- **Use two or three weights:** regular (400) for reading, medium or semibold (500–600) for labels, buttons, and headings, and perhaps bold (700) for rare strong emphasis or display.
- **Semibold usually beats bold for UI headings.** Bold at large sizes gets heavy and loud.
- **Light weights (300 and below) only at large sizes**, and never for body text on screens. They fail contrast in practice and render poorly on low-DPI screens.
- **Emphasize with one lever at a time.** Bigger and bolder and colored and uppercase is shouting.
- **Italic for emphasis within prose; semibold for UI emphasis.** Underline is reserved for links.
- **Watch for faux bold.** If a weight isn't loaded, browsers synthesize a smeared fake. Load the weights you use, or set `font-synthesis-weight: none`.

## 7. Building hierarchy with type

- **De-emphasize instead of emphasizing.** To make a title stand out, try making the surrounding text smaller or more muted before making the title bigger.
- **Three levels of text color** cover nearly everything: primary (headings, body), secondary (supporting text, labels), tertiary (captions, placeholders, timestamps). All must meet contrast.
- **Headings belong to what follows.** Put more space above a heading than below it (roughly 2:1), so it groups visually with its section rather than floating between sections.
- **Labels vs values.** In data displays, the value is usually the content, so make it larger or darker and the label small and muted. "Revenue" doesn't need to be bold; "$48,210" might.
- **Eyebrows** (small caps-tracked labels above headings) are useful for categorization. They're also a template cliché when slapped above every section. Use them only when they carry information.
- **Don't center long text.** Centered alignment works for 1–3 short lines (hero headline, empty state message). For anything longer, left-align; ragged centered edges make reading hard.

## 8. Numbers

- `font-variant-numeric: tabular-nums` wherever numbers align vertically (tables, lists of prices) or change in place (counters, timers, stock tickers). Without it, digits have different widths and columns and live values jitter.
- Right-align numeric columns so place values line up. Keep decimal places consistent within a column.
- Format numbers for humans: thousands separators (`Intl.NumberFormat`), sensible precision ($1.2M rather than $1,203,847.23 in a summary), units close to the number and visually quieter.
- `font-variant-numeric: slashed-zero` for codes and IDs where O/0 confusion matters.
- Old-style (lowercase-height) numerals suit running editorial text; lining numerals suit UI. Many fonts default to one; check.

## 9. Typographic details that signal care

These are small, and readers notice them without knowing why.
- **Real punctuation:** curly quotes “ ” ‘ ’ and apostrophes ’ (not straight " '), an ellipsis character …, an en dash for ranges (9–5, 2020–2024), an em dash for breaks—like this—and the multiplication sign × for dimensions (1920 × 1080).
- **Non-breaking spaces** between numbers and units (`10&nbsp;MB`) and in short phrases that shouldn't split.
- `text-wrap: balance` on headings (no single orphaned word on the last line) and `text-wrap: pretty` on paragraphs.
- **Hanging punctuation** for pull quotes (`hanging-punctuation: first` in Safari, or a negative text-indent).
- **Hyphenation** (`hyphens: auto` plus a `lang` attribute on `<html>`) for narrow justified or columnar text. Otherwise avoid justified text on the web; it creates rivers.
- **Links in body text are underlined.** Color alone fails for color-blind users. Use `text-underline-offset: 0.15–0.25em` and a thin `text-decoration-thickness` so underlines are elegant rather than heavy.
- **Optical alignment:** large headings can look indented relative to body text because of side bearings. Nudge with a small negative margin if it matters (hero headlines).

## 10. Loading web fonts

Fonts are often the largest render-blocking asset on a page. Treat them as a budget.
- **Limit files:** 2–4 font files total. A variable font covers all weights in one file.
- **Use WOFF2**, subset to the characters you need (Latin, or Latin-ext if needed).
- **Preload** the one or two files used above the fold: `<link rel="preload" href="/fonts/x.woff2" as="font" type="font/woff2" crossorigin>`.
- **`font-display: swap`** shows fallback text immediately and swaps in the web font when it arrives. `optional` avoids the swap entirely on slow connections (best for CLS; the web font appears on later visits).
- **Reduce layout shift from the swap** by tuning the fallback's metrics with `size-adjust`, `ascent-override`, and `descent-override` in a fallback `@font-face`. Tools like Fontaine and Capsize compute these, and Next.js `next/font` does it automatically.
- **Self-hosting** is fastest and most private. Google Fonts' CSS API is fine with `&display=swap` and `preconnect` to fonts.gstatic.com.

## 11. Fluid type

On marketing and editorial pages, let display sizes grow with the viewport so headlines are big on desktop without overflowing on phones:

```css
h1 { font-size: clamp(2.5rem, 1.84rem + 2.82vw, 4.375rem); } /* 40px at 375 → 70px at 1440 */
```

- Generate values with `scripts/scale.py`, which handles the math and keeps a `rem` term so text still scales with browser zoom. Pure `vw` sizes ignore zoom and fail WCAG 1.4.4.
- Body text usually needs little or no fluidity: 16px → 18px at most.
- App UIs generally shouldn't use fluid type. Fixed sizes keep dense layouts predictable.

## 12. Base CSS

```css
body {
  font-family: var(--font-sans);
  font-size: 1rem;
  line-height: 1.5;
  font-synthesis-weight: none;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3 { line-height: 1.15; text-wrap: balance; font-weight: 600; }
h1 { font-size: var(--text-4xl); letter-spacing: -0.02em; }
p  { text-wrap: pretty; }
.prose p { max-width: 65ch; }  /* opt-in: a global max-width makes centered paragraphs render off-center */
small, .caption { font-size: var(--text-sm); color: var(--color-text-muted); }
.eyebrow { font-size: var(--text-xs); font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase; color: var(--color-text-muted); }
.numeric { font-variant-numeric: tabular-nums; }
```
