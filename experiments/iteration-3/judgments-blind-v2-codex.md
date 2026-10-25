# Blind judgments: iteration-3 (blind-v2), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-2/with-skill**: 6
- **iteration-3/with-skill**: 8

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-2/with-skill | 4.00 | 4.00 | 3.90 | 3.67 | 3.30 | 3.50 | 4.00 | 4.00 | 3.00 | 4.50 | 4.00 | 3.50 | 3.60 | 2.50 |
| iteration-3/with-skill | 4.00 | 4.00 | 3.60 | 3.58 | 3.70 | 4.00 | 3.80 | 3.50 | 3.00 | 4.00 | 4.00 | 3.50 | 3.90 | 3.50 |

## Pairs

### booking-flow-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **Y** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 3 | 2 | 3 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y handles the phone layout substantially better: its collapsed cleaning summary keeps the page focused, while X’s action footer visibly overlaps the phone-number field and leaves excessive empty space underneath. Y’s “Continue to home details” also communicates the next step more directly. X has warmer, more product-specific character through its green palette and house illustration, but Y’s integrated card and consistent spacing deliver the stronger overall execution.

### booking-flow-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X feels more specific to home cleaning: its serif headline, warm green palette, and living-room illustration create a cohesive identity. Its full-width mobile Continue button also gives the primary action stronger emphasis. Y has clearer task-oriented copy and a more economical booking summary, but its blue styling feels more generic and its repeated step counts add clutter. X’s demo-payment disclaimer is unnecessary.

### invoice-dashboard-run-1

X = `iteration-2/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/with-skill) | 4 |  | 4 | 2 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y has more consistent spacing and a better-contained phone layout, with accessible navigation and compact summary cards. X’s lime accent and dark sidebar are more distinctive, but its phone view shows a clipped logo, a large empty right gutter, and awkward wrapping in the overdue card. Both mobile tables compromise essential information: X clips statuses, while Y prioritizes invoice IDs and clips amounts, leaving status and due date offscreen.

### invoice-dashboard-run-2

X = `iteration-2/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/with-skill) | 4 |  | 4 | 3 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 3 | 3 |  | 3 |  |  |  |  |  | 4 |  |

X’s dark outstanding balance card establishes a clearer priority, while its payment breakdown and upcoming deadlines make the overview more useful. Y’s consistent typography and spacious table are polished, but its equally weighted summary cards and unexplained sparklines feel more generic. Both phone layouts clip essential invoice fields: X loses status and clips amounts, while Y places amounts and due dates entirely outside the visible table.

### landing-page-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **Y** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 3 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y is more consistently resolved across desktop and phone: its feature summaries stack cleanly, and the membership preview makes the product’s value concrete. X’s mobile feature section has icons and numbered labels colliding with headings and body copy, undermining readability and polish. X’s forest-green palette and handwritten annotation give it character, while Y’s blue emphasis, climbing holds, and rope illustrations provide equally specific branding with stronger execution.

### landing-page-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **Y** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s repeated “Book a demo” gives visitors a clearer next step than X’s vague “Explore Tidepool” and “Find your flow.” Its feature selector and membership preview provide more concrete product detail, while the navy and lime accents establish stronger emphasis. X has the better mobile dashboard treatment: its adapted layout remains readable, whereas Y’s compressed desktop preview makes much of the interface illegible.

### logo-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **Y** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 3 |
| Y (iteration-2/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 3 |

Y’s upright stem and two right-facing leaves make the botanical F clearer and sturdier at favicon sizes; X’s curved stem reads more readily as a generic sprout. X’s heavier serif lettering feels more robust, while Y’s delicate hairlines give its wordmark elegance at some cost to resilience. Both reversed wordmarks work well, but the colored icons lose contrast on the dark panels and browser tabs.

### logo-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 4 |
| Y (iteration-2/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

Both combine an F with leaflike fronds, a clear connection to Fernway’s name. X’s green mark and finer serif wordmark feel more botanical and literary; Y’s heavier serif feels sturdy and welcoming. X wins on practical execution: its cream icon stays clear on dark backgrounds, while Y’s brown icons nearly disappear in the dark size tests and browser tab.

### pricing-restyle-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 3 | 2 |  | 4 |  |  |  |  |  | 3 |  |

X feels more tailored to Marginalia: its warm paper palette, restrained rust accents, and editorial headings support the notebook identity. Its mobile header keeps account actions together, while Y strands the signup button on a third row. Y makes Pro immediately prominent and uses clearer plan-specific buttons, but its navy-and-blue treatment feels more generic and its oversized dollar signs compete with the prices.

### pricing-restyle-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X feels more specific to Marginalia: serif plan names, warm paper tones, and burgundy accents form a coherent notebook identity. Its headline and supporting copy also communicate the product and free allowance more specifically than Y’s generic pricing introduction. Y makes Pro more prominent with a tinted card and handles the mobile header and footer more comfortably, but its blue palette and bold sans-serif plan labels feel more conventional.

### rsvp-page-run-1

X = `iteration-2/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/with-skill) | 4 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more specific to the wedding: its oak illustrations, sage palette, double border, and italic sign-off create a cohesive invitation. Its guest-count stepper also provides a clearer starting point than X’s empty numeric field. X’s stacked attendance options are easier to read on mobile than Y’s smaller side-by-side labels. Both explicitly say responses stay on the device and aren't sent to the couple, limiting their usefulness as RSVP pages.

### rsvp-page-run-2

X = `iteration-2/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s expressive serif typography, emphasized venue, botanical illustration, and fine double border create a more distinctive wedding invitation. Its guest-count stepper also makes the available action clearer on mobile. X is more compact and explicitly states that responses are not sent to the couple; Y’s browser-only notice is less direct, and it omits the requested weekday.

### svg-animation-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-2/with-skill) |  |  |  |  |  | 3 |  | 4 | 3 | 5 |  |  |  |  |

X’s filled green check gives a clearer sense of completion, while its envelope seams add useful detail without much clutter. Y is especially restrained, but its pale blue outlined badge feels less conclusive. Both show small vertical shifts across the frames, keeping things calm but making the loop barely perceptible.

### svg-animation-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/with-skill`. Preferred: **Y** (iteration-2/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 4 |  |  |  |  |
| Y (iteration-2/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |

Y feels more polished: faint envelope folds, a delicate ground shadow, and a neatly placed upper-right check badge give it depth without clutter. X communicates completion clearly, but its darker, disconnected diagonal seams feel less refined. Both show restrained vertical movement across the sampled frames, with little evidence to distinguish their easing or loop quality.
