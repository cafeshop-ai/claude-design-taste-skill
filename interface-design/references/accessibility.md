# Accessibility

Accessibility is a quality bar, not a separate feature. About one in six people worldwide lives with a significant disability (WHO), and everyone is situationally impaired sometimes: bright sunlight, a broken trackpad, a baby in one arm, a slow connection, aging eyes. The practices below make interfaces better for everyone, and most cost nothing if built in from the start.

Target **WCAG 2.2 level AA**. It's the common legal standard and a sensible quality floor.

## Contents
1. The essentials (do these always)
2. Semantic HTML first
3. Keyboard and focus
4. Color, contrast, and visual design
5. Text, zoom, and reflow
6. Images, icons, and media
7. Forms
8. Dynamic content
9. Component patterns
10. Motion and timing
11. Forced colors and user preferences
12. Testing
13. Snippets

---

## 1. The essentials (do these always)

- [ ] Native elements for their purpose: `<button>` for actions, `<a href>` for navigation, `<label>` for inputs, real headings, lists, and tables.
- [ ] Everything operable by keyboard, in a logical order, with a clearly visible focus indicator.
- [ ] Text contrast ≥ 4.5:1 (3:1 for large text); control boundaries, icons, and focus rings ≥ 3:1.
- [ ] Color never the only way information is conveyed.
- [ ] Every image has appropriate alt text (or `alt=""` if decorative); every icon-only button has an accessible name.
- [ ] Every form field has a visible, programmatically associated label; errors are described in text and linked to their field.
- [ ] The page works at 200% zoom and at 320px width without horizontal scrolling (except for things like data tables and maps).
- [ ] `<html lang>`, a descriptive `<title>`, one `<h1>`, headings in order, landmark elements.
- [ ] Respect `prefers-reduced-motion`; nothing flashes more than 3 times per second.
- [ ] Touch targets at least 24×24px (44×44 recommended).

## 2. Semantic HTML first

The first rule of ARIA: don't use ARIA if a native element does the job. Native elements come with keyboard behavior, focus, roles, and states for free.
- `<button>` not `<div onclick>`. A div needs `role="button"`, `tabindex="0"`, and Enter and Space handlers to approximate what a button does natively.
- `<a href>` for anything that navigates. Links without `href` aren't focusable.
- `<nav>`, `<main>`, `<header>`, `<footer>`, `<aside>`, `<section aria-labelledby>` give screen-reader users a map.
- Headings (`h1`–`h6`) form the outline people navigate by. Choose the level by structure and style it however you like; don't skip levels for visual size.
- `<ul>`/`<ol>` for lists (screen readers announce "list, 5 items"), `<table>` with `<th scope>` for tabular data (never for layout).
- `<dialog>`, `<details>/<summary>`, `[popover]`, `<input type="date">`, and `<select>` provide accessible behavior that's hard to replicate.

## 3. Keyboard and focus

- **Tab order follows visual order.** Don't use positive `tabindex`; fix the DOM order instead. `tabindex="0"` makes a custom element focusable; `tabindex="-1"` makes something focusable by script only.
- **Visible focus, always.** Use `:focus-visible` so mouse users don't see rings on click but keyboard users always do. 2px solid, ≥ 3:1 against adjacent colors, with an offset so it doesn't merge with the element's border. Never `outline: none` without a replacement.
- **Focus not obscured** (WCAG 2.2): sticky headers and footers must not cover the focused element; use `scroll-padding-top` equal to header height.
- **No keyboard traps,** except intentional, escapable ones (modal dialogs trap focus until closed with Escape).
- **Manage focus on context change:** move focus into opened dialogs, back to the trigger on close; to the new content's heading after client-side navigation; to a sensible place after deleting an item.
- **Skip link** as the first focusable element: "Skip to main content", visible on focus.
- **Composite widgets** (tabs, menus, listboxes, grids, radio groups, toolbars) use one tab stop and arrow keys inside (roving tabindex or `aria-activedescendant`).

## 4. Color, contrast, and visual design

- Contrast requirements and tooling: see color.md and `scripts/color.py contrast`.
- **Non-text contrast (1.4.11):** input borders, checkbox and radio outlines, toggle tracks, icon buttons without labels, focus indicators, and meaningful chart elements need 3:1 against adjacent colors.
- **Use of color (1.4.1):** links in body text need an underline (or another non-color cue); errors need an icon or text; required fields need a text marker; charts need labels or patterns.
- **Hover and focus content (1.4.13):** tooltips and popovers shown on hover must be dismissible (Escape), hoverable (pointer can move onto them), and persistent until dismissed.
- **Text over images** needs a scrim, overlay, or text shadow sufficient to guarantee contrast at every point.

## 5. Text, zoom, and reflow

- Size text in `rem`, never set a px font size on `html`, and don't disable zoom (`user-scalable=no` / `maximum-scale=1` are failures).
- **200% zoom** (1.4.4): no clipped or overlapping text, no lost functionality.
- **Reflow at 320 CSS px** (1.4.10): content works in a single column without horizontal scrolling.
- **Text spacing** (1.4.12): layouts survive users increasing line height to 1.5, paragraph spacing to 2×, letter spacing to 0.12em, and word spacing to 0.16em. Avoid fixed heights on text containers.
- Avoid text in images; avoid justified text; keep line lengths reasonable.

## 6. Images, icons, and media

- **Alt text** conveys the purpose in context. A product photo: what it shows. A chart: the takeaway ("Revenue grew 40% in Q3"), with the data available elsewhere. A linked image: the destination. Decorative: `alt=""`.
- **Icon-only buttons:** `aria-label="Close"` (or visually hidden text). Decorative icons next to text: `aria-hidden="true"`.
- **SVG icons:** `aria-hidden="true" focusable="false"` when decorative; `role="img"` with `<title>` when meaningful.
- **Video:** captions for speech, audio description or a transcript for important visual content, no autoplay with sound, and controls.
- **Animated GIFs and autoplaying video** need a way to pause.

## 7. Forms

- Every input has a `<label for>` (or wraps it). Placeholders are not labels.
- Group radios and checkboxes in `<fieldset>` with a `<legend>`.
- Helper text and errors are linked with `aria-describedby`; invalid fields get `aria-invalid="true"`.
- Required fields: the `required` attribute plus a visible text marker.
- On failed submit, move focus to an error summary (with links to fields) or the first invalid field.
- `autocomplete` attributes on personal data fields (1.3.5), which also enable autofill.
- **Accessible authentication** (3.3.8): don't block paste in password or code fields; support password managers; don't rely on cognitive tests (puzzles, memorization).
- **Redundant entry** (3.3.7): don't make people re-enter information they already provided in the same process.

## 8. Dynamic content

- **Live regions** announce changes that happen without focus moving: `role="status"` (polite: "Saved", "3 results") and `role="alert"` (assertive: errors that need immediate attention). The region must exist in the DOM before content is inserted into it.
- **Toasts** need a live region and enough time to read (or no timeout for important content); don't put the only copy of an action in a disappearing toast.
- **Loading:** `aria-busy="true"` on the region being updated; announce completion if it isn't obvious.
- **Client-side routing:** update `document.title`, move focus to the new page's `h1` (or announce the navigation).
- **Infinite scroll** traps keyboard users above the footer. Provide "Load more" or pagination.

## 9. Component patterns

Follow the WAI-ARIA Authoring Practices Guide (APG) for custom widgets. Key points:
- **Dialog:** native `<dialog>` + `showModal()`. Label it (`aria-labelledby` pointing to the title). Escape closes; focus returns to the trigger.
- **Disclosure/accordion:** `<details>/<summary>`, or a `<button aria-expanded aria-controls>` toggling a region.
- **Tabs:** `role="tablist"`, `role="tab"` with `aria-selected`, `role="tabpanel"`; arrow keys move between tabs.
- **Menu button:** `<button aria-haspopup="menu" aria-expanded>`. Use `role="menu"` only for application-style action menus, never for site navigation (use a list of links in `<nav>`).
- **Toggle button:** `<button aria-pressed="true|false">` for on/off tools (bold, mute); `role="switch"` with `aria-checked` for settings switches.
- **Combobox:** complex; use a well-tested library (or native `<select>` / `<datalist>` where acceptable).
- **Tooltip:** `aria-describedby` from the trigger to the tooltip; it supplements, never replaces, an accessible name.
- **Carousels:** pause control, previous/next buttons, no auto-advance (or pause on hover/focus), each slide reachable by keyboard. Usually a carousel is the wrong pattern; show the content.

## 10. Motion and timing

- `prefers-reduced-motion`: see motion.md.
- No content flashing more than 3 times per second.
- Auto-updating, moving, or scrolling content lasting more than 5 seconds needs pause/stop/hide.
- Time limits (session timeouts, timed quizzes) must be adjustable or extendable, with a warning before expiry.

## 11. Forced colors and user preferences

- **Windows High Contrast / forced colors** replaces your colors with a system palette and removes box-shadows and background images. Test with `@media (forced-colors: active)`.
  - Use real borders (even `1px solid transparent`) on buttons, cards, and inputs so they still have edges.
  - Focus indicators should use `outline` (survives) rather than `box-shadow` (removed).
  - SVG icons using `currentColor` adapt automatically.
- Respect `prefers-color-scheme`, `prefers-reduced-motion`, `prefers-contrast: more` (strengthen borders and text), and `prefers-reduced-transparency` (replace frosted-glass effects with solid surfaces).

## 12. Testing

Automated tools catch roughly a third of issues. Do all of these:
1. **Keyboard pass:** unplug the mouse. Tab through everything. Can you see focus at all times? Reach and operate everything? Escape every overlay? Is the order logical?
2. **Automated scan:** axe DevTools, Lighthouse, or WAVE; fix all errors.
3. **Zoom:** 200% browser zoom and a 320px-wide window.
4. **Screen reader spot check:** VoiceOver (macOS: Cmd+F5; iOS), NVDA (Windows, free), or TalkBack (Android). Navigate by headings and landmarks; operate a form; open a dialog. Does what you hear match what you see?
5. **Contrast check** of text and UI states, including hover, disabled, placeholder, and dark mode.
6. **Forced colors** emulation in Chrome DevTools (Rendering panel), plus color-vision-deficiency emulation.

## 13. Snippets

```html
<!-- Skip link: first element in <body> -->
<a class="skip-link" href="#main">Skip to main content</a>
...
<main id="main" tabindex="-1">…</main>
```

```css
.skip-link {
  position: absolute; left: var(--space-4); top: var(--space-4); z-index: var(--z-tooltip);
  padding: var(--space-2) var(--space-4); background: var(--color-surface); color: var(--color-text);
  border-radius: var(--radius-md); box-shadow: var(--shadow-md);
  translate: 0 -200%;
}
.skip-link:focus-visible { translate: 0 0; }

/* Text for screen readers only */
.sr-only { position: absolute !important; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip-path: inset(50%); white-space: nowrap; border: 0; }

/* Keep focused elements clear of a sticky header */
html { scroll-padding-top: 5rem; }

/* Strengthen boundaries when users ask for more contrast */
@media (prefers-contrast: more) {
  :root { --color-border: var(--color-border-control); --color-text-muted: var(--color-text); }
}

/* Make sure custom controls keep edges in forced colors */
@media (forced-colors: active) {
  .btn, .card, .input { border: 1px solid CanvasText; }
}
```

```html
<!-- Icon button with accessible name and tooltip -->
<button class="btn btn-ghost" aria-label="Archive" aria-describedby="tip-archive">
  <svg aria-hidden="true" focusable="false">…</svg>
</button>
<div role="tooltip" id="tip-archive">Archive (E)</div>

<!-- Field with hint and error -->
<div class="field">
  <label for="email">Work email</label>
  <input id="email" class="input" type="email" autocomplete="email" required
         aria-invalid="true" aria-describedby="email-hint email-error">
  <p class="hint" id="email-hint">We'll send the invite here.</p>
  <p class="error" id="email-error">Enter an email address like name@company.com</p>
</div>

<!-- Polite status region, present on page load -->
<div role="status" aria-live="polite" class="sr-only" id="status"></div>
```
