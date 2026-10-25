# Interaction design

Visual design gets attention; interaction design determines whether the thing works. The craft is anticipating what a person is trying to do, what they expect to happen, and what they'll need when it doesn't go to plan.

## Contents
1. Principles that hold everywhere
2. Response time and perceived speed
3. The state inventory
4. Feedback
5. Loading
6. Errors: prevent, then explain
7. Forms
8. Destructive actions, undo, and confirmation
9. Navigation and wayfinding
10. Progressive disclosure and defaults
11. Keyboard and power users
12. Touch, pointer, and hover
13. Selection, bulk actions, drag and drop
14. Notifications and interruptions
15. Onboarding and empty states
16. Microcopy
17. Laws worth knowing

---

## 1. Principles that hold everywhere

- **Visibility of state.** People should always be able to tell what's going on: what's selected, what's saving, what failed, where they are.
- **Signifiers.** Things that can be acted on must look like it. Buttons look pressable, links look like links, draggable things have handles, editable fields look editable. Flat, borderless "is this clickable?" design pushes the burden onto users.
- **Feedback.** Every action gets an immediate, proportional response.
- **Mapping.** Controls relate to their effects spatially and conceptually. The control sits next to the thing it changes; up means more.
- **Constraints.** Make invalid actions impossible rather than erroring after the fact (a date picker that can't select past dates for a booking).
- **Consistency.** The same action works and looks the same everywhere, and platform conventions are followed (Jakob's law: people spend most of their time in *other* products).
- **Forgiveness.** Easy to undo, hard to do irreversible damage, and input is never lost.
- **Recognition over recall.** Show options rather than making people remember them: recent items, autocomplete, visible commands, examples in empty fields.

## 2. Response time and perceived speed

| Delay | Perception | What to do |
|---|---|---|
| < 100ms | instant | direct manipulation, hover and press states, toggles |
| 100ms–1s | noticeable, flow intact | subtle pending state; no spinner needed under ~300ms |
| 1–10s | waiting | show progress: skeletons, spinners, labels ("Saving…") |
| > 10s | attention lost | determinate progress, time estimate, let them leave and notify on completion |

Making it feel fast:
- **Optimistic UI:** apply the change immediately (toggle flips, item appears, message sends) and reconcile with the server in the background, rolling back with a clear message if it fails. Use it when success is very likely and the action is reversible.
- **Show content progressively:** render what you have and stream in the rest. Keep stale data visible while revalidating instead of blanking the screen.
- **Avoid spinner flashes:** delay showing a loading indicator by ~200–300ms, and once shown, keep it at least ~400–500ms so it doesn't flicker.
- **Prefetch** likely next steps on hover/intent; preload the next page of results.
- **Never block input while saving** if the save can happen in the background.

## 3. The state inventory

Most interfaces are designed only in their ideal state. Real use is mostly the other states. Design all of them.

**Every interactive element:**
| State | Notes |
|---|---|
| Default | looks interactive |
| Hover | subtle change (background, border, underline) on pointer devices; never the only signifier |
| Focus-visible | strong, unmistakable ring for keyboard users |
| Active / pressed | immediate response on press (darker, slightly inset) |
| Selected / checked / current | persistent, distinct from hover |
| Disabled | visibly inert; explain why if it's not obvious |
| Loading / pending | after activation, while waiting |
| Error / invalid | for inputs |

**Every view or data-driven component:**
| State | Notes |
|---|---|
| Ideal | realistic content, not the perfect demo |
| Empty (first use) | explain what goes here and offer the action to create the first item |
| Empty (no results) | say nothing matched, show the query, suggest a way out (clear filters, fix spelling) |
| Empty (cleared) | positive closure ("All caught up") |
| Loading | skeleton matching the final layout |
| Partial | some data loaded, some failed or pending |
| Error | what happened, whether data is safe, how to retry |
| Offline | what still works, what's queued |
| No permission | why, and who can grant access |
| Overflow | very long names, 10,000 items, huge numbers, many tags, narrow containers |

Test overflow on purpose: a username of 40 characters, a title in German, a price of $1,234,567.89, a list with one item and with 500.

## 4. Feedback

- **Proportional:** small actions get small feedback (a checkmark, a color change); big or risky actions get more (a confirmation message, a summary).
- **Local:** show feedback where the action happened. "Saved" next to the field beats a toast in the corner, which beats a banner at the top.
- **Button pending state:** after click, show a spinner or progress label *inside* the button, keep its width fixed (no layout jump), and prevent double submission. Restore it and show the outcome when done.
- **Success** often needs no message at all if the result is visible (the item appeared in the list). Add explicit confirmation when the result happens elsewhere ("Invite sent to sam@…").
- **Toasts** suit brief, non-critical confirmations of actions that happened off-screen, ideally with Undo. They're wrong for errors that need action, because they disappear. They're wrong for anything long, too.
- **Inline status for saves:** "Saving…" → "Saved" → (fade) near the content; "Couldn't save. Retry" if it fails, persisting until resolved.

## 5. Loading

- **Skeletons** for content-heavy layouts: they preview structure and prevent layout shift. Match the real layout's dimensions closely, keep them low-contrast, and use a subtle shimmer or pulse (1.5–2s cycle) or none.
- **Spinners** for small, indeterminate waits in a specific place (a button, a panel refresh). Not full-screen spinners for page loads if you can show the page frame.
- **Progress bars** when the duration is knowable (uploads, multi-step processes). Real progress beats fake progress, and fake progress that stalls at 99% destroys trust.
- **Keep the frame:** navigation, headers, and layout stay put while content loads. Swapping an entire screen for a spinner feels slow and disorienting.
- **Reserve space** for images (`width`/`height` or `aspect-ratio`), ads, embeds, and async components so content doesn't jump. Layout shift causes misclicks.

## 6. Errors: prevent, then explain

**Prevention first:**
- Constrain inputs (pickers, steppers, select lists for closed sets).
- **Be liberal in what you accept:** phone numbers with spaces or dashes, card numbers with spaces, emails with trailing whitespace, dates in several formats. Normalize them silently.
- Sensible defaults; inline hints before the error happens ("8+ characters").
- Disable impossible actions only when the reason is self-evident, otherwise allow the action and explain.

**When errors happen, a good message says:**
1. **What happened**, in plain language (no codes as the main message, no "An error occurred").
2. **Why**, if known and useful.
3. **How to fix it**, or what to do next.
4. Reassurance about data, when relevant ("Your draft is saved").

| Bad | Good |
|---|---|
| Invalid input | Enter a date in the future |
| Error 500 | We couldn't load your invoices. Try again, or check our status page if it keeps happening. |
| Password does not meet requirements | Password needs at least 8 characters (you have 6) |
| Upload failed | That file is 32 MB; the limit is 25 MB. Try compressing it. |

**Placement:**
- **Field errors** inline, directly below (or beside) the field, with an icon and text in the danger color, connected via `aria-describedby`.
- **Form-level summary** at the top for long forms after a failed submit, linking to each field, with focus moved to the summary or first invalid field.
- **Page or system errors** in the area that failed, with retry. Keep the rest of the page usable.
- **Never clear the user's input on error.** Re-typing a long form because one field was wrong is the fastest way to lose someone.
- Don't blame ("You entered an invalid…"). Don't joke in errors that cost people money or data.

## 7. Forms

Forms are where interfaces most often fail people. Good form design is mostly about removing work.

**Structure**
- **Ask for less.** Every field costs completion. Cut what you don't need, defer what you don't need yet, infer what you can (city from postcode, card type from number).
- **Single column.** Multi-column forms cause skipped fields and zig-zag reading, except for tightly related short pairs (first/last name, city/postcode, expiry/CVC).
- **Labels above fields** (fastest to scan, works on mobile, handles long labels). Left-aligned labels to the side only for dense, familiar admin forms.
- **Never use placeholder text as the label.** It disappears on typing, usually fails contrast, and looks like a pre-filled value. Placeholders are for format examples at most.
- **Group related fields** with headings or fieldsets; break long forms into logical steps with a progress indicator.
- **Size fields to their expected input:** a postcode field shouldn't be as wide as an address field. Width is a hint.
- **Mark the minority:** if most fields are required, mark optional ones "(optional)". If most are optional, mark the required ones. An asterisk alone needs explaining.

**Behavior**
- **Validate on blur** (when leaving a field), not on every keystroke; a field shouldn't turn red while someone is still typing their email. Once a field has shown an error, re-validate on input so the error clears as soon as it's fixed.
- **Keep the submit button enabled.** A disabled submit button with no explanation leaves people stuck guessing. Let them submit and show what's missing.
- **Use the right input types and attributes:** `type="email"`, `type="tel"`, `inputmode="numeric"` (for codes, not `type="number"`), `autocomplete` tokens (`email`, `given-name`, `street-address`, `one-time-code`, `new-password`, `cc-number`). Correct attributes enable autofill and the right mobile keyboard, which is the single biggest speed-up for forms.
- **Password fields:** a show/hide toggle; allow paste; state the rules up front; support password managers (`autocomplete="new-password"` or `"current-password"`).
- **Selection controls:** radios for 2–5 mutually exclusive options (all visible), a select or combobox for longer lists, checkboxes for independent choices, a toggle switch only for settings that take effect immediately.
- **Enter submits single-line forms.** Escape cancels in dialogs.
- **Autofocus** the first field only when filling the form is clearly the page's purpose (login, search), never on pages where it would scroll past content or open the mobile keyboard unexpectedly.
- **Preserve progress:** autosave long forms or warn before navigating away with unsaved changes.
- **Primary action at the end of the form,** aligned with the fields' left edge (or right, consistent with your system), labeled with the outcome ("Create account", "Pay $42.00").

## 8. Destructive actions, undo, and confirmation

- **Prefer undo to confirmation.** Confirmation dialogs get clicked through by habit; undo catches the actual mistake. Pattern: perform the action, show a toast "Project archived · Undo" for 5–10 seconds, actually delete later (soft delete).
- **Confirm only when the action is destructive and irreversible**, or costly (sends money, emails 10,000 people).
- **Write confirmations that can be answered without reading the question:** title states the consequence ("Delete 'Q3 report'?"), body says what will be lost ("This permanently deletes the report and its 14 comments."), and the button names the action ("Delete report") in the danger style. The cancel button is plain "Cancel". Never "Are you sure?" with "OK/Cancel" or "Yes/No".
- **For catastrophic actions** (delete an account, a production database), require typing the resource name.
- **Separate destructive controls spatially** from frequent ones (a "Danger zone" section, or the end of a menu after a divider) so they aren't hit by accident.
- Default focus in a destructive confirmation goes to the safe option.

## 9. Navigation and wayfinding

People should always be able to answer: Where am I? What's here? Where can I go? How do I get back?
- **Show location:** highlight the current nav item (not just on hover), use clear page titles matching the nav label, and breadcrumbs for deep hierarchies.
- **The URL is part of the interface:** tabs, filters, sort, search queries, pagination, and open dialogs worth sharing should be reflected in the URL, so Back works, refresh preserves state, and links can be shared.
- **The Back button must do what people expect.** Don't break it with client-side state that isn't in history, and don't add history entries for trivial changes.
- **Preserve scroll position and state** when returning to a list from a detail view.
- **Keep navigation stable:** items don't reorder, appear, or disappear based on context in ways that break muscle memory.
- **Name things by what users call them**, not internal jargon.
- **Links navigate; buttons act.** A link goes somewhere (has a URL, can open in a new tab); a button does something on this page. Don't style or code one as the other.
- **New tabs:** open external links in the same tab by default; use new tabs only when leaving would lose work, and indicate it.

## 10. Progressive disclosure and defaults

- **Show what most people need; reveal the rest on demand.** Advanced settings behind an "Advanced" disclosure, rarely used actions in an overflow menu, details on expand.
- **But don't hide the primary path.** Disclosure is for secondary complexity, not for core actions. Hiding key actions in a "⋯" menu or behind hover makes them undiscoverable.
- **Good defaults are the most powerful design decision.** Most people never change them. Default to the safest and most common choice, pre-fill what you know, and remember the user's last choice.
- **Choice overload (Hick's law):** more options mean slower decisions. Curate. Recommend one option when the choice is hard (the highlighted pricing tier).

## 11. Keyboard and power users

- **Everything works with the keyboard:** logical tab order following the visual order, visible focus, no keyboard traps.
- **Expected keys:** Enter activates/submits, Space toggles/activates buttons, Escape closes the topmost overlay, arrow keys move within composite widgets (menus, tabs, listboxes, grids, radio groups), Home/End jump to the extremes.
- **Focus management:** opening a dialog moves focus into it; closing returns focus to the trigger. After deleting an item, move focus to a sensible neighbor, not back to the top of the page.
- **Shortcuts for frequent actions** in productivity tools (single keys like `C` to create or `/` to search, or modifier combos). Make them discoverable: show them in tooltips and menus, and offer a `?` cheat sheet. Never hijack browser or OS shortcuts (Cmd+F, Cmd+L, Cmd+W).
- **Command palette** (Cmd/Ctrl+K) for apps with many actions: fuzzy search over commands, navigation, and recent items.

## 12. Touch, pointer, and hover

- **Hover doesn't exist on touch.** Anything revealed only on hover (row actions, tooltips with essential info, menus) must have a touch alternative. Use `@media (hover: hover)` for hover-only enhancements.
- **Target size:** at least 24×24px (WCAG 2.2 AA minimum), 44×44px recommended on touch. Small visual elements can have larger hit areas via padding or a pseudo-element.
- **Spacing between targets** prevents mis-taps; dense icon rows need gaps.
- **Thumb reach:** on phones, primary actions near the bottom; destructive actions away from the main thumb path.
- **Gestures need visible alternatives.** Swipe-to-delete needs a visible delete somewhere too; pinch-zoom needs buttons.
- **Hover intent:** menus that open on hover need a short open delay (~100–150ms), a longer close delay (~300ms), and a forgiving path to the submenu (the "safe triangle"). Click-to-open is usually better.
- **Tooltips:** for supplementary labels (icon buttons, truncated text), appear after ~400–700ms on hover and immediately on keyboard focus, and contain no interactive content and nothing essential.
- **Cursor:** `pointer` on clickable non-link elements is conventional on the web; keep it consistent. `not-allowed` for disabled.

## 13. Selection, bulk actions, drag and drop

- **Selection:** checkboxes appear on hover (pointer) or are always visible (touch, or when any item is selected). Shift-click selects ranges. A select-all in the header, with a "Select all 1,240 results" follow-up when paginated.
- **Bulk action bar** appears when items are selected, showing the count ("3 selected") and the available actions, with a way to clear the selection.
- **Drag and drop:** a visible grab handle (⋮⋮) when not obvious; lift the item on drag (shadow, slight scale); show a placeholder where it will land; auto-scroll near edges; animate the drop. Always provide a non-drag alternative (move up/down buttons, a "Move to…" menu) for keyboard and accessibility.

## 14. Notifications and interruptions

Attention is the scarcest resource. Spend it carefully.
- **Interruption ladder**, from least to most intrusive: inline indicator (badge, dot) → inline message → toast → banner → modal → OS notification/email. Use the lowest rung that will do the job.
- **Modals interrupt.** Use them for decisions that block progress or need focused input, not for marketing, tips, or announcements.
- **Banners** for persistent, page- or app-level conditions (trial ending, degraded service, unsaved changes), and they're dismissible unless critical.
- **Badges** for counts that need eventual attention; clear them when the user has seen the content.
- **No pop-ups on arrival** (newsletter modals, cookie walls bigger than needed, chat widgets that open themselves). They're the most hated pattern on the web.

## 15. Onboarding and empty states

- **Empty states are onboarding.** The first time someone sees a feature, its empty state should explain the value in a sentence, show what it will look like (illustration or preview), and offer the one action to begin ("Create your first project"). Sample data or templates help even more.
- **Learn by doing beats tours.** Multi-step coachmark tours get skipped and forgotten. Contextual hints at the moment of need work better.
- **Don't front-load setup.** Let people experience value before asking for profile details, invites, and preferences.
- **Checklists** ("3 of 5 steps done") work for products with genuine setup, and should be dismissible.

## 16. Microcopy

Words are interface. Most UI text is read in fragments, under pressure, mid-task.
- **Buttons are verbs plus objects:** "Save changes", "Create invoice", "Send 3 invites". Not "Submit", "OK", "Yes", or "Click here". A button label should make sense on its own.
- **Match the button to the heading:** a dialog titled "Delete project?" has a "Delete project" button.
- **Sentence case** for everything in UI: buttons, labels, headings, menu items. Title Case Feels Formal And Is Harder To Scan.
- **Be specific and brief:** "3 files uploaded" beats "Your upload was successful!" Remove "please", "simply", "just", "successfully", and exclamation marks.
- **Use the user's vocabulary**, not system internals ("Couldn't connect to the server" over "ECONNREFUSED"; "workspace" if that's what they call it).
- **Talk to the user as "you"** and write as a helpful person would speak. Consistent voice; tone shifts with the situation (lighter for success, plain and calm for errors).
- **Numbers and time:** relative times for recent events ("3 min ago") with the absolute time on hover; absolute dates for anything older than a week; locale-aware formatting; units always shown.
- **Labels describe the value, not the control:** "Email" not "Enter your email".
- **Truncation:** truncate with an ellipsis in the middle for file names and IDs where the end matters (`report-fin…-v3.pdf`), at the end otherwise, and show the full text on hover or focus.

## 17. Laws worth knowing

- **Fitts's law:** time to hit a target depends on its distance and size. Make frequent targets big and close; screen edges and corners are "infinitely" large for mouse users; put a popover's actions near where the pointer already is.
- **Hick's law:** decision time grows with the number of choices. Curate and group options.
- **Jakob's law:** users expect your product to work like the ones they already use. Innovate on value, not on basic conventions (logo links home, cart top-right, Cmd+K opens search in tools).
- **Miller's/chunking:** people handle information in chunks. Group long numbers (card numbers, phone numbers), break long lists into sections.
- **Doherty threshold:** productivity soars when the system responds in under ~400ms.
- **Tesler's law (conservation of complexity):** some complexity can't be removed, only moved. Move it to the system rather than the user.
- **Peak-end rule:** people judge an experience by its most intense moment and its end. Make the finish of a flow (confirmation, success state) feel good.
- **Postel's law:** be liberal in what you accept, conservative in what you send.
- **Aesthetic-usability effect:** people perceive attractive interfaces as easier to use, and forgive them more. Polish isn't superficial.
