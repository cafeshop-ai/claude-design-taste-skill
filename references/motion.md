# Motion

Motion in interfaces is a functional tool. It explains what changed, where something came from or went, and that the system heard you. Used well, nobody notices it; things just feel responsive and solid. Used for decoration, it slows people down and makes products feel like templates.

## Contents
1. What motion is for
2. When not to animate
3. Duration
4. Easing
5. Choreography
6. Common patterns, with values
7. Performance
8. Reduced motion
9. Modern CSS tools
10. Code recipes

---

## 1. What motion is for

1. **Feedback:** confirm an action registered (button press, toggle, like).
2. **Orientation:** show where something came from and where it went (a menu growing from its trigger, a deleted row collapsing, a sheet sliding from the edge it lives on).
3. **Continuity:** connect two states so the change is understandable (a card expanding into a detail view; list items reordering).
4. **Attention:** draw the eye to something that changed outside the focus (a new notification arriving). Use sparingly.
5. **Character:** a small amount of personality in key moments (completing onboarding, a success state). The rarest use, and the one most often overdone.

If an animation doesn't do one of these, remove it.

## 2. When not to animate

- **Frequent, repeated actions.** Anything a person does dozens of times a day (opening a command palette, switching tabs, typing) should be instant or nearly so. Delight wears off on the second use; delay doesn't.
- **Keyboard-initiated actions** should feel more immediate than pointer ones.
- **Page load "reveals":** fading and sliding every section in as you scroll delays content, feels gimmicky, and breaks Ctrl+F, print, and screenshots. If you use scroll reveals at all, keep them subtle (short fade, small offset), trigger once, and only on a few hero elements.
- **Layout properties** (width, height, top, left, margin) cause jank. Animate transforms and opacity instead.
- **Anything that blocks input** while it plays.
- **Looping decoration** (pulsing CTAs, floating blobs, rotating gradients). It competes with content forever.

## 3. Duration

Motion should be fast enough that nobody waits for it, and slow enough to be perceived.
| Duration | Use |
|---|---|
| 0–100ms | color and opacity feedback on press, hover color changes |
| 100–200ms | small elements: tooltips, dropdowns, toggles, checkboxes, button states |
| 200–300ms | medium: dialogs, popovers with movement, accordions, tab indicators |
| 300–500ms | large or long-distance: sheets, full-screen transitions, page transitions |
| > 500ms | almost never in UI; reserved for deliberate storytelling moments |

- **Bigger elements and longer distances take longer**, smaller ones shorter.
- **Exits are faster than entrances** (~65–75% of the enter duration). People don't need to watch something leave.
- **Mobile can run slightly longer** than desktop because of physical distance on screen; wearables shorter.
- When in doubt, shorter. Most UI animation feels better at 150–250ms than at the 300–500ms people tend to default to.

## 4. Easing

Nothing in the physical world moves at constant speed. Easing makes movement feel natural.
| Curve | When | Value |
|---|---|---|
| Ease-out (decelerate) | elements **entering**, responding to user action; the default for most UI | `cubic-bezier(0.22, 1, 0.36, 1)` (quint) or `cubic-bezier(0.16, 1, 0.3, 1)` (expo, snappier) |
| Ease-in (accelerate) | elements **exiting** permanently | `cubic-bezier(0.32, 0, 0.67, 0)` |
| Ease-in-out | elements **moving** from one on-screen position to another; things that loop | `cubic-bezier(0.65, 0, 0.35, 1)` |
| Linear | only continuous motion: spinners, progress bars, marquee | `linear` |
| Spring | direct manipulation (drag release, swipe), playful products | JS spring libraries or CSS `linear()` approximations |

- Ease-out for entrances because a fast start makes the UI feel responsive, and the gentle stop feels controlled.
- The CSS keyword `ease` is a reasonable generic fallback; `ease-in` on entrances feels sluggish, and `linear` on movement feels mechanical.
- **Springs** suit gestures because they preserve the velocity of the user's flick and can be interrupted naturally. Keep bounce subtle (little or no overshoot) in productivity tools; more overshoot reads as playful.

## 5. Choreography

- **Origin-aware motion:** a popover or menu scales from its trigger (`transform-origin` at the anchor), a sheet slides in from its edge, a toast from the edge where toasts live. Motion should reinforce the spatial model.
- **Small distances:** entering elements move 4–16px, not 100px. Combine a small translate with a fade.
- **Subtle scale:** 0.95–0.98 → 1 for dialogs and popovers. Scaling from 0 looks cartoonish.
- **Stagger** lists by 20–40ms per item, capped so the whole sequence finishes within ~300ms (so stagger only the first ~6–8 items).
- **Things that move together move together:** related elements share timing and easing. Mixed timings look broken.
- **Interruptible:** if the user reverses an action mid-animation (closes the menu while it's opening), the motion should reverse from where it is. CSS transitions handle this naturally; keyframe animations don't.
- **Persistent elements stay put.** During a transition, navigation and headers should not animate along with the content.

## 6. Common patterns, with values

| Pattern | Motion |
|---|---|
| Button press | background color 75–100ms; optional 1px translateY or scale 0.98 |
| Hover | color/background 100–150ms ease-out; no layout change |
| Toggle switch | thumb slides 150–200ms ease-out; track color crossfades |
| Checkbox | checkmark draws or pops 150ms |
| Dropdown / popover | opacity 0→1, scale 0.96→1 (from trigger), translateY 4px→0, 150–200ms ease-out; exit 100–150ms |
| Tooltip | opacity, 100–150ms, after a ~500ms hover delay; no delay when moving between adjacent tooltips |
| Dialog | scrim fades 200ms; dialog opacity + scale 0.96→1, 200–250ms ease-out; exit 150ms ease-in |
| Sheet / drawer | translate from edge 100%→0, 250–350ms ease-out; exit 200ms ease-in |
| Toast | slide from edge 16px + fade, 200ms; exit fade + slide 150ms; others reflow smoothly |
| Accordion | height 0→auto 200–250ms ease-out (see recipes), chevron rotates in sync |
| Tab indicator | slides to the new tab 200–250ms ease-in-out |
| List item added / removed | fade + height expand / collapse 150–200ms, so neighbors move smoothly instead of jumping |
| Skeleton shimmer | 1.5–2s linear loop, very low contrast |
| Page transition | crossfade 150–250ms, or shared-element transition for continuity |

## 7. Performance

- **Animate `transform` and `opacity`** (and `filter`, sparingly). These run on the compositor without triggering layout or paint.
- **Avoid animating** `width`, `height`, `top`, `left`, `margin`, `padding`, `box-shadow` (animate a pseudo-element's opacity to fake a shadow change), and large `backdrop-filter` areas.
- **Don't use `transition: all`.** It animates properties you didn't intend (including layout ones) and makes changes unpredictable. List the properties.
- `will-change` only as a targeted fix for a measured problem, then remove it; overusing it wastes memory.
- Test on a mid-range phone, not just a fast laptop.

## 8. Reduced motion

Some people get dizzy, nauseous, or distracted from motion (vestibular disorders, migraine, ADHD). Respect `prefers-reduced-motion: reduce`:
- **Replace movement with fades** rather than removing all feedback. A dialog that fades in is fine; one that zooms and slides is not.
- **Remove** parallax, scroll-linked movement, auto-playing carousels and video, large zooms, and decorative loops.
- **Keep** essential feedback: color changes, focus rings, progress indication.
- A global safety net (as in `assets/tokens.css`) catches anything missed, but designing the reduced variant deliberately gives a better result.
- Auto-playing animation longer than 5 seconds needs a pause control (WCAG 2.2.2), regardless of the preference.

## 9. Modern CSS tools

- **`@starting-style`** defines the "from" state for elements entering the page or changing from `display: none`, enabling CSS-only entry animations for dialogs and popovers.
- **`transition-behavior: allow-discrete`** lets `display` and `overlay` participate in transitions, so exit animations work for `<dialog>` and `[popover]`.
- **View Transitions API** (`document.startViewTransition()`, and cross-document `@view-transition { navigation: auto; }`) animates between DOM states or pages, including shared-element morphs via `view-transition-name`.
- **Animating to `height: auto`:** `interpolate-size: allow-keywords` (Chromium) or the grid trick (`grid-template-rows: 0fr → 1fr`), which works everywhere.
- **Scroll-driven animations** (`animation-timeline: scroll()` / `view()`) for progress indicators and subtle effects without JS. Never hijack scroll speed or direction.
- **`linear()` easing** can approximate springs and bounces in pure CSS.

## 10. Code recipes

```css
/* Popover / dropdown that animates in and out, CSS only */
.menu {
  transform-origin: top left;              /* match the trigger side */
  transition: opacity var(--duration-base) var(--ease-out),
              scale var(--duration-base) var(--ease-out),
              translate var(--duration-base) var(--ease-out),
              display var(--duration-base) allow-discrete,
              overlay var(--duration-base) allow-discrete;
}
.menu:not(:popover-open) { opacity: 0; scale: 0.96; translate: 0 -4px; transition-duration: var(--duration-fast); transition-timing-function: var(--ease-in); }
@starting-style { .menu:popover-open { opacity: 0; scale: 0.96; translate: 0 -4px; } }

/* Dialog with scrim */
dialog {
  transition: opacity var(--duration-slow) var(--ease-out), scale var(--duration-slow) var(--ease-out),
              display var(--duration-slow) allow-discrete, overlay var(--duration-slow) allow-discrete;
}
dialog:not([open]) { opacity: 0; scale: 0.96; }
@starting-style { dialog[open] { opacity: 0; scale: 0.96; } }
dialog::backdrop { background: var(--color-overlay); transition: opacity var(--duration-base) var(--ease-out), display var(--duration-base) allow-discrete, overlay var(--duration-base) allow-discrete; }
dialog:not([open])::backdrop { opacity: 0; }
@starting-style { dialog[open]::backdrop { opacity: 0; } }

/* Accordion: animate height to auto with the grid trick */
.disclosure-panel { display: grid; grid-template-rows: 0fr; transition: grid-template-rows var(--duration-base) var(--ease-out); }
.disclosure-panel > div { overflow: hidden; }
.disclosure[aria-expanded="true"] + .disclosure-panel { grid-template-rows: 1fr; }

/* Reduced motion: keep the fade, drop the movement.
   (If you use the blanket safety net from tokens.css, it zeroes all transitions;
   narrow it to movement-heavy elements once components have variants like this.) */
@media (prefers-reduced-motion: reduce) {
  .menu, dialog { scale: 1 !important; translate: none !important; }
}
```
