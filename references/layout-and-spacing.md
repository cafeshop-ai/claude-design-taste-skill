# Layout, spacing, and surfaces

Spacing is the most underrated design tool. Most "this looks amateur" problems are spacing problems: inconsistent gaps, elements crammed against edges, groups that don't read as groups. Fix spacing and a design often improves more than any color or font change could.

## Contents
1. Spacing scale
2. Proximity and grouping
3. Padding inside components
4. Alignment
5. Grids and page structure
6. Widths and containers
7. Density
8. Responsive layout
9. Surfaces, depth, and elevation
10. Corner radius
11. Common layout patterns
12. Internationalization and right-to-left
13. Layout mistakes to catch

---

## 1. Spacing scale

Use a fixed scale based on 4px: **4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128**. Every margin, padding, and gap comes from it.

Why it matters: with a scale, choices become "one step more or less" instead of "13 or 14px?", and the consistency is visible as calm. The steps grow roughly geometrically because the difference between 4 and 8px is as noticeable as the difference between 48 and 96px.

Approximate roles:
| Range | Use |
|---|---|
| 2–4px | icon to its label, tightly coupled pieces |
| 8–12px | inside components (button padding), between a label and its field, list item gaps |
| 16–24px | card padding, gaps between related elements, between form fields |
| 32–48px | between groups or sections within a page |
| 64–128px | between major page sections on marketing and editorial pages |

When a value isn't on the scale, ask why. Usually the layout needs restructuring, not a 22px gap.

## 2. Proximity and grouping

The Gestalt principle of **proximity** is the core of layout: things close together are read as related.
- **The space inside a group must be clearly smaller than the space between groups.** If a label is 16px from its field and 16px from the previous field, the eye can't tell which field it belongs to. Use 6–8px label-to-field and 20–24px field-to-field.
- **A heading should be closer to its content than to the preceding section** (e.g., 48px above, 16px below).
- **Use the weakest grouping cue that works**, in this order: spacing, then alignment, then a subtle background change, then a divider line, and only then a bordered or shadowed box. Each step up adds visual noise. Many layouts drawn with cards and borders read better with just whitespace.
- **Similarity** groups too: elements that look alike (same color, shape, size) read as the same kind of thing. Make different kinds of things look different.
- **Common region**: a shared background or border groups strongly. That's why it's powerful, and why boxes inside boxes inside boxes become confusing.

## 3. Padding inside components

- **Buttons and inputs:** horizontal padding is typically 1.5–2.5× the vertical (e.g., 8px × 16px). Height comes from the control size scale (32/40/48px), and padding fills it.
- **Cards and panels:** 16–24px padding (12–16px in dense UIs, 32px+ for spacious marketing cards). Keep padding equal on all sides unless there's a reason.
- **Containers with text need more room than you think.** Text touching a border looks cramped. Text with ample padding looks deliberate.
- **Optical vs mathematical:** a button with an icon on the left often needs slightly less padding on the icon side to *look* balanced. A play triangle needs to shift right to look centered. Trust your eye after the math.

## 4. Alignment

- **Fewer alignment lines = calmer layout.** Every element that starts at a new x-position creates a new invisible line. Align content to a small set of edges.
- **Left-align by default.** Text, form labels, table text columns, and card content. Centered layouts are for short, symmetrical moments (hero, empty state, auth card, pricing headers).
- **Don't mix alignments in one group.** A centered heading over left-aligned paragraphs and a right-aligned button is three systems.
- **Align text baselines, not boxes,** when different text sizes sit on one line (`align-items: baseline` in flex). Centering a 24px heading and a 14px link vertically misaligns their baselines.
- **Icons beside text:** size the icon to the text's line height (16px icon with 14–16px text, 20px with 18–20px text) and center it on the first line, not on a multi-line block.
- **Numbers right-aligned** in tables; text left-aligned; headers aligned like their column's content.
- **Hang icons and bullets outside the text edge** in lists so the text edge stays clean.

## 5. Grids and page structure

- **Marketing and editorial pages:** a 12-column grid (divisible into halves, thirds, quarters) inside a max-width container, with 16–32px gutters. Content doesn't have to fill all columns; asymmetric spans (7/5, 8/4) are more interesting than 6/6 everywhere.
- **App layouts are regions, not columns:** a fixed sidebar (220–280px), a fluid main area, and an optional inspector (300–400px). Use CSS Grid with named areas.
- **Card grids:** `grid-template-columns: repeat(auto-fill, minmax(min(18rem, 100%), 1fr))` gives responsive columns without breakpoints.
- **Vertical rhythm:** keep consistent spacing between sections, e.g., one value for all major section gaps (`--space-section`), and one for gaps inside sections.
- **Vary section layouts on long pages.** A stack of identical "heading + 3 cards" sections is monotonous. Alternate text-and-image splits, a full-bleed visual, a single strong statement, a dense comparison table.
- **Break the grid deliberately**, rarely: an image bleeding to the edge, a pull quote hanging into the margin. Breaking it everywhere means there's no grid.

## 6. Widths and containers

Content stretched across a 1920px screen is unreadable and looks unfinished. Constrain it.
| Content | Max width |
|---|---|
| Body prose | ~65ch (about 600–720px at 16–18px) |
| Forms, auth, settings | 400–640px |
| Article with media | 720–800px text, images may go wider |
| App content | 1024–1280px, or fluid for data-heavy views (tables, boards) |
| Marketing page container | 1120–1280px |

- Side gutters scale with the viewport: `padding-inline: clamp(1rem, 4vw, 2rem)`.
- Full-bleed backgrounds can stretch edge to edge while their content stays constrained.
- Data-dense apps (tables, kanban, canvases) should use the full width. Constrained widths are for reading, not for working.

## 7. Density

Density is a product decision, not a style:
- **Comfortable** (consumer apps, marketing, infrequent tasks): 40–48px controls, 48–56px list rows, generous gaps. Easier to read and to tap.
- **Compact** (pro tools, admin, data, daily power use): 28–32px controls, 32–40px table rows, 13–14px text. More on screen, faster scanning for experts.
- Don't mix densities within one view. A spacious header above a cramped table looks like two products.
- For tools serving both audiences, offer a density toggle (`--density` in tokens.css scales control heights).
- Dense isn't cluttered. Dense UIs need *more* discipline: strict alignment, consistent row heights, minimal borders, clear typographic hierarchy.

## 8. Responsive layout

- **Design mobile-first in CSS** (base styles for small screens, `min-width` queries to enhance), but **design the content priority first**: decide what matters most, because on a phone it's the only thing visible.
- **Set breakpoints where the content breaks**, not at device widths. Common landmarks: ~640, 768, 1024, 1280px.
- **Use container queries for components** (`container-type: inline-size; @container (min-width: 30rem)`) so a card adapts to its column, not the viewport.
- **Reflow, don't shrink.** Rows become stacks; sidebars become drawers or bottom navigation; multi-column forms become single-column; secondary actions collapse into an overflow menu.
- **Tables on mobile:** let them scroll horizontally with a sticky first column, or reformat rows as stacked cards when each row is an "object". Never shrink text to make a table fit.
- **Touch:** targets ≥ 44×44px with ≥ 8px between them; primary actions within thumb reach (bottom of the screen on phones); nothing that only works on hover.
- **Viewport units:** `100dvh` instead of `100vh` (mobile browser bars), and `env(safe-area-inset-*)` padding for notches and home indicators on full-bleed layouts.
- **Test at 320–375px, ~768px, ~1280px, and 1440px+,** plus browser zoom at 200% (WCAG reflow).

## 9. Surfaces, depth, and elevation

Depth tells users what's on top of what. Use a small, consistent elevation system:
| Level | Examples | Treatment (light mode) |
|---|---|---|
| 0: canvas | page background | `--color-bg` |
| 1: surface | cards, panels, table containers | white surface + 1px border **or** `--shadow-xs/sm` |
| 2: raised | dropdowns, popovers, hover cards | `--shadow-md` + 1px border |
| 3: overlay | dialogs, sheets | `--shadow-xl`, plus a scrim behind |
| 4: transient | toasts | `--shadow-lg` |

Principles:
- **Pick one primary separation technique per level.** Border or shadow for resting cards, not both at full strength. (A hairline border plus a very soft shadow works well together because the shadow is barely there.)
- **Shadows should be soft, layered, and low-opacity:** a tight, slightly darker shadow for contact plus a large, faint one for ambient depth. Use one light source (from above), tinted with the neutral hue rather than pure black. A shadow you notice as a shadow is too strong.
- **Elevation should mean something.** Floating things are temporary or interactive (menus, dialogs, dragged items). A static card with a heavy shadow claims an importance it doesn't have.
- **Avoid nesting surfaces.** A card inside a card inside a panel creates a stack of borders and paddings that eats space and muddles hierarchy. Flatten: use spacing and headings inside a single surface.
- **In dark mode,** elevation comes from lighter surfaces and subtle borders; shadows mostly disappear. See color.md.
- **Hover elevation** (card lifts on hover) is only appropriate when the whole card is a single click target, and even then a background or border shift is usually more refined than a jump in shadow and scale.

## 10. Corner radius

Radius is a strong personality signal and must be consistent.
- **0–4px:** precise, serious, technical, editorial, Swiss.
- **6–10px:** neutral modern default.
- **12–20px:** soft, friendly, consumer, playful.
- **Pill (full):** for tags, badges, toggles, and sometimes buttons in friendly brands. Pill buttons beside 4px-radius inputs look mismatched.

Rules:
- **Scale radius with element size:** small elements (checkbox, badge) get a smaller radius, large containers (dialogs, cards) a larger one, all derived from one base (see tokens.css).
- **Concentric corners:** when a rounded element sits inside another with padding, inner radius = outer radius − padding. A 16px-radius card with 8px padding holds 8px-radius children. Equal radii on nested elements look pinched at the corners.
- **Images in cards** should share the card's radius at the outer corners (`overflow: hidden` on the card) and have none on the inner edges.

## 11. Common layout patterns

- **App shell:** sidebar nav (collapsible) + top bar (search, account) + main content. Use the sidebar for 5+ destinations, top tabs for 2–5.
- **List–detail (master–detail):** a list on the left, the selected item on the right; on mobile, they become two screens.
- **Settings:** a centered single column (~640px), grouped into titled sections, each section with a short description. Or a left section nav with content on the right for many sections.
- **Dashboard:** the most important metric(s) top-left, larger; supporting cards in a consistent grid; consistent card heights per row. Don't fill the page with equally sized widgets of equal emphasis.
- **Auth:** a small centered card or a split screen (form left, brand or visual right). Only the essentials; let password managers work.
- **Landing page:** see web-design.md.
- **Bento grid** (varied tile sizes): a strong pattern when the tiles contain real, varied content (screenshots, numbers, quotes). It's a cliché when every tile is an icon, a title, and a sentence.

## 12. Internationalization and right-to-left

Design so translation doesn't break layouts:
- **Text expands.** German, Finnish, and French run 20–35% longer than English (short labels can double); CJK is shorter but often needs larger sizes and more line height. Avoid fixed widths on buttons, tabs, and labels; let them grow and wrap.
- **Use logical properties:** `margin-inline-start`, `padding-inline`, `inset-inline-end`, `border-start-start-radius`, `text-align: start`. Layouts then mirror automatically for right-to-left languages with `dir="rtl"`.
- **Mirror direction-bound things in RTL:** layout order, back/forward arrows, progress direction, chevrons. Don't mirror logos, media playback controls, clocks, or numbers.
- **Never concatenate translated strings** ("You have " + n + " messages"). Use message formatting with plurals and gender (ICU MessageFormat, `Intl.PluralRules`).
- **Format with `Intl`:** numbers, currencies, dates, relative times, and lists differ by locale ("1,234.5" vs "1.234,5"; month/day order).
- **Fonts must cover the scripts** you ship (check glyph coverage; fall back to Noto families), and `lang` attributes let browsers pick correct glyphs and hyphenation.
- **Don't put text in images,** and avoid culturally specific icons and gestures (hand signs, mailboxes, checkmarks mean different things in places).

## 13. Layout mistakes to catch

- Inconsistent gaps between similar elements (16px here, 20px there).
- Equal spacing everywhere, so nothing groups.
- Text or icons touching container edges; buttons cramped inside cards.
- Everything centered, including paragraphs and form labels.
- Elements almost aligned (off by 2–4px). Either align exactly or offset clearly.
- Full-width text lines on large screens.
- Boxes within boxes; borders on every element.
- A sidebar or header that eats a third of a laptop screen.
- Sticky elements stacking up (sticky header + sticky sub-nav + cookie banner + chat widget) until little content remains on mobile.
- Layout shift: content jumping as images, fonts, or async data load. Reserve space with `aspect-ratio`, fixed skeleton dimensions, and font fallback metrics.
