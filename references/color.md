# Color

Color is the loudest tool in the kit, so it's the one most often overused. In a well-designed interface, neutrals do almost all the work, and color appears only where it means something: here's what you can act on, here's what's selected, here's what went wrong.

## Contents
1. The role model: what color is for
2. Palette anatomy
3. Why OKLCH, and how to build ramps
4. Neutrals
5. Choosing an accent
6. Semantic tokens
7. Contrast
8. Interactive state colors
9. Dark mode
10. Gradients, transparency, and tints
11. Color-blindness and meaning
12. Workflow with the scripts

---

## 1. The role model: what color is for

Before choosing a single hex value, decide what color will *mean* in this interface:

| Role | Typical use | Share of the screen |
|---|---|---|
| Neutral | backgrounds, surfaces, text, borders, icons | ~90% |
| Accent | primary actions, links, focus, selection, key highlights | ~5–10% |
| Status | error, warning, success, info, and nothing else | only when there's a status |
| Data | charts and categorical coding | inside visualizations |
| Brand moments | a hero band, illustrations, marketing accents | deliberate, rare |

If the accent appears on decorative things (icon backgrounds, section dividers, random headings), it stops signaling "actionable", and users lose their best cue for where to click.

**Test:** convert a screenshot to grayscale. The hierarchy should still read. If it doesn't, the problem is structural (size, weight, spacing), and adding color won't fix it.

## 2. Palette anatomy

A complete, practical palette:
- **One neutral ramp**, 11 steps (50–950), slightly tinted.
- **One accent ramp**, 11 steps.
- **Four status hues** (danger, warning, success, info), each needing just a solid (text and icons) and a subtle (background) version per theme. Full ramps are optional.
- Optionally a **second brand color** for marketing surfaces only. Keep it out of the product UI.
- **Data colors** for charts if needed (see a data-viz guide for categorical and sequential palettes).

Resist adding more. Every extra hue is a decision you'll have to apply consistently forever.

## 3. Why OKLCH, and how to build ramps

HSL is a lie about lightness: `hsl(60 100% 50%)` (yellow) and `hsl(240 100% 50%)` (blue) have the same "L" but look wildly different in brightness and contrast. Build ramps in HSL and step 500 will be legible in blue and unreadable in yellow.

**OKLCH** (`oklch(L C H)`) is perceptually uniform: L is perceived lightness (0–1), C is chroma (colorfulness, roughly 0–0.37), H is hue angle. Equal L means roughly equal perceived lightness and similar contrast, across hues. It's supported in all modern browsers.

**Ramp construction principles**
- **Fix lightness per step across all ramps**, so `--blue-600` and `--red-600` behave the same way against white. That makes rules like "600 is the button color" and "500 is the lightest text step" hold for every hue.
- **Chroma peaks in the mid-tones** (400–600) and falls off toward 50 and 950. Very light and very dark colors can't hold much chroma in sRGB, and forcing it produces garish tints or out-of-gamut clipping.
- **Hue may drift slightly across the ramp.** Yellows look muddy and olive when darkened, so shift them toward orange (lower hue) at the dark end. Blues can shift slightly toward cyan at the light end. `scripts/color.py ramp --hue-shift` does this.
- **Gamut-map, don't clip.** Reduce chroma until the color fits sRGB, rather than letting channels clip (which shifts hue). The script does this.

Lightness targets that work (used by `assets/tokens.css` and the script):

| Step | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 950 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| L | .985 | .967 | .925 | .870 | .730 | .560 | .490 | .420 | .345 | .270 | .200 |

Roughly: 50–100 for tinted backgrounds, 200–300 for borders and subtle fills, 400 for disabled or decorative marks and dark-mode accents, 500–600 for text-safe color, 600–700 for solid buttons in light mode, 800–950 for text and dark surfaces.

## 4. Neutrals

Neutrals are the bulk of your interface, so their temperature sets the mood more than the accent does.
- **Pure gray** (chroma 0): stark, neutral, a little clinical. Fine for photo-heavy or brand-heavy sites where you want no interference.
- **Cool gray** (hue ~250–265, chroma 0.005–0.015): crisp, technical, "software". The common default.
- **Warm gray** (hue ~60–80, chroma 0.005–0.015): paper-like, friendly, editorial, calmer on the eyes.
- **Brand-tinted gray** (accent hue, very low chroma): ties the whole interface to the brand subtly. The tint should be felt, not seen.

Don't mix temperatures. A warm beige background with cool blue-gray text looks dirty.

**How many grays to actually use:** typically a background, one or two surface levels, two border weights, and three text levels. That's 7–8 neutral tokens, not 11 ad-hoc grays.

**Text color:** near-black (L ~0.2) rather than pure #000 is slightly softer on white for long reading, but don't go so light that body text looks washed out. Secondary text should still pass 4.5:1.

## 5. Choosing an accent

- **Meaning first:** the accent will mark "do this" and "you are here". It needs to stand out from the neutrals and be distinct from the status colors.
- **Beware red, orange, and green as the primary accent.** Users read them as error, warning, and success. If the brand is red, consider using it for brand moments and a neutral (near-black) for primary buttons. Near-black primary buttons are a strong, modern choice in general.
- **Blue is the safe default** because it's universally read as "interactive" and doesn't collide with status colors. Its downside is that it's generic. Consider a specific blue (a deep cobalt, a sky, a slate) or a less expected hue (teal, violet, a deep green for a finance product) when brand matters.
- **Chroma sets personality:** 0.08–0.12 is muted and sophisticated, 0.13–0.17 is confident, 0.18 and up is vivid and playful (and harder to use in large areas).
- **Text on the accent:** light hues (yellow, lime, cyan, amber) need dark text; deep hues take white. Always check (`color.py contrast`).
- **The #6366f1/#8b5cf6 indigo-violet** (and indigo-to-pink gradients) is the signature of template and AI-generated UI. Avoid it unless it's genuinely the brand.

## 6. Semantic tokens

Components should never reference raw ramp steps (`--blue-600`) or hex codes. They reference **roles**, which map to different ramp steps in each theme. This is what makes theming, dark mode, and rebrands possible without touching components.

A complete, minimal set (as in `assets/tokens.css`):

```
Surfaces    --color-bg, --color-surface, --color-surface-sunken, --color-surface-raised,
            --color-surface-hover, --color-surface-active, --color-overlay,
            --color-surface-inverse + --color-text-inverse (toasts, tooltips)
Text        --color-text, --color-text-muted, --color-text-subtle, --color-text-disabled
Lines       --color-border, --color-border-strong, --color-border-control
Accent      --color-accent, -hover, -active, -contrast, -subtle, -subtle-text, --color-link, --color-focus
Status      --color-danger / -subtle / -solid, --color-warning / -subtle, --color-success / -subtle, --color-info / -subtle
            (base = text and icons; -subtle = backgrounds; -solid = fills that carry white text)
```

Name by role, not appearance. `--color-text-muted` survives a theme change; `--gray-500` used directly in a component doesn't.

## 7. Contrast

**WCAG 2.2 AA requirements** (the legal and practical baseline):
| Content | Minimum ratio |
|---|---|
| Body text (< 24px regular, < 18.66px bold) | 4.5:1 |
| Large text (≥ 24px regular, or ≥ 18.66px bold) | 3:1 |
| UI components and graphical objects needed to understand them: input borders, checkbox outlines, icons without text, focus indicators, chart lines | 3:1 against adjacent colors |
| Disabled controls, pure decoration, logos | exempt |

AAA asks for 7:1 for body text. It's worth targeting for long reading.

**APCA** (the candidate method for future WCAG) models perception better, especially for dark mode and for thin or small text. `scripts/color.py contrast` reports both. Rough APCA targets: Lc 75+ for body text, 60+ for other readable text, 45+ for large headings and icons, 30+ for placeholder and disabled text, 15+ for dividers.

**The most common failures:**
- Light gray body or secondary text (#999 on white is 2.8:1, and #aaa is worse).
- Placeholder text used as the only label, in light gray.
- Input borders at #e5e5e5 (1.3:1), so the field is invisible to low-vision users. Form control boundaries need 3:1, which is why tokens.css has a separate `--color-border-control`.
- White text on mid-tone buttons (bright blue, green, orange). Use a deeper shade or dark text.
- Text over images without a scrim or overlay.
- Thin fonts at light colors: they pass the calculator but read lighter in practice.

## 8. Interactive state colors

Derive states from the ramp so they're consistent:
- **Hover:** one step darker in light mode (600 → 700), one step lighter in dark mode. For neutral or ghost elements, overlay a translucent tint (`--color-surface-hover`) so it works on any background.
- **Active/pressed:** two steps from rest, or a stronger tint.
- **Selected:** a subtle accent background (`--color-accent-subtle`) plus accent text or a marker. Don't use a solid accent fill for large selected areas; it's too loud.
- **Focus:** a 2px ring in the accent (or a dedicated focus color) with an offset, at 3:1 or better against the surrounding surface.
- **Disabled:** reduced contrast and no hover response. Don't rely on opacity alone, which makes text fail contrast unpredictably on varied backgrounds. Also consider whether the control should be hidden or explained instead (see interaction.md).

## 9. Dark mode

Dark mode is a second palette designed on purpose, not `filter: invert()`.
- **Canvas:** dark gray, L ~0.14–0.20, not pure black. Pure black with white text causes halation (bright text appears to glow and bleed), and on OLED screens true-black areas smear during scrolling.
- **Elevation through lightness:** higher surfaces are lighter (bg 0.17 → surface 0.205 → raised 0.25). Shadows are nearly invisible on dark backgrounds, so lighter surfaces and subtle borders carry the depth.
- **Borders matter more:** use low-alpha white (`oklch(1 0 0 / 0.08–0.12)`) so they adapt to whichever surface they sit on.
- **Text:** off-white (L ~0.93–0.96), not #fff, with secondary text around L 0.70.
- **Accents:** shift lighter (light-mode 600 → dark-mode ~400–500) and often slightly less chroma. Saturated colors vibrate against dark backgrounds.
- **Status colors** go lighter too (L ~0.72–0.80), and their subtle backgrounds become dark tints (L ~0.26).
- **Avoid large saturated fills.** A full-width bright banner that's fine in light mode is blinding in dark mode.
- **Images and illustrations:** consider slightly reducing brightness, providing dark variants of illustrations, and making sure transparent PNG logos don't vanish.
- **Implementation:**
  - `color-scheme: light dark` (or per theme) so native form controls, scrollbars, and system colors match.
  - Respect `prefers-color-scheme` by default, and allow an explicit override with `[data-theme]` on `<html>`, persisted per user.
  - Set the theme before first paint (inline script in `<head>`) to avoid a flash of the wrong theme.
  - `light-dark(lightValue, darkValue)` is a handy CSS function for one-off values once `color-scheme` is set.
- **Check dark mode separately.** Every contrast pair, every state, every illustration. It's a different design.

## 10. Gradients, transparency, and tints

- **Gradients** work best subtle: same hue shifting in lightness, or two adjacent hues. Interpolate in OKLCH (`linear-gradient(in oklch, …)`) to avoid the gray "dead zone" sRGB produces between complementary colors. Big rainbow or purple-pink gradients are the clearest sign of template design.
- **Gradient text** is almost always a gimmick. It hurts legibility and signals "AI landing page". Use it only for a single, deliberate brand moment, if at all.
- **Transparency** is right for overlays, scrims, hover tints, and borders that must adapt to multiple surfaces. It's wrong for body text colors: alpha text over varying backgrounds has unpredictable contrast. Use solid text colors.
- **Tinted backgrounds** (accent-50, or a status subtle) can group or highlight a region. Use one tinted region per view at most, or the tints stop meaning anything.
- **Grain, noise, and glow** effects are seasoning. One subtle texture in a hero can add warmth; glowing blobs behind every section look like a template.

## 11. Color-blindness and meaning

About 1 in 12 men and 1 in 200 women have some color vision deficiency, most commonly red-green.
- Never use color as the only signal. Pair status colors with icons and text ("⚠ 3 errors"), mark required fields with text, underline links in body copy, and use patterns, labels, or direct annotations in charts.
- Avoid red/green as the only distinction (diff views, stock up/down, pass/fail). Add +/− signs, arrows, or position.
- Test by simulating deuteranopia and protanopia (browser devtools rendering emulation).

## 12. Workflow with the scripts

```bash
# Generate an accent ramp and see which steps take white or black text
python3 scripts/color.py ramp --hue 255 --chroma 0.15

# Warm neutral ramp as CSS custom properties
python3 scripts/color.py ramp --hue 70 --chroma 0.012 --name neutral --format css

# Yellow ramp that drifts toward orange as it darkens (avoids olive)
python3 scripts/color.py ramp --hue 95 --chroma 0.16 --hue-shift -25

# Check a pairing
python3 scripts/color.py contrast "#6b7280" white
python3 scripts/color.py contrast "oklch(0.95 0 0)" "oklch(0.2 0.01 260)"

# Convert a brand hex to OKLCH to find its hue and chroma
python3 scripts/color.py convert "#0f766e"
```

To adopt a brand color: convert it to find its H and C, set `--accent-h` and `--accent-c` in tokens.css, then verify `--color-accent` with `--color-accent-contrast` and `--color-link` on `--color-bg` in both themes.
