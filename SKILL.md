---
name: interface-design
description: Opinionated craft guidance for web design, UI design, and interaction design. Covers visual hierarchy, typography, color and dark mode, spacing and layout, components, states, forms, motion, responsive behavior, accessibility, and design critique. Ships with a contrast/palette script, a type-scale script, and a starter design-token stylesheet. Use this skill whenever you build, restyle, or review anything people will look at or click (websites, landing pages, web apps, dashboards, settings screens, forms, components, HTML/CSS/Tailwind/React front-end work, prototypes, mockups), even if the user never says "design" (for example "build a signup page", "make this look more professional", "why does this feel off?", "add an empty state", "pick fonts for my blog"). Also use it for UX reviews, design systems and tokens, choosing palettes, and making something accessible.
---

# Interface Design

Good interfaces come from a small number of deliberate decisions applied with discipline, not from decoration. Most weak design isn't ugly so much as *undecided*: five grays where three would do, every element at the same volume, spacing picked per element instead of from a system, states nobody designed. This skill is about making those decisions on purpose, and making them well.

## The stance

- **How it works comes first, then how it looks.** A screen is a tool for someone to get something done. Start from the person and the job, and let the visuals express the hierarchy of that job.
- **Content first.** Design with real or realistic content. Lorem ipsum and "Feature One" hide every real problem: long names, empty lists, three-line titles, seven-digit numbers.
- **Restraint is the default; emphasis is earned.** If everything is bold, nothing is. Every extra color, weight, border, shadow, or animation must justify itself by communicating something.
- **Quiet almost everywhere, memorable somewhere.** Restraint alone produces competent, forgettable work. Spend boldness deliberately in one or two places (a confident headline, an ownable color, a beautifully made empty state, a delightful core interaction), and keep everything around it disciplined so it lands. "Clean and modern" is not a direction.
- **Systems over one-offs.** Choose scales (type, space, color, radius, motion) and use only values from them. Consistency is what makes plain things look designed.
- **Specific beats generic.** The generic version of anything (gradient hero, three emoji feature cards, "Unlock your potential") is invisible. Make choices particular to this product and audience.
- **The existing system wins.** Inside a product with an established design language (tokens, component library, Tailwind config, brand guide), follow it even where you'd choose differently; coherence beats personal taste. Point out problems; don't silently "fix" the system.

## Workflow

### 1. Understand before drawing
Work out, mostly by inference (ask only when the answer would materially change the design and you can't infer it):
- **Who** uses this, how often, on what device, in what state of mind? A daily-use admin tool wants density and speed; a once-a-year tax form wants guidance and reassurance.
- **What is the one primary job** of this screen, and what are the secondary ones?
- **What content** exists, how big can it get, and what does it look like empty?
- **What constraints** exist: codebase, component library, brand, framework?

In a codebase, look before you design: find the theme (tailwind.config, CSS custom properties, theme files), the existing components, and a couple of representative screens, then reuse them.

### 2. Choose a direction (new work only)
Decide the personality in one sentence ("a calm, precise tool for accountants"; "a warm, editorial magazine for home cooks"), then commit to the foundational decisions that follow from it:

1. Typeface(s): usually one family, at most two.
2. Neutral temperature: cool, warm, or pure gray.
3. One accent color, and what it means.
4. Corner radius and depth strategy (borders, shadows, or tonal surfaces).
5. Density and base text size.
6. Motion character: none, snappy, or soft.

`references/aesthetic-directions.md` has eight worked directions with these filled in. Start from one rather than the no-decision default (Inter everywhere, indigo accent, 12px radius, soft shadows, everything centered), which reads as "template" instantly. For substantial new work, tell the user the direction in a line or two so they can redirect early.

Encode the decisions as tokens. `assets/tokens.css` is a complete starter: change its DECISIONS block, and the palette, radii, and density follow.

### 3. Structure before style
Lay out hierarchy and grouping first: what matters most, what belongs together, what order people read in. Get it working in near-grayscale with real content. If the hierarchy doesn't read without color, color won't save it.

### 4. Apply the system
Fill in type, color, and surfaces from the tokens only. When you reach for an off-scale value, either the scale is missing a step (add it deliberately) or you're compensating for a structural problem (fix the structure).

### 5. Design every state
Default, hover, focus-visible, active, disabled, loading, empty, error, success, and overflow (long text, many items, huge numbers). Unhandled states are where interfaces feel broken. See `references/interaction.md`.

### 6. Look at it, then critique it
If you can render (browser tools, Playwright, screenshots), do it at ~375px, ~768px, and ~1440px wide, in dark mode if supported. This step is not optional polish. Rendering routinely catches what careful reading of the code misses: a selector silently overriding another's font size, grid children stretching to fill a row, colors clipping out of gamut and shifting hue, a fill that passes contrast in light mode and fails in dark, identifiers wrapping mid-word on a phone. Squint at it. Tab through it. Then run the checklist below, or the full method in `references/critique.md`, and fix the biggest problems first. When the structure is right, do a polish pass with `references/craft-details.md`.

## Core principles

### Hierarchy
- Each view has one primary focus and one primary action. Decide what they are before styling anything.
- Use the fewest levers: size, weight, color/contrast, position, space. Two together are usually enough.
- **De-emphasize to emphasize.** Make secondary things smaller, lighter, or muted before making the important thing bigger.
- Values often matter more than labels. In "Revenue: $48,210", the number is the content; the label can be small and muted.
- Squint test: blur your eyes. What pops out first should be what matters most.

### Spacing and layout
- A 4px-based scale (4, 8, 12, 16, 24, 32, 48, 64, 96, 128) for every gap, padding, and margin. No 13px or 22px.
- **Proximity encodes relationship:** space within a group must be clearly smaller than space between groups. A label sits closer to its own field than to the previous one.
- Start with more whitespace than feels necessary and remove it. Cramped is worse than airy for everything except expert data tools.
- Align to few edges. Left-align text by default; center only short standalone moments (hero headline, empty state, auth card).
- Constrain widths: prose at ~65ch, forms at 400–640px. Never let content stretch across a 1920px screen.
- Group with the weakest cue that works: space → alignment → background tint → divider → box. Boxes inside boxes are a smell.

### Typography
- One family is usually enough; two at most. Variety comes from size and weight.
- A type scale with distinct steps; most screens need 4–6 sizes. Body 16px on the web (14px is fine in dense apps).
- Leading ~1.5 for body, 1.1–1.25 for headings. Bigger type gets tighter leading and tighter tracking; uppercase labels get positive tracking.
- Two or three weights: 400 for text, 500–600 for labels and headings. App headings are smaller than you think.
- `tabular-nums` for numbers that align or change. `text-wrap: balance` on headings.

### Color
- Neutrals do ~90% of the work. One accent marks action, selection, and focus. Status colors appear only for status.
- Build ramps in OKLCH so steps are perceptually even; tint neutrals slightly. `scripts/color.py ramp` generates them.
- Components use role tokens (`--color-text-muted`, `--color-surface-raised`), never raw hex values or ramp steps.
- Contrast: text ≥ 4.5:1, large text and UI boundaries (input borders, icons, focus rings) ≥ 3:1. Verify with `scripts/color.py contrast`. Light-gray text is the most common failure in otherwise good design.
- Never rely on color alone. Pair it with text, icons, or shape.
- Dark mode is its own palette, not an inversion: dark gray canvas, lighter surfaces for elevation, softened accents, off-white text.

### Surfaces and depth
- Use one separation technique per level: a border *or* a shadow, not both at full strength.
- Shadows are soft, layered, low-opacity, and lit from one direction. If you clearly see a shadow, it's too strong.
- Elevation means something: floating things are temporary or interactive (menus, dialogs). Resting content stays flat.
- Nested radii are concentric: inner = outer − padding. Keep one radius logic across the product.

### Interaction
- Interactive things look interactive and respond within 100ms.
- Visible keyboard focus everywhere (`:focus-visible`, 2px ring, offset, ≥ 3:1). Never remove outlines without a replacement.
- Touch targets ≥ 44×44px; nothing essential hidden behind hover.
- Prefer undo to "Are you sure?". Confirm only irreversible, destructive actions, and name the action on the button ("Delete project").
- Feedback is immediate, proportional, and local to the action.
- Forms: labels above fields (never placeholder-as-label), validate on blur, keep submit enabled and explain what's missing, use correct `type` and `autocomplete`.
- Motion is functional and fast: 150–250ms for most UI, ease-out for entrances, quicker exits, and `prefers-reduced-motion` respected.

### Copy is design
- Buttons are verbs plus objects: "Save changes", "Send invite". Avoid "Submit", "Yes/No", and "Click here"; "OK" only for a plain acknowledgment.
- Sentence case for all UI text. Specific over grand: "3 files uploaded", not "Your upload was successful!"
- Errors say what happened and how to fix it, next to the problem, without blame.
- Never invent statistics, testimonials, or logos. Use clearly marked placeholders and tell the user.

## Generic tells to avoid

These signal that nothing was decided. Each needs a real reason to appear:
- Indigo/violet accents; purple-to-pink gradients; gradient text; glowing blurred blobs.
- Every section as centered heading + subtitle + three identical cards; emoji or icons-in-circles as decoration.
- A pill badge above every hero headline; "Unlock / Supercharge / Seamless / Revolutionize" copy; triplet slogans.
- The same large radius and soft shadow on everything; cards that scale up on hover; everything fading in on scroll.
- Low-contrast gray text, everything centered, uniform sizes with no hierarchy.

The fix is never more style. It's a specific choice: a typeface with character, a real product screenshot, a layout that follows the content, copy that says something only this product could say. `references/critique.md` has the full list, a symptom → cause table, and two worked before → after redesigns that show this judgment in action. Read them when you want calibration.

## Two short examples of deciding

**"Build a settings page for our project-management app"** (existing codebase with Tailwind and a component library). Read the existing theme and components and reuse them. Use a single centered column (~640px), with sections titled "Profile", "Notifications", and "Danger zone", each with a one-line description. Labels go above fields. Notification toggles take effect immediately (switches); profile fields have a Save button (no switches there). Delete workspace lives in the danger zone, opens a confirmation that requires typing the workspace name, and its button says "Delete workspace". Cover the states: saving, saved, validation errors, and a failed save with retry.

**"Make a landing page for a meal-planning app for busy parents"** (new, no brand). Direction: warm and human. Fraunces for headlines and Figtree for text; warm neutrals (`--neutral-h: 70`); a tomato/terracotta accent (`--accent-h: 35`, `--accent-c: 0.14`); 14px radius; comfortable density; soft, quick motion. The hero headline says the outcome plainly ("Dinner, decided. Every week, in five minutes."), with a real-looking plan screenshot rather than an abstract graphic. Sections vary: a split hero, a three-step "how it works" with app screenshots, a single large testimonial slot clearly marked as a placeholder for a real customer quote, pricing, FAQ. No gradients, no emoji icons.

## Pre-ship checklist

- [ ] One clear primary action per view; the squint test matches importance.
- [ ] Spacing, type sizes, colors, radii, and shadows all come from tokens/scales.
- [ ] Text ≥ 4.5:1, UI boundaries and focus ≥ 3:1, in every theme.
- [ ] Prose ≤ ~75ch; headings balanced; numbers tabular where they align.
- [ ] Hover, focus-visible, active, disabled, and loading states on interactive elements.
- [ ] Empty, loading, error, and overflow states designed with realistic content.
- [ ] Works at 375px with no horizontal scroll; targets ≥ 44px; nothing hover-only.
- [ ] Keyboard: logical order, visible focus, Escape closes overlays, focus returns.
- [ ] Semantic HTML: buttons act, links navigate, inputs have labels, headings in order.
- [ ] Motion purposeful and short; reduced-motion respected.
- [ ] Copy specific, sentence case, verb buttons, no invented claims.
- [ ] No generic tells left without a reason.

## Reference files

Read what the task needs; don't load everything.

| File | Read when |
|---|---|
| `references/aesthetic-directions.md` | starting new work; choosing a visual personality; font pairings by mood; adapting a brand |
| `references/typography.md` | choosing fonts, type scales, fluid type, font loading, text-heavy pages |
| `references/color.md` | building a palette, theming, dark mode, contrast problems, gradients |
| `references/layout-and-spacing.md` | page and screen layout, grids, widths, density, responsive behavior, surfaces and elevation, radius |
| `references/components.md` | specific components (buttons, inputs, tables, dialogs, nav, cards, menus, toasts, empty states), with CSS recipes |
| `references/interaction.md` | states, feedback, loading, errors, forms behavior, navigation, keyboard, touch, microcopy |
| `references/motion.md` | transitions and animation: durations, easing, choreography, CSS recipes |
| `references/web-design.md` | websites, landing pages, heroes, pricing, editorial and docs pages, web performance |
| `references/accessibility.md` | any production UI; WCAG 2.2 AA; ARIA patterns; testing |
| `references/critique.md` | reviewing a design or screenshot; "make it look better"; diagnosing what feels off; self-review; worked before → after examples |
| `references/craft-details.md` | the polish pass: the small type, color, edge, optical, and interaction details that separate good from great |
| `references/implementation.md` | putting tokens into Tailwind v4/v3, shadcn/ui, other component libraries, React components, or single-file HTML |
| `references/platforms.md` | native iOS/Android conventions, mobile web specifics, tablets |

## Bundled tools

- `assets/tokens.css`: a starter token stylesheet with OKLCH neutral and accent ramps generated from a hue and chroma, semantic color roles for light and dark (contrast-checked for every accent hue), type, space, size, radius, shadow, motion, and z-index scales, plus a small base reset. Copy it into the project and change the DECISIONS block. Shipping it unchanged everywhere would make everything look alike, which is the opposite of the point.
- `scripts/color.py`: `contrast FG BG` (WCAG 2 ratio + APCA Lc with verdicts), `ramp --hue H --chroma C` (a gamut-mapped 50–950 OKLCH ramp with text-contrast notes; `--format css`), and `convert COLOR` (hex ↔ oklch). Standard-library Python.
- `scripts/scale.py`: modular type scales with suggested line-heights and tracking; fluid `clamp()` values between two viewport widths (`--max-base`/`--max-ratio`); `--space --min --max` for one fluid value like section padding.

- `assets/specimen.html`: a living specimen of tokens.css (type scale, ramps, surfaces, buttons in every state, form fields, settings switches, stat cards, a table, alerts, a toast, an empty state) with live accent-hue, neutral-hue, radius, and theme controls. Open it beside tokens.css when tuning a direction; it doubles as a reference for what "done" looks like at the component level.

Run scripts with `python3 <this-skill-dir>/scripts/<name>.py --help`.

For charts, use a dedicated data-viz skill if one is available; `references/components.md` covers the basics otherwise.
