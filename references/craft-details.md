# Craft details: the last 10%

The difference between "fine" and "this feels great" is rarely the big layout. It's dozens of small decisions that nobody notices individually and everybody feels collectively. This is a catalog of them. Use it as a polish pass once structure, hierarchy, and states are solid. Polish on a broken structure is wasted.

## Contents
1. Restraint with a point of view
2. Type details
3. Color details
4. Edges, borders, and shadows
5. Alignment and optics
6. Interaction feel
7. Content and copy details
8. Images and media
9. Browser and platform details
10. Dark mode details

---

## 1. Restraint with a point of view

Restraint is the default in this skill, but restraint alone produces competent, forgettable work. The best interfaces are quiet almost everywhere and *memorable somewhere*.
- **Spend boldness in one place.** A very large confident headline, a single unexpected color, an illustration with real character, a beautifully crafted empty state, a delightful micro-interaction on the core action. One or two moments, not ten.
- **Concentrate richness where users spend time.** The core screen of the product deserves the most care. The settings page deserves clarity, not flair.
- **Consistency makes the bold moment land.** A distinctive accent only reads as intentional if everything around it is disciplined.
- **"Clean" is not a design direction.** If a description of the design would fit any product ("clean, modern, minimal"), push until it wouldn't.

## 2. Type details

- **Tighten display type.** −0.02em to −0.04em letter-spacing on headings above ~32px. It's the single most visible difference between amateur and professional headlines.
- **Lighten heading weight as size grows.** 600 at 24px may look right; at 64px, 500 or even 400 often looks more refined.
- **Optical sizes and stylistic sets.** Many good fonts ship alternates: Inter's `cv11` (single-story a), `ss01` (open digits), `tnum`; `font-feature-settings` or `font-variant-*` unlock them. Use `font-optical-sizing: auto` for fonts with an `opsz` axis.
- **Muted numbers' units.** "$48,210" with "/mo" in a smaller, muted style; "12.4%" with the % slightly smaller in large stat displays.
- **Balanced headlines, pretty paragraphs.** `text-wrap: balance` / `pretty`. Manually break hero headlines at phrase boundaries if needed (`<br>` hidden on mobile, or `&nbsp;` to bind words).
- **Non-breaking pairs:** "10&nbsp;GB", "Mr.&nbsp;Smith", "Page&nbsp;3", "⌘&nbsp;K".
- **Small caps for acronyms** in running editorial text (`font-variant-caps: all-small-caps`) so "NASA" doesn't shout.
- **Line-height on single-line UI text** (buttons, badges, nav) set to 1 or the exact control height, with padding doing the work, so text is truly centered.
- **Text color on tinted backgrounds:** on a blue-50 callout, use a dark blue text rather than neutral gray. Gray text on colored backgrounds looks dirty.

## 3. Color details

- **Tint your grays** a hair toward the brand hue or a temperature. Pure #888 grays look unconsidered next to anything colorful.
- **Shadows take the hue of the surface beneath,** not pure black: `oklch(0.2 0.02 <neutral-h> / 0.1)`.
- **Selection color** (`::selection`) in a light accent tint. A tiny brand touch everyone sees.
- **Caret and accent color** (`caret-color`, `accent-color`) so native checkboxes, radios, range sliders, and the text cursor match the accent.
- **Scrim color** slightly tinted toward the neutral hue, not pure black.
- **Hover on colored buttons** darkens in light mode, lightens in dark mode; ghost hovers use a translucent tint so they work on any surface.
- **One accent, one job.** If links, primary buttons, selected rows, focus rings, and charts all share the accent, check that the selected-row tint isn't confused with a button.

## 4. Edges, borders, and shadows

- **Image edges:** photos and screenshots on white backgrounds blur into the page. Add an inner hairline: `outline: 1px solid oklch(0 0 0 / 0.08); outline-offset: -1px;` (white at low alpha in dark mode).
- **Ring + shadow combo:** a 1px low-alpha ring (`box-shadow: 0 0 0 1px oklch(0 0 0 / 0.06), var(--shadow-md)`) gives floating elements a crisp edge plus soft depth. That's better than a heavier shadow alone.
- **Inner highlight on dark surfaces:** a 1px top inset highlight (`box-shadow: inset 0 1px 0 oklch(1 0 0 / 0.06)`) makes dark cards and buttons look physical and refined.
- **Borders are lighter than you think.** If you can see every border as a line, there are too many or they're too dark. Dividers should be felt.
- **Avoid double borders** where a bordered element sits flush inside another bordered container (tables in cards, inputs in toolbars). Remove one.
- **Concentric radii,** always: inner = outer − padding.
- **Consistent stroke weight** across borders, icons, and dividers (usually 1px borders, 1.5px icon strokes at 20px).

## 5. Alignment and optics

- **Optical centering:** play icons shift right ~1–2px; asymmetric icons (arrows, chevrons) often need a nudge; text in pill buttons can look low because of descender space, so adjust padding if needed.
- **Icon-to-text alignment** on the first line's center (or cap height), not the text block's center.
- **Hanging punctuation and bullets** so the text edge is clean.
- **Visual vs mathematical padding:** a button with a leading icon usually wants ~2px less padding on the icon side. A card with a full-bleed image wants slightly more padding below the image than at the sides.
- **Align across components:** the left edge of the page title, the first table column text, and the sidebar label text ideally share a line. Check edges across the whole screen, not just within a component.
- **Round, consistent sizes:** 40px controls, 16px icons, 24px gaps. Odd sizes like 37px or 15px are a sign of an eyeballed value.

## 6. Interaction feel

- **Press states on everything clickable,** within 50–100ms. Even a subtle darkening makes an interface feel responsive.
- **Hover only on hover-capable devices:** `@media (hover: hover)` wrapping hover styles prevents "sticky hover" on touch.
- **Hit area bigger than the visual:** small icon buttons get padding or a pseudo-element extending the clickable area to 32–44px.
- **Don't move things under the cursor:** hover effects that resize or shift elements cause jitter and misclicks. Change color, not geometry.
- **Instant for frequent actions,** animated for rare ones. A command palette opens instantly; an onboarding success can celebrate.
- **Preserve user context:** after an action, keep the scroll position, the selection, and the focus where they make sense. Losing your place is the most frustrating "small" bug.
- **Disable double submits** without making the button look broken: show a pending state.
- **Autofocus with care,** select-all on focus for fields people typically replace (rename dialogs), and put the cursor at the end for fields people append to.
- **Keyboard shortcuts visible** in menus and tooltips as `<kbd>` hints styled as subtle keycaps.
- **Delayed spinners** (~300ms) so fast responses don't flash.
- **Smooth number changes:** counters and totals can tween briefly (or just update; never jitter thanks to `tabular-nums`).

## 7. Content and copy details

- **Realistic data in every screenshot and mock:** real-sounding names of varied lengths and origins, plausible numbers, dates that make sense.
- **Smart truncation:** middle truncation for filenames (`quarterly-rep…final.pdf`), end truncation for titles, full text on hover/focus.
- **Pluralize correctly:** "1 item", "2 items", "No items". Never "1 item(s)". Use `Intl.PluralRules`.
- **Relative times with absolute on hover**; consistent date formats; time zones shown when ambiguous.
- **Specific empty states** that teach, instead of "No data".
- **Placeholder examples, not instructions:** `name@company.com`, not "Enter your email".
- **Consistent terminology:** pick "delete" or "remove", "workspace" or "team", and never mix them.

## 8. Images and media

- **Consistent aspect ratios** within a set (`aspect-ratio` + `object-fit: cover`), and focal points kept in frame (`object-position`).
- **Screenshot framing:** a subtle background, a consistent device or window frame (or none), consistent shadow and radius. Crop to the part that matters.
- **Placeholders while loading:** a dominant-color or blurred LQIP background, not an empty box that pops.
- **Avatars with fallbacks** (initials on a deterministic color), never broken-image icons.
- **SVG icons inherit `currentColor`** so they follow text and theme colors.

## 9. Browser and platform details

- **`color-scheme`** set so scrollbars, form controls, and system UI match the theme.
- **`theme-color` meta** matching the header background for mobile browser chrome.
- **Favicon** that works on light and dark tabs (SVG with a `prefers-color-scheme` media query inside, or a shape with its own background).
- **`scroll-margin-top`** on anchored headings so they aren't hidden under sticky headers.
- **`overscroll-behavior: contain`** on scrollable panels and modals, so scrolling inside them doesn't scroll the page.
- **`scrollbar-gutter: stable`** to prevent layout shift when content becomes scrollable (and when dialogs lock scrolling).
- **`-webkit-tap-highlight-color: transparent`** when you provide your own press states.
- **`touch-action: manipulation`** on controls to remove double-tap-zoom delay where needed.
- **`text-size-adjust: 100%`** to stop mobile Safari from inflating text in landscape.
- **Print styles** for content people print (invoices, articles, docs): hide navigation, show URLs for links, black text on white.

## 10. Dark mode details

- **Reduce the weight of large white text** slightly or use off-white. Light text on dark looks heavier than dark on light.
- **Images and illustrations** may need a dark variant or reduced brightness (`filter: brightness(0.9)`).
- **Borders over shadows** for separation; inner highlights for depth.
- **Desaturate accents** a little; saturated colors glow on dark.
- **Check every state again:** hover tints, focus rings, selected rows, disabled controls, and status badges all need their own dark values.
