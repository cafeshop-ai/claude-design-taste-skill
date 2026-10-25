# Logo design

A logo is a small, durable decision: a mark people should recognize at a glance, at 16 pixels, in one color, for years. Good logos are simple, specific to the name and business, and built with care at the level of single anchor points.

## Contents
1. Before drawing: the brief and the concept
2. Choosing the kind of logo
3. Principles
4. Construction and optical correction
5. Type in logos
6. Color and versions
7. The small mark and favicon
8. SVG hygiene
9. Presenting it

---

## 1. Before drawing: the brief and the concept

- **Read the name for ideas.** Millrace, a coffee roaster: a millrace is the channel that carries water to a mill wheel; roasting is heat and turning; the town is old and industrial. Sketch associations before shapes: what's ownable in *this* name?
- **Avoid the first cliché, or twist it.** The first idea for a coffee roaster is a bean or a steaming cup; for a law firm, scales or columns; for a tech company, a hexagon. These are what everyone else did. A good mark either finds a less obvious idea (for Millrace, a water channel curving into a wheel that also reads as a roasting drum) or executes the familiar idea so specifically that it becomes theirs.
- **Consider three directions, then commit to one.** In your head or in notes: a wordmark-led direction, a symbol-led direction, and a lettermark. Pick the one that best fits the name and how the logo will be used, and say why in a sentence.
- **Personality in a phrase**, as with any direction: "literary and warm, not twee"; "precise and quiet". Every later choice (typeface, weight, corner shape, color) should be traceable to it.

## 2. Choosing the kind of logo

| Kind | Use when | Watch out for |
|---|---|---|
| **Wordmark** (the name, carefully set) | Short or distinctive names; the name is the brand | Needs real typographic work, not just a font |
| **Lettermark / monogram** | Long names; a strong initial | Generic unless the letterform itself is distinctive |
| **Symbol + wordmark (lockup)** | Most small businesses; app icons and favicons needed | Symbol and type must feel like one family |
| **Emblem** (text inside a shape) | Heritage, crafts, food and drink | Fails at small sizes; always provide a simplified mark |

Most briefs that ask for "a logo and an icon" want a lockup: a symbol that can stand alone, and a wordmark set beside or below it.

## 3. Principles

- **Simple:** recognizable when blurred, at 16px, and drawn from memory. Count the shapes; fewer is stronger. Fine detail (veins on a leaf, wood grain, steam wisps) disappears at small sizes and makes large sizes busy.
- **Distinctive:** it shouldn't be confusable with the category's defaults or with famous marks.
- **Appropriate:** a children's toy shop and an antiques dealer need different marks, even with the same idea.
- **Timeless:** no gradients, glows, bevels, drop shadows, or trend effects in the master logo. A mark that only works in full color with effects isn't finished.
- **Versatile:** works in one color, reversed on dark, tiny, huge, embroidered, stamped.
- **Balanced weight:** the symbol and the wordmark should carry similar visual weight; a heavy symbol beside a hairline serif looks pasted together.

## 4. Construction and optical correction

- **Build on a grid** (e.g. a 24 or 48 unit square for the symbol) and use consistent stroke weights and corner radii, the same way an icon set is built.
- **Few, well-placed anchor points.** Smooth curves come from few points at extremes, not many points along the curve.
- **Optical, not mathematical:** circles and pointed shapes must overshoot the baseline and cap height slightly (about 1–3%) to look the same size as squares; horizontal strokes are drawn slightly thinner than vertical ones to look equal; visual centering often sits a little above the geometric center.
- **Negative space is part of the mark.** Check counters and gaps at small sizes; gaps narrower than ~1/16 of the mark's width fill in at favicon size.
- **Test at every stage:** 16px, 32px, 128px, one color, reversed. A mark that only looks good at 400px isn't done.

## 5. Type in logos

- **Never depend on a font being installed.** An SVG logo with `<text>` renders in whatever font the viewer's machine has. Draw the letters as paths (convert outlined type, or construct the letterforms), so the logo looks the same everywhere.
- **Customize, don't just type.** Adjust kerning pair by pair (logo kerning is looser or tighter than text, and always manual), consider a ligature or one modified letter that echoes the symbol, and choose a weight that matches the symbol's stroke.
- **Wordmark size and spacing:** all-caps wordmarks need generous tracking (+5–15%); lowercase wordmarks usually want slightly tight tracking at display size.
- **Taglines don't belong in the primary logo.** "Coffee Roasters" in 6px caps under the name becomes an illegible smudge in most real uses. If it's needed, make it a separate lockup for large uses only.

## 6. Color and versions

- **Design in black first.** If it doesn't work in one color, color won't save it.
- **Then choose one or two colors** with meaning for the brand. Check contrast on light and dark backgrounds; a dark green that reads beautifully on cream disappears on black.
- **Deliver versions:** full color on light, reversed (light) for dark backgrounds, and one-color. In SVG, a single-color mark can use `fill="currentColor"` so it adapts to whatever text color surrounds it, or ship separate `-dark` files.
- **Don't put a background rectangle in the master logo** unless the background is part of the mark (an app icon is a different deliverable).

## 7. The small mark and favicon

- **Redraw for small sizes; don't just scale down.** At 16px a mark has 256 pixels. Thicken strokes, remove secondary details, open up gaps, and enlarge it to fill most of the square (leave about 1px padding).
- **Snap to the pixel grid at 16 and 32**: align horizontal and vertical edges to whole pixels in a 16-unit viewBox so edges render crisp instead of blurry.
- **Check it in context:** a browser tab on light and dark themes, next to other favicons. Contrast with both tab colors matters more than color fidelity; a mid-tone or a mark with its own small background tile is often more robust than dark-on-transparent.
- **Ship:** an SVG favicon (`<link rel="icon" href="mark.svg" type="image/svg+xml">`; it can even switch colors with `@media (prefers-color-scheme: dark)` inside the SVG), plus a 32px PNG and a 180px apple-touch-icon for platforms that need raster.

## 8. SVG hygiene

- A `viewBox` with the artwork tightly but evenly framed; width/height attributes either omitted or matching the viewBox ratio.
- `<title>` with the company name, and `role="img"`, so it's accessible when inlined.
- Paths with coordinates rounded to 1–2 decimals; no empty groups, editor metadata, hidden layers, or embedded raster images.
- Shapes merged where they share a color, so there are no hairline seams between adjacent pieces.
- One file per version (`logo.svg`, `logo-reversed.svg`, `mark.svg`), named plainly.

## 9. Presenting it

When you deliver a logo, show it the way a designer would: the lockup on light and on dark, the mark at 128, 32, and 16px, and a one-paragraph rationale (the idea, why this kind of logo, why these colors and type). Keep the rationale specific; "modern and clean" says nothing.
