# Blind judgments: iteration-4, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-2/baseline**: 2
- **iteration-4/with-skill**: 12

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-2/baseline | 3.40 | 4.00 | 2.70 | 3.33 | 3.80 | 4.00 | 3.70 | 4.00 | 3.00 | 4.00 | 3.00 | 3.00 | 3.40 | 2.00 |
| iteration-4/with-skill | 4.00 | 4.00 | 3.90 | 4.00 | 3.30 | 4.00 | 4.00 | 3.50 | 2.50 | 5.00 | 4.00 | 4.00 | 4.00 | 3.00 |

## Pairs

### booking-flow-run-1

X = `iteration-2/baseline`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 2 | 4 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y keeps the contact step focused, with readable fields and a desktop sidebar that adapts cleanly into a mobile progress header. X has more brand character, but its faint secondary text and compressed mobile stepper reduce readability. Its premature $119 estimate, default room counts, and unsupported customer claims add unnecessary content and substantially lengthen the phone page.

### booking-flow-run-2

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 3 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X offers the stronger phone experience: readable labels, full-width email and phone fields, and a compact first step with an obvious Continue button. Y has more distinctive branding through its clover mark, house illustration, and desktop sidebar, but its small, pale supporting text and two-column phone fields weaken readability. Y also adds address collection and several promotional reassurances, making the contact step longer and busier.

### invoice-dashboard-run-1

X = `iteration-2/baseline`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y’s mobile invoice cards keep client, amount, status, and due date visible; X’s clipped table hides essential information. Y also offers stronger text contrast and clearer emphasis on outstanding and overdue balances. X has more personality through its serif headings and illustrations, but the upgrade promotion and secondary panels dilute the core workflow.

### invoice-dashboard-run-2

X = `iteration-2/baseline`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y prioritizes outstanding balances and recent invoices, and its mobile invoice cards keep client, amount, status, and due date visible; X’s phone table shows only invoice and client columns. Y also has more readable supporting text, while X’s pale labels and cramped mobile reminder headline weaken its polish. X has more personality through its branding and cash-flow chart, but Y handles the brief’s core tasks more effectively across both sizes.

### landing-page-run-1

X = `iteration-2/baseline`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 4 |  | 2 | 3 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y has stronger typographic rhythm and more readable mobile spacing, with a clear progression from climbing imagery to product details and the final CTA. Its forest green, rust accents, wave logo, and contour pattern form a more cohesive identity than X’s badges and decorative flourishes. X covers more information, but its small supporting text weakens readability, while partner logos and the $99/500-member plan introduce claims the brief doesn’t establish.

### landing-page-run-2

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 4 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X communicates the product more directly: “More climbing. Less admin.” leads into a dashboard preview and three clearly differentiated feature cards that stack cleanly on mobile. Its membership card, booking slip, and day-pass ticket make the functionality tangible, while the climbing illustration adds personality. Y has striking typography and effective orange accents, but its outdoor climbing photograph explains less about gym operations, and the customer-logo strip, $99 pricing, and migration/support promises introduce unsupported claims.

### logo-run-1

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 3 |
| Y (iteration-2/baseline) |  | 4 |  | 3 |  |  |  |  |  |  | 3 | 3 |  | 2 |

X’s leafy F connects directly to Fernway, with a compact silhouette and sturdy serif wordmark that hold up better at small sizes. Y’s book-and-sprout concept communicates the business more explicitly, but its narrow internal gaps and tiny subtitle lose clarity as it shrinks. X also supplies a successful cream reversed lockup; both green favicon treatments lack contrast on dark backgrounds, while Y’s full dark-background logo is particularly difficult to read.

### logo-run-2

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 3 |
| Y (iteration-2/baseline) |  | 4 |  | 3 |  |  |  |  |  |  | 3 | 3 |  | 2 |

X’s leaf-built F combines the name and botanical theme in a memorable silhouette that holds together better at favicon sizes. Y’s open book and sprout communicate the business more explicitly, but its narrow stem gaps and separate leaves lose definition at 16px, while the tiny tagline adds little at this scale. X supplies a successful cream reversed wordmark, although its green standalone icons remain low contrast on dark; Y’s dark presentation has poor contrast throughout.

### pricing-restyle-run-1

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **Y** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y edges ahead through more deliberate brand details: the italic rust-colored “grow,” outlined popularity badge, and coordinated benefit icons. X is clear and restrained, but feels more conventional; Y’s additional slogans and feature-list headings introduce some unnecessary copy. Y also needs a mobile typography fix: “Good questions.Simple answers.” visibly loses its separating space.

### pricing-restyle-run-2

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 4 |  | 3 | 3 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X feels more resolved: concise copy, a clearly emphasized Pro card, and consistent spacing make the purchase decision straightforward across screen sizes. Y’s sage palette, book icon, and italic headline give it more character, but its repeated literary taglines add filler. Y also has visible mobile text defects—“between.Choose” and “questions.Simple”—that undermine its otherwise polished presentation.

### rsvp-page-run-1

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 3 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X wins on readability and restraint: its larger form text, stronger contrast, and generous mobile field widths make responding easier. Y’s terracotta names and floral illustration feel personal, but faint supporting text and the padded form card reduce legibility and usable space. Y invents a reply deadline and adds sentimental filler; X is more direct, although its explicit local-only saving falls short of collecting an RSVP.

### rsvp-page-run-2

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 3 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X feels more cohesive through its botanical illustration, fine border, and restrained invitation typography; its shorter mobile introduction also brings guests to the form sooner. Y’s desktop split layout works well, but the large photograph delays the mobile form, and pale labels and field outlines weaken contrast. X’s “Save RSVP” button and explicit notice that responses are not sent communicate the visible limitation more clearly than Y’s “Confirm my RSVP.”

### svg-animation-run-1

X = `iteration-4/with-skill`, Y = `iteration-2/baseline`. Preferred: **Y** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 3 | 2 | 5 |  |  |  |  |
| Y (iteration-2/baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |

Y’s open envelope, visible letter, and mint check create a more considered illustration, with a cohesive lavender palette. Its slight vertical movement is more perceptible across the frames, although neither candidate demonstrates much motion. X is exceptionally restrained and its darker check reads clearly, but the nearly static drawing feels more like a status icon.

### svg-animation-run-2

X = `iteration-2/baseline`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |

Y’s simple envelope and solid green check communicate completion clearly at a small size. X’s lavender envelope, letter, halo, shadow, and sparkles are cohesive, but add visual fuss and use faint strokes. Both show gentle vertical movement across the sampled frames, though neither demonstrates especially distinctive motion.
