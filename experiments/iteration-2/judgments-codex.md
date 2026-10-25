# Blind judgments: iteration-2, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **baseline**: 6
- **with-skill**: 8

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 3.50 | 4.00 | 2.80 | 3.50 | 3.90 | 4.00 | 3.70 | 4.00 | 3.50 | 4.00 | 3.00 | 3.00 | 3.50 | 2.00 |
| with-skill | 4.00 | 4.00 | 4.00 | 3.67 | 2.80 | 4.00 | 4.00 | 3.00 | 3.00 | 5.00 | 4.00 | 4.00 | 3.70 | 3.00 |

## Pairs

### booking-flow-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 3 |  | 2 | 3 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 4 | 4 | 2 |  | 4 |  |  |  |  |  | 4 |  |

Y makes the booking task clearer through readable labels, stronger contrast, and the specific “Continue to home details” button. Its collapsed mobile summary keeps the page focused, while X adds substantial scrolling through promotional content, an unexplained $119 estimate, and customer claims. X has a more distinctive identity through its spruce mark, warm palette, and photography, but its small, faint supporting text and compressed mobile stepper weaken usability.

### booking-flow-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 3 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X better serves the phone-first brief with readable labels, full-width email and phone fields, and a clear booking headline. Y has more distinctive branding through its forest-green palette, house illustration, and integrated desktop sidebar, but its mobile form squeezes email, phone, and address inputs into narrow columns. Y’s tiny, faint supporting text and additional promotional copy weaken readability and focus; X’s main drawback is the lengthy, largely empty booking summary on mobile.

### invoice-dashboard-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |

X makes outstanding balances and invoice amounts easier to scan through stronger contrast, larger figures, and a simpler structure. Y’s serif headings and muted green identity are more distinctive, but faint supporting text and promotional panels dilute the core task. Both phone tables clip essential information; X retains amounts, while Y shows only invoice numbers and clients. Y also has an unexplained green rectangle floating over the invoice table on both screen sizes.

### invoice-dashboard-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 2 | 3 |  | 3 |  |  |  |  |  | 3 |  |

X makes the outstanding balance unmistakable and brings recent invoices closer to the top; Y’s cash-flow chart and reminder banner push the essential list down, especially on mobile. X’s stronger contrast and more readable supporting text better suit a financial dashboard, while Y’s pale labels and miniature mobile metrics weaken scanning. Both phone tables leave key columns offscreen, but Y’s visible table shows only invoice identifiers and clients, hiding amount, status, and due date.

### landing-page-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s larger product previews, readable supporting text, and more focused page structure communicate the app clearly across desktop and phone. Its climbing holds, rope illustrations, and membership example give the design product-specific character. X has a memorable headline and climbing photograph, but its smaller text and longer mobile page weaken scanning, while the customer logos and $99 pricing introduce claims unsupported by the brief.

### landing-page-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X communicates the product more directly through its dashboard preview, explicit feature names, and consistent “Book a demo” calls to action; its mobile layout also keeps supporting copy comfortably readable. Y has more personality through its climbing photography, coral accents, and graphic flourishes, but introduces unsupported partner logos, testimonials implied by avatars, and $99 pricing. X feels more credible and focused, although its overall visual language is more conventional.

### logo-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 3 |
| Y (baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 3 | 3 |  | 2 |

X’s leaf-built F is memorable and keeps a clearer silhouette at 16–32 px. Y’s book-and-sprout concept communicates the business more explicitly, but its narrow internal gaps lose definition and its tiny tagline is fragile. X supplies a readable cream reversed lockup, while Y’s dark-green version nearly disappears on black; both candidates’ dark-background favicon marks lack contrast.

### logo-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 3 |
| Y (baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 3 | 3 |  | 2 |

X’s leaf-shaped F combines the name and botanical theme in a compact silhouette that remains clearer at favicon sizes. Y’s open book and sprout communicate the business more explicitly, but the leaves and narrow page separations become crowded at 16px. Both show controlled curves and suitable serif typography; X also supplies a successful reversed full logo, although its dark-panel icons lose contrast, while Y’s entire dark presentation is difficult to read.

### pricing-restyle-run-1

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 3 | 2 |  | 4 |  |  |  |  |  | 3 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s warm palette, italic hero accent, and softly highlighted Pro card give Marginalia a more considered identity; X’s blue-and-navy treatment feels generic. Y also handles the phone header much better, while X spreads navigation and signup across three rows. X has more direct, economical copy; Y adds marketing filler and loses polish with the visibly joined “questions.Simple” mobile FAQ heading.

### pricing-restyle-run-2

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 2 |  | 4 |  |  |  |  |  | 3 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more tailored to Marginalia: the book mark, editorial typography, muted green palette, and coordinated icons create a coherent identity. Its plan cards have clearer internal grouping and more specific trial CTAs, while X’s pricing headline is more direct and its copy more economical. Y needs another mobile polish pass: “between.Choose” and “questions.Simple answers.” visibly run together.

### rsvp-page-run-1

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y wins narrowly through its cohesive art direction: terracotta names, a sage ampersand, botanical illustration, and a balanced desktop split. X offers a more direct mobile experience, with the form appearing substantially earlier and supporting text easier to read. Y’s long mobile introduction, faint small text, invented reply deadline, and decorative slogans weaken an otherwise more distinctive design.

### rsvp-page-run-2

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 3 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X’s arched countryside photograph, expressive serif typography, and balanced desktop columns create a more distinctive wedding invitation. Its small, pale secondary text compromises readability, and the extended introduction pushes the form considerably farther down on mobile. Y offers a more compact RSVP flow and clearer disclosure that responses stay on the device, but its uniform outlined controls and restrained typography feel more generic.

### svg-animation-run-1

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 5 |  |  |  |  |

X feels more thoughtfully illustrated: the emerging letter, lavender envelope, and mint check create a quiet sense of completion. Y is exceptionally restrained and clearly readable, but its plain envelope and blue badge feel more generic. Both show subtle vertical movement across the sampled frames, though neither demonstrates especially distinctive motion or easing.

### svg-animation-run-2

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) |  |  |  |  |  | 4 |  | 4 | 4 | 4 |  |  |  |  |
| Y (with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 5 |  |  |  |  |

X’s layered letter, lavender envelope, and mint check badge give the completion state more warmth and visual depth. Its small positional changes feel restrained across the sampled frames, while the soft shadow helps ground the float. Y is exceptionally spare and readable, but its uniform envelope-and-badge movement and simpler drawing feel less distinctive.
