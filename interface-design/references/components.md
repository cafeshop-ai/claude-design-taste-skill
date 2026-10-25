# Components

Specs, judgment calls, and pitfalls for the components that make up most interfaces. Numbers are dependable defaults; adapt them to the product's density and personality, but keep them consistent within it.

## Contents
1. Buttons
2. Links
3. Text inputs
4. Choice controls: checkbox, radio, switch, select, segmented control
5. Cards
6. Lists
7. Tables
8. Navigation: top bar, sidebar, tabs, breadcrumbs, pagination
9. Overlays: dialog, sheet, popover, tooltip
10. Menus and command palette
11. Feedback: toast, banner, inline alert
12. Badges, tags, chips
13. Avatars
14. Icons
15. Empty states
16. Loading indicators
17. Search
18. Charts in interfaces
19. Code recipes

---

## 1. Buttons

**Hierarchy.** Have a small, fixed set of variants and use them by rank of importance, not by taste:
| Variant | Use | Look |
|---|---|---|
| Primary | the one main action in a view or section | solid accent (or near-black) fill, contrasting text |
| Secondary | other real actions | neutral fill or 1px border, text color |
| Tertiary / ghost | low-emphasis actions, toolbars | no fill or border until hover |
| Destructive | irreversible actions, in confirmations | solid danger fill (or danger text for less emphasis) |
| Link-style | inline, navigational | text + underline on hover |

- **One primary per view** (or per clearly separate section). Two solid primary buttons side by side compete; make one secondary.
- **Pairs:** primary + secondary, ordered consistently. Common conventions: primary on the right in dialogs and wizards (Windows puts it left; pick one and stay consistent), primary first (left) in left-aligned page forms.
- **Size scale:** 32px (small/dense), 40px (default), 48px (large/marketing, mobile primary). Horizontal padding ~12/16/20px. Font 14–16px, weight 500–600.
- **Label:** verb + object, sentence case, 1–3 words ("Save changes"). Icons optional; leading icons for recognizable actions, trailing arrows for "continue/go".
- **Width:** natural width by default. Full-width on mobile forms and narrow cards. Set a minimum width (~80px) so "OK"-length labels don't look like stubs.
- **States:** hover (one step darker), active (two steps, or 1px translateY), focus-visible ring, disabled (muted, no hover), loading (spinner replacing or beside the label; width locked; `aria-busy`).
- **Icon-only buttons** need an accessible name (`aria-label`) and a tooltip, a square hit area matching control height, and should be reserved for universally understood icons (close, search, more, edit).
- **Don't** use buttons for navigation (use links styled as buttons only for CTAs that navigate), add shadows and gradients to make them "pop", make every button primary, or use ALL CAPS labels.

## 2. Links

- In body text: accent color + underline (offset ~0.2em, thin). Hover thickens the underline or darkens the color.
- In navigation and UI chrome: no underline is fine where context makes them obviously clickable (nav bars, card titles), but hover must respond.
- Visited styles help in content-heavy sites (docs, search results), and are unnecessary in apps.
- Link text describes the destination ("Read the pricing FAQ"), never "click here" or "learn more" alone. Screen-reader users often navigate by a list of links.
- External links can carry a small ↗ icon. Downloads should say the file type and size ("Annual report (PDF, 2.4 MB)").

## 3. Text inputs

**Anatomy:** label (above) → input → helper text or error (below). Optional: prefix/suffix (currency, units), leading icon (search), trailing action (clear, show password).
- **Height** matches buttons (40px default) so they align in rows. Padding ~12px horizontal. Text 16px on mobile (smaller text makes iOS zoom in on focus).
- **Border** must meet 3:1 against the background (`--color-border-control`). Background is the surface color or very slightly sunken.
- **Focus:** a clear ring or border color change to the accent. The focused field must be unmistakable.
- **Error:** danger-colored border + error text below with an icon. Don't rely on red alone.
- **Disabled:** sunken background, muted text, no focus. **Read-only:** looks like text, not like a disabled field, and stays selectable and copyable.
- **Label** 14px, medium weight, text color (not muted), 6–8px above the input. Helper text 13–14px, muted, 6px below.
- **Textareas:** at least 3–4 lines tall to signal "write more here"; auto-grow (`field-sizing: content`) where supported; show a character count only near a limit.
- **Search fields:** leading magnifier icon, a clear (×) button once there's text, and keyboard shortcut hint (`/` or ⌘K) on desktop.

## 4. Choice controls

- **Checkbox:** independent on/off choices or multi-select. 16–20px box with a radius of 3–4px, label clickable, 8px gap. Indeterminate state for "some children selected".
- **Radio group:** 2–5 mutually exclusive options, all visible, stacked vertically (horizontal only for 2–3 short options). One option preselected when a sensible default exists.
- **Switch/toggle:** settings that take effect immediately (no save button). The label states what's on ("Email notifications"), not the switch state. If a form needs a Save, use a checkbox instead.
- **Select (native):** 6+ options, or a known list (countries). Native selects are accessible and mobile-friendly; style the closed state and leave the open menu native unless you need richer options.
- **Combobox/autocomplete:** long lists (50+) or open-ended entries; type to filter, arrow keys to move, Enter to choose.
- **Segmented control:** 2–5 options that switch a view or mode (Day/Week/Month, List/Grid). Acts immediately. Not for form data entry.
- **Large selectable cards** (plan pickers, choosing a template) are radio groups in disguise: the whole card is clickable, the selected state is unmistakable (accent border + check), and they're built on real radio inputs for accessibility.

## 5. Cards

A card says "this is one self-contained object". Use cards for collections of discrete, comparable items (projects, products, articles), not as the default container for every block of content.
- **Padding** 16–24px; consistent across a collection.
- **Separation:** 1px border or a very soft shadow, rarely both strongly. On a tinted page background, a white card with no border can be enough.
- **Hierarchy inside:** one clear title, supporting metadata muted, at most one or two actions. Media (if any) on top, full-bleed to the card edge.
- **Clickable cards:** make the whole card the target (stretched link on the title via a pseudo-element), with a hover state (border or background shift) and visible focus. Avoid nesting other interactive elements inside, or handle them carefully.
- **Equal heights in a row**; align internal elements (titles, prices, buttons) across cards with grid/subgrid or flex column + `margin-top: auto` on the footer.
- **Don't** nest cards, put every section of a page in a card, or put icon-in-a-colored-circle on every card as decoration.

## 6. Lists

- **Row anatomy:** leading element (avatar, icon, checkbox) → primary text + secondary text → trailing metadata or action.
- **Row height:** 40–48px single-line, 56–72px two-line; consistent within a list.
- **Dividers:** hairlines between rows *or* spacing, not both. Inset dividers (starting at the text, not the avatar) feel lighter.
- **Hover** background on interactive rows; row actions revealed on hover for pointer, always present (or behind a ⋯ menu) for touch.
- **Long lists:** group with sticky section headers (by date, letter, status); virtualize when thousands of rows.

## 7. Tables

Tables are for comparing values across rows. Design for scanning.
- **Alignment:** text left, numbers right (with tabular figures), dates consistently; header aligned with its column's content.
- **Minimal lines:** horizontal row dividers only (or zebra striping for wide, dense tables). Vertical gridlines rarely help. Remove the outer border if the table sits in a card.
- **Header:** smaller (12–13px), medium weight, muted color, maybe uppercase with tracking; sticky on scroll for long tables.
- **Row height:** 36–40px compact, 48–52px comfortable. Cell padding 12–16px horizontal.
- **Hover** row highlight for interactive rows; selected rows tinted with `--color-accent-subtle`.
- **Sortable columns:** clickable headers with a sort direction arrow on the active column (and a faint one on hover).
- **Truncate** long text with an ellipsis and a tooltip, or wrap to two lines max. Keep key identifiers fully visible.
- **First column** is usually the identifier: make it the strongest (primary text color, perhaps a link) and sticky on horizontal scroll.
- **Empty values:** use an em dash (—) or "None", not blank cells that look broken.
- **Numbers:** consistent decimals, units in the header ("Revenue (USD)") rather than every cell, negative values with a minus sign (and color as secondary signal).
- **Pagination vs infinite scroll:** paginate when users need to find their place or reference positions; load more/infinite for feeds. Show the total count.
- **Mobile:** for object-like rows (orders, tickets, people), reflow each row into a stacked card that shows the 2–4 fields people scan for (name, status, date, total), with the rest a tap away. Horizontal scroll suits truly tabular data (comparisons, spreadsheets) and needs a sticky first column, so you never lose track of which row you're on. Scroll wrappers need `overflow-x: auto` *and* `position: relative`: without a positioned wrapper, absolutely positioned descendants (including `.sr-only` labels in header cells) escape it and widen the whole page on phones.

## 8. Navigation

**Top bar (site header):** logo left (links home), 3–7 primary links, a single CTA right (sign up, contact), account/search on the right in apps. Height 56–72px; compact on scroll if sticky. Collapses to a menu button on mobile with the CTA kept visible.

**Sidebar (app):** 220–280px, collapsible to icons (~56–64px) on smaller screens. Group items under small muted section labels. Current item: accent-subtle background + accent or text-color label + maybe a left indicator; hover: neutral tint. Icons + labels (icons alone only in the collapsed state, with tooltips). Keep it to what users navigate to often; settings and account at the bottom.

**Tabs:** switch between views of the same object or context, 2–7 tabs. The active tab is clearly marked (underline indicator 2px in accent, or a filled segment), inactive tabs muted but legible. Tabs don't trigger actions or navigate to different contexts. Overflowing tabs scroll horizontally with fade edges or collapse into a "More" menu. Reflect the active tab in the URL.

**Breadcrumbs:** for hierarchies 3+ levels deep. Muted links separated by `/` or `›`, current page last and not a link. Truncate the middle on mobile.

**Pagination:** previous/next plus a few page numbers with ellipses ("1 … 4 5 6 … 20"). Show "Showing 41–60 of 1,240". Keep controls in the same place on every page.

## 9. Overlays

**Dialog (modal):** for focused tasks and decisions that block progress (confirm a destructive action, a short form that must be completed in context).
- Width ~400–560px (confirmations narrower, forms wider); max height with internal scroll on the body, header and footer fixed.
- Anatomy: title (states the task or question), body, footer actions (primary on the right by convention, or matching your system), close button top-right.
- Closes on Escape, close button, and (for non-destructive dialogs) clicking the scrim. Traps focus inside; returns focus to the trigger on close. Use the native `<dialog>` element with `showModal()`, which handles focus containment, Escape, and inertness of the page behind.
- Scrim at ~40–60% dark overlay; dialog enters with a short fade + slight scale (0.96 → 1).
- Don't stack dialogs, open them on page load, or use them for content that deserves a page (long forms, multi-step flows).

**Sheet / drawer:** slides from the edge, for secondary tasks while keeping context (filters, editing a record from a list, details). Right side on desktop (360–480px), bottom on mobile. Non-modal variants let you interact with the page behind.

**Popover:** small, anchored, non-blocking panel for contextual content and light interaction (date picker, color picker, share options). Anchored to its trigger, closes on outside click or Escape, positions itself to stay in the viewport. The native `popover` attribute and CSS anchor positioning help.

**Tooltip:** a short text label (a few words) for icon buttons, truncated text, or definitions. Delay ~500ms on hover, immediate on focus, no interactive content, never essential information, not reachable on touch. Dark background in light mode is conventional; keep max width ~240px.

## 10. Menus and command palette

- **Dropdown menu:** a list of actions. Items 32–36px high, 8–12px padding, optional leading icons (all or none in a group), keyboard shortcuts right-aligned and muted. Group with dividers; destructive items last, in danger color. Opens below the trigger (flips when constrained), arrow keys navigate, type-ahead jumps, Escape closes.
- **The ⋯ overflow menu** holds secondary actions. Don't hide the primary action of an object in it.
- **Context menus** (right-click) duplicate actions available elsewhere; never make them the only way.
- **Command palette (⌘K):** a centered overlay with a search input and grouped results (navigation, actions, recent). Fuzzy matching, keyboard-first, shows shortcuts next to commands. Great for power users in tools with many actions.

## 11. Feedback: toast, banner, inline alert

- **Toast:** brief confirmation of something that happened ("Message sent · Undo"). An inverse surface (`--color-surface-inverse`) makes it stand apart from the page in both themes. Bottom center or bottom right (top on mobile is common too); 4–6 seconds (longer if it has an action); pauses on hover; dismissible; stacks with a limit of ~3; announced to screen readers via a live region. Never for errors that need action or info people must read.
- **Banner:** page or app-level persistent message (system status, billing problem, trial ending). Full-width at the top of the relevant area, status color subtle background + icon + one sentence + optional action. Dismissible unless critical.
- **Inline alert/callout:** contextual message within content ("This setting affects all workspaces"). Subtle status background, icon, short text. Use sparingly; a page full of callouts teaches people to ignore them.

## 12. Badges, tags, chips

- **Badge:** a status or count label. Small (20–24px tall, 12px text, medium weight), subtle status background with darker text in the same hue. Use a consistent mapping (green = active/success, amber = pending/warning, red = failed/error, gray = draft/inactive, blue = info/new).
- **Count badge:** small dot or number on an icon; "99+" for overflow.
- **Tag/chip:** user-applied labels or filter tokens; removable chips have an × with its own hit area and accessible label.
- Don't put badges everywhere. Five colored badges on one row is noise; reserve color for states that matter.

## 13. Avatars

- Circle for people, rounded square for organizations/workspaces (a useful distinction).
- Sizes on a scale: 20/24 (inline), 32 (lists), 40 (comments), 64–96 (profiles).
- Fallback: initials on a color derived consistently from the name (deterministic hash to a small palette with good contrast), not a generic silhouette.
- Groups: overlapping stack with a 2px ring in the surface color, max ~3–5 then "+12".

## 14. Icons

- **One icon set**, one style (outline or filled, matching stroke width). Mixing sets is instantly visible. Good sets: Lucide, Phosphor, Heroicons, Tabler, Material Symbols, SF Symbols (Apple platforms).
- **Size to text:** 16px with 14px text, 20px with 16–18px text; stroke weight to match the font weight (1.5–2px strokes at 24px).
- **Color:** icons inherit text color (`currentColor`); muted icons beside primary text; accent only when interactive or selected.
- **Labels:** icons alone are ambiguous except for a handful of universal ones (search, close, menu, home, settings, trash, plus). Pair icons with text in navigation and primary actions.
- **Don't decorate with icons.** An icon beside every heading, list item, and card title adds noise, not meaning. Emoji as UI icons look unprofessional in most products.

## 15. Empty states

- **Anatomy:** a simple illustration or icon (optional, small and muted), a headline that says what goes here or what happened, one sentence of explanation, and a primary action.
- **First use:** "No projects yet" → "Projects keep your team's files and tasks together." → [Create project]. Offer templates or sample data where possible.
- **No results:** "No results for 'invioce'" → "Check the spelling or try a broader term." → [Clear filters]. Show the active filters.
- **Cleared:** "You're all caught up." Positive, quiet, no action needed.
- **Errors** are not empty states. "No data" when the request failed is a lie that makes people think their data is gone.
- Center empty states in the area they replace, at a reasonable size; don't fill a small panel with a giant illustration.

## 16. Loading indicators

- **Skeleton:** gray blocks matching the final layout (text lines at the right widths, avatar circles, image boxes), low contrast, subtle shimmer or none. Use for initial content loads.
- **Spinner:** small, in context (inside the button, in the panel being refreshed). 16–24px, inheriting color. Delay ~300ms before showing.
- **Progress bar:** determinate for uploads and multi-step jobs; a thin indeterminate top bar for page transitions.
- **Inline text:** "Saving…" "Loading 3 of 12…" Words are often the clearest indicator.

## 17. Search

- Prominent in content-heavy products; `/` or ⌘K to focus on desktop.
- Instant results as you type (debounced ~150–300ms) when cheap; otherwise submit on Enter.
- Results highlight matching text, show enough context to choose, and group by type if mixed.
- Recent searches and suggestions when empty; a helpful no-results state.
- Keep the query in the input and the URL on the results page.

## 18. Charts in interfaces

If a dedicated data-visualization skill is available, use it. Otherwise these basics cover most product charts:
- **Pick the chart by the question:** change over time → line (or bars for few periods); comparison across categories → horizontal bars, sorted; part of a whole → a single stacked bar or simply a table (pie charts only for 2–3 parts); distribution → histogram; relationship → scatter. When in doubt, a well-formatted table or a single big number with a comparison beats a chart.
- **Start bar axes at zero.** Line charts may zoom in on the range, but label it.
- **Direct labels over legends:** label lines at their ends and bars at their tips; a legend forces back-and-forth reading.
- **Quiet the scaffolding:** light gridlines (horizontal only), no chart borders, muted axis text at 12px, few ticks with round numbers, abbreviated units ($1.2M).
- **Color with intent:** one emphasis color for the series that matters and neutral grays for context; status colors only when the data is about status. Categorical palettes should have similar lightness and stay distinguishable for color-blind users (vary lightness too, or label directly).
- **Titles state the takeaway** ("Signups doubled after the March launch"), with the metric and period as a subtitle.
- **Interaction:** a hover/focus tooltip with exact values, a crosshair for time series, keyboard access to data points where feasible, and a data table alternative for screen readers.
- **Sparklines** in tables and stat cards add trend context cheaply: no axes, a single muted line, the last point marked.
- **Dashboards:** lead with the 3–5 numbers that matter, each with a comparison (vs. last period or target); details below. Consistent card sizes and time ranges across a dashboard.

## 19. Code recipes

These use the semantic tokens from `assets/tokens.css`. They show complete state coverage; restyle freely.

```css
/* Button */
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: var(--space-2);
  height: var(--control-md); padding-inline: var(--space-4); min-width: 5rem;
  border: 1px solid transparent; border-radius: var(--radius-md);
  font-size: var(--text-sm); font-weight: var(--weight-medium); line-height: 1;
  white-space: nowrap; user-select: none;
  transition: background-color var(--duration-fast) var(--ease-out),
              border-color var(--duration-fast) var(--ease-out),
              color var(--duration-fast) var(--ease-out);
}
.btn:active:not(:disabled) { translate: 0 1px; }
.btn:disabled { opacity: 0.5; }       /* acceptable for buttons with clear labels; see color.md */

.btn-primary { background: var(--color-accent); color: var(--color-accent-contrast); }
.btn-primary:hover:not(:disabled)  { background: var(--color-accent-hover); }
.btn-primary:active:not(:disabled) { background: var(--color-accent-active); }

.btn-secondary { background: var(--color-surface); color: var(--color-text); border-color: var(--color-border-strong); box-shadow: var(--shadow-xs); }
.btn-secondary:hover:not(:disabled) { background: var(--color-surface-sunken); }

.btn-ghost { background: transparent; color: var(--color-text-muted); }
.btn-ghost:hover:not(:disabled) { background: var(--color-surface-hover); color: var(--color-text); }

.btn-danger { background: var(--color-danger-solid); color: var(--neutral-0); }

.btn[aria-busy="true"] { color: transparent; position: relative; pointer-events: none; }
.btn[aria-busy="true"]::after {
  content: ""; position: absolute; width: 1em; height: 1em; border-radius: 50%;
  border: 2px solid var(--color-accent-contrast); border-right-color: transparent;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { rotate: 1turn; } }

/* Field */
.field { display: grid; gap: var(--space-1-5); }
.field label { font-size: var(--text-sm); font-weight: var(--weight-medium); color: var(--color-text); }
.field .hint { font-size: var(--text-sm); color: var(--color-text-muted); }
.field .error { font-size: var(--text-sm); color: var(--color-danger); display: flex; gap: var(--space-1-5); }

.input {
  height: var(--control-md); padding-inline: var(--space-3); width: 100%;
  background: var(--color-surface); color: var(--color-text);
  border: 1px solid var(--color-border-control); border-radius: var(--radius-md);
  transition: border-color var(--duration-fast) var(--ease-out), box-shadow var(--duration-fast) var(--ease-out);
}
.input::placeholder { color: var(--color-text-subtle); }
.input:hover:not(:disabled) { border-color: var(--color-text-subtle); }
.input:focus-visible { outline: 2px solid transparent; border-color: var(--color-focus); box-shadow: 0 0 0 3px color-mix(in oklch, var(--color-focus) 25%, transparent); }
.input[aria-invalid="true"] { border-color: var(--color-danger); }
.input:disabled { background: var(--color-surface-sunken); color: var(--color-text-disabled); }
@media (pointer: coarse) { .input { font-size: max(16px, 1rem); } } /* prevents iOS zoom on focus */

/* Card */
.card {
  background: var(--color-surface); border: 1px solid var(--color-border);
  border-radius: var(--radius-lg); padding: var(--space-6);
}
.card > img:first-child { margin: calc(var(--space-6) * -1) calc(var(--space-6) * -1) var(--space-4); max-width: none; width: calc(100% + 2 * var(--space-6)); border-radius: var(--radius-lg) var(--radius-lg) 0 0; }
```

Note the input's focus style: it replaces the global outline with an accent border plus a soft ring. The border change alone carries the 3:1 focus contrast. The `outline: 2px solid transparent` is deliberate: it's invisible normally, but Windows forced-colors mode (which strips box-shadows and recolors borders) paints it in a visible system color, so keyboard focus never disappears. Never use `outline: none` without that fallback.
