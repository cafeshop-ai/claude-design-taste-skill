# SVG illustration and animation

Small animated illustrations (empty states, loaders, success moments, onboarding spots) are where interfaces most often tip from charming into distracting. The craft is restraint: one idea, a few shapes, slow and small movement, a resting frame that works on its own, and silence for people who ask for less motion.

## Contents
1. Decide what the motion is for
2. Illustration style for UI
3. Choosing a technique
4. Timing, easing, and amplitude
5. Loops that don't nag
6. Transform origins and other SVG gotchas
7. Reduced motion and accessibility
8. Performance and file hygiene
9. A worked example

---

## 1. Decide what the motion is for

- **State the job in a phrase:** "confirm the sync finished", "show we're still searching", "make an empty list feel calm rather than broken". If you can't, the illustration may not need to move at all.
- **Ambient vs. event motion.** Event motion plays once in response to something (a check draws when the upload finishes). Ambient motion loops while the state persists (a gentle bob in an empty state). Many good pieces are both: a short entrance, then a very quiet idle.
- **Loaders and progress indicators are a third kind: the motion is the message.** They must read as "working" at a glance: continuous, clearly perceptible movement (a sweep, a travelling dot, elements rising and falling in sequence), cycles of 0.8–1.6s, no rest phase, running only while the wait lasts. The calm, mostly still loops described below are for ambient art, not loaders. Pair a loader with text ("Loading messages…") for anyone who can't see the motion, and under reduced motion keep a slow opacity pulse or the text rather than freezing into something that looks finished.
- **Near text, less.** Anything that moves in peripheral vision pulls the eye away from reading. Empty states and success screens can move a little; anything beside a form or a table should barely move, or not at all.

## 2. Illustration style for UI

- **Match the product's icon language:** the same stroke width (scaled), corner radius, and line caps as the interface's icons. An illustration in a different style looks pasted in.
- **Few shapes, one idea.** An envelope with a check, a cloud with an arrow, a magnifier over a page. Add a second element only if it carries meaning (a small sparkle for "done" is the most you need).
- **Limited palette:** neutrals from the UI plus the accent, perhaps one tint of it. Use `currentColor` or CSS variables so it adapts to dark mode.
- **Finish comes from soft, flat tints:** a pale fill inside the outline, a backdrop disc behind the subject, a flat ground-shadow ellipse that seats the object. Bare outlines on white look unfinished; gradients, glows, and drop shadows that fake 3D look dated. Keep strokes no heavier than the product's icons.
- **Size it to its context:** empty-state art is usually 96–200px wide. Design at that size; details that need a 400px canvas will be noise.
- **Compose a good still frame first.** The resting pose is what most people will see (and what reduced-motion users always see). Animate only once it works static.

## 3. Choosing a technique

| Technique | Use for | Notes |
|---|---|---|
| **CSS `@keyframes` inside the SVG's `<style>`** | Most UI animation | Runs when the SVG is used inline *or* as `<img src>`; animate `transform` and `opacity`; supports `prefers-reduced-motion` inside the file |
| **SMIL (`<animate>`, `<animateTransform>`)** | Path morphing, attribute animation CSS can't reach | Also runs in `<img>`; harder to disable for reduced motion; use sparingly |
| **JavaScript (Web Animations API, a library)** | Interactive or state-driven animation | Doesn't run in `<img>`; needs the SVG inline |
| **Lottie / video** | Complex character animation from a motion designer | Heavy; rarely right for a UI spot illustration |

Default to CSS keyframes in the file: it's portable, small, and easy to switch off.

## 4. Timing, easing, and amplitude

- **Entrances:** 300–600ms for a small illustration, ease-out (`cubic-bezier(0.22, 1, 0.36, 1)`). Stagger parts by 60–120ms so they arrive in reading order.
- **Stroke drawing:** 400–800ms. Set `pathLength="1"` on the path, then animate `stroke-dashoffset` from 1 to 0 with `stroke-dasharray: 1`, so the timing doesn't depend on path length.
- **Ambient loops:** slow. 3–8 seconds per cycle. Use ease-in-out (sine-like) and `animation-direction: alternate` for breathing and floating; linear only for continuous rotation.
- **Amplitude: small, but visible.** Floating 3–6px, rotation 3–8°, scale 0.96–1.04, opacity between 0.5 and 1 (at a 100–200px illustration size). Two failure modes: motion you can see from across the room is too much for an empty state; motion nobody notices within a few seconds of watching (under ~2px, ~2°, or a 2% scale) reads as a static image and wasn't worth the bytes. Check by comparing frames a second apart.
- **One mover at a time.** Animate one or two elements; let the rest stay still. Several elements moving on different cycles reads as busy and makes the loop feel random.
- **Overshoot sparingly:** a tiny overshoot (1.04 → 1) on a success check feels alive; bouncy springs on everything feel toy-like.

## 5. Loops that don't nag

- **Seamless:** keyframes end exactly where they start (or use `alternate`), so there's no jump at the loop point.
- **Rest in the cycle (ambient art):** hold still for part of each loop (`0%, 60% { transform: none } 80% { … } 100% { transform: none }`), so the motion is an occasional gesture rather than constant fidgeting.
- **Consider stopping (ambient art):** an entrance plus 2–3 idle cycles, then rest (`animation-iteration-count: 3`), is often better than infinite. Loaders are the opposite: they loop continuously until the wait ends.
- **No flashing:** nothing should flash more than three times per second, and avoid large high-contrast blinking anywhere.

## 6. Transform origins and other SVG gotchas

- **Rotation and scale happen around the SVG's origin (0,0) by default,** not the element's center, so a "gentle wobble" flings the shape across the canvas. Set `transform-box: fill-box; transform-origin: center;` (or an explicit point like `50% 100%` for a pendulum) on every animated element.
- **CSS transforms replace the `transform` attribute.** If a shape is positioned with `transform="translate(…)"`, animating CSS `transform` on it discards that positioning. Wrap it in a `<g>` that holds the position, and animate the inner element.
- **Keep the viewBox fixed** and leave room for the movement inside it, or motion gets clipped at the edges.
- **`stroke-linecap="round"` and `stroke-linejoin="round"`** for friendly line art; set `vector-effect="non-scaling-stroke"` only if the art is resized and the stroke must stay constant.

## 7. Reduced motion and accessibility

- **Always include** `@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }` in the SVG's style, and make sure the final, static frame is the complete composition (for example, set the drawn state as the default and animate *from* hidden in the keyframes, not the other way round).
- **Decorative art** (beside text that says the same thing): `aria-hidden="true"` when inline, `alt=""` as an image. **Meaningful art** (no text alternative nearby): `role="img"` and a `<title>`.
- **Never make the animation carry information alone.** The empty state still needs its sentence ("You're all set. New items will appear here.").

## 8. Performance and file hygiene

- Animate only `transform` and `opacity`; avoid animating filters, blur, masks, or path data on large areas.
- Few elements (often under 20), coordinates rounded to 1 decimal, no editor metadata, no embedded rasters. A spot animation should be a few kilobytes.
- A `viewBox`, no fixed pixel width/height (or both, matching the viewBox), so it scales with its container.

## 9. A worked example

A "sync complete" spot illustration: a cloud outline, a check that draws once, then the cloud breathes very slightly. One accent color, line art matching a 1.5px-stroke icon set at 24px (scaled to 4px at 96px).

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96" role="img" aria-labelledby="t">
  <title id="t">Everything is synced</title>
  <style>
    :root { --ink: #5b6472; --accent: #1f7a5a; --tint: #eef1f4; }
    @media (prefers-color-scheme: dark) { :root { --ink: #a3abb8; --accent: #5cc49a; --tint: #262b31; } }
    .ground { fill: var(--ink); opacity: 0.12; }
    .cloud { fill: var(--tint); stroke: var(--ink); stroke-width: 4; stroke-linejoin: round;
             transform-box: fill-box; transform-origin: 50% 100%;
             animation: breathe 6s ease-in-out 1s infinite; }
    .check { fill: none; stroke: var(--accent); stroke-width: 5; stroke-linecap: round; stroke-linejoin: round;
             stroke-dasharray: 1; animation: draw 600ms cubic-bezier(0.22, 1, 0.36, 1) 250ms both; }
    @keyframes draw { from { stroke-dashoffset: 1; } to { stroke-dashoffset: 0; } }
    /* Mostly still: a slow swell and settle, then a long rest. */
    @keyframes breathe { 0%, 55%, 100% { transform: none; } 75% { transform: scale(1.04); } }
    @media (prefers-reduced-motion: reduce) { * { animation: none !important; } }
  </style>
  <ellipse class="ground" cx="49" cy="76" rx="22" ry="2.5"/>
  <path class="cloud" d="M30 68H68A14 14 0 1 0 67.6 40A18 18 0 0 0 32 44.2A12 12 0 1 0 30 68Z"/>
  <path class="check" pathLength="1" d="M38 52l7 7 13-14"/>
</svg>
```

Why it works: one idea (the cloud means sync; the check means done), finished with a pale fill and a ground shadow rather than effects; the check's motion is the event, and the breathing is so slow and small it reads as calm rather than busy; the composition is complete when nothing moves; colors adapt to dark mode; it's under 1KB.
