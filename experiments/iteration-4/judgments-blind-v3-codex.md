# Blind judgments: iteration-4 (blind-v3), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-3/with-skill**: 5
- **iteration-4/with-skill**: 9

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-3/with-skill | 4.00 | 3.50 | 3.70 | 3.17 | 3.30 | 4.00 | 3.90 | 4.00 | 3.50 | 4.00 | 4.00 | 3.50 | 3.70 | 2.00 |
| iteration-4/with-skill | 4.00 | 4.00 | 3.90 | 3.92 | 3.50 | 4.00 | 3.90 | 4.00 | 3.00 | 4.50 | 3.50 | 3.50 | 3.80 | 2.00 |

## Pairs

### booking-flow-run-1

X = `iteration-3/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 3 | 2 | 3 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y combines progress and form into a coherent card, adapting its desktop sidebar into a compact phone stepper. X’s phone action row overlaps the phone-number field, leaves excessive empty space beneath it, and pushes a large placeholder summary farther down the page. Both have clear typography and restrained green palettes, but Y’s tighter layout and useful phone-number helper make it more polished and focused.

### booking-flow-run-2

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X presents a more focused booking experience, with the contact form and Continue button fitting comfortably within the supplied phone view. Y has more character through its bold serif headline and living-room illustration, but the mostly empty booking summary adds substantial mobile length with little immediate value. X’s required-fields instruction and next-step preview are more useful here than Y’s demo disclaimer and repeated unselected states.

### invoice-dashboard-run-1

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 2 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X wins through its phone layout: each invoice retains the client, amount, status, and due date in a readable stacked arrangement. Y keeps a wide table on mobile, visibly cutting off amounts and leaving statuses and due dates outside the viewport; its “All invoices” tab also wraps awkwardly. Y’s dark green outstanding card creates a stronger focal point, but X delivers the more complete, polished experience across both sizes.

### invoice-dashboard-run-2

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 2 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X gives total outstanding clear priority with its tinted card and adapts invoice rows so client, amount, status, and due date remain visible on the phone. Y retains a wide table on mobile, clipping statuses and leaving amounts and due dates outside the visible area. Both use restrained palettes, but Y’s unexplained sparklines add little, while X’s small secondary text and awkwardly wrapped mobile follow-up message limit its polish.

### landing-page-run-1

X = `iteration-3/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 2 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y wins on responsive craft: its feature accordion and membership preview stay orderly on mobile, while X’s feature icons and numbered labels collide with headings and body copy. Y’s rust accent gives the hero CTA and highlighted “climb” a clear visual priority, and its product previews make the offering concrete. X’s fuller dashboard and illustrated touches feel tailored, though Y’s outdoor climbing photo is less specific to gym operations.

### landing-page-run-2

X = `iteration-3/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s “More climbing. Less admin.” headline communicates the benefit faster, while the membership card, booking strip, and day-pass ticket make the features tangible. Its climbing illustration and restrained blue accents give it more product-specific character than X. X offers calmer spacing and a better-adapted mobile dashboard with tabs; Y’s retained sidebar makes its phone preview cramped, but its stronger visual storytelling wins overall.

### logo-run-1

X = `iteration-3/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  | 3 |  | 3 |  |  |  |  |  |  | 4 | 3 |  | 2 |
| Y (iteration-4/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |

Y’s upright stem and two right-facing leaves form a clearer F, giving the botanical symbol a stronger connection to Fernway. Its sturdier geometry holds together better at small sizes and pairs more convincingly with the bold serif wordmark; X’s curved, tapering stem feels softer but less distinctive. Both work in one color on white, but the dark green loses substantial contrast on the dark backgrounds shown.

### logo-run-2

X = `iteration-3/with-skill`, Y = `iteration-4/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (iteration-4/with-skill) |  | 4 |  | 3 |  |  |  |  |  |  | 3 | 3 |  | 2 |

X’s two leaf-shaped arms form a cleaner, more memorable F that holds together better at favicon size. Y’s extra left-facing leaf strengthens the botanical idea but crowds the central junction and makes the small silhouette less clear. X’s high-contrast serif adds editorial character; both candidates lose substantial visibility with dark green on the dark backgrounds shown.

### pricing-restyle-run-1

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s oversized, left-aligned headline gives it a more distinctive editorial character, carried consistently into the phone layout. Its separated currency symbols, bolder feature headings, and ruled benefit sections create clearer typography and grouping than X. X’s “Start free” and “Choose Team” buttons are more specific, but Y is more visually resolved overall.

### pricing-restyle-run-2

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more cohesive: serif plan names and prices extend the brand typography, while the rust Pro button creates a precise focal point. Its introduction explains the free allowance, and the compact benefits strip keeps both layouts focused on choosing a plan. X has a more distinctive asymmetric hero, but its large dark Pro card dominates the comparison and the extra benefits heading adds unnecessary length.

### rsvp-page-run-1

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y’s compact invitation header brings the form much closer to the top on mobile, and its framed composition maintains a cohesive reading order across sizes. X has more distinctive artwork and a strong desktop split layout, but its oversized arch pushes the first mobile input roughly twice as far down the page. Both use polished serif typography and restrained, readable green palettes.

### rsvp-page-run-2

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X feels more personal through its monogram, flowering tree illustration, and balanced date-and-venue arrangement. Its phone layout also keeps both attendance labels on one line, while Y’s decline label wraps awkwardly. Y offers larger form text and a more compact layout, but X has the stronger overall invitation character. Both clearly disclose browser-only saving; X more explicitly explains that the couple will not receive the response.

### svg-animation-run-1

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 4 | 4 | 4 |  |  |  |  |

Y’s envelope and check badge show a more legible gentle bob across the frames, while X’s movement is barely perceptible. Y’s faint horizontal ground stroke provides a stable reference that makes the floating motion easier to read. Both use clean envelope outlines and a restrained green confirmation badge appropriate to the caught-up state.

### svg-animation-run-2

X = `iteration-4/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |
| Y (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |

X’s simpler envelope and solid green badge make the completion state easier to read at a small size. Y’s outlined badge is cohesive, but the additional diagonal envelope seams add detail without strengthening the message. Both show a barely perceptible vertical bob across the sampled frames: appropriately calm, though neither demonstrates especially polished motion.
