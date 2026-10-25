# Blind judgments: iteration-1, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **baseline**: 5
- **with-skill**: 9

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 3.40 | 4.00 | 3.30 | 3.58 | 3.60 | 4.00 | 3.90 | 4.00 | 3.00 | 4.00 | 3.50 | 2.50 | 3.50 | 2.00 |
| with-skill | 4.00 | 3.50 | 3.60 | 3.67 | 3.60 | 4.00 | 3.90 | 4.00 | 3.00 | 5.00 | 4.00 | 4.00 | 4.00 | 2.00 |

## Pairs

### booking-flow-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 3 |  | 3 | 3 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y has a stronger typographic identity through its serif headline, more readable form styling, and a phone step indicator that remains fully visible; X clips the Review step. Y also places the mobile price summary directly above the action, while X puts it below the button. Y’s additional address fields make the first step considerably longer, but its spacing and contrast hold up better than X’s small, faint supporting text.

### booking-flow-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X is more readable on phones: email and phone receive full-width fields, and supporting text has stronger contrast and a more comfortable scale. Y has a compact desktop composition and a distinctive house illustration, but its pale, small text and paired mobile contact fields weaken usability. Y’s “Continue to home details” is more informative than X’s “Continue,” while X’s demo disclaimer adds unnecessary content.

### invoice-dashboard-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 2 | 3 |  | 3 |  |  |  |  |  | 3 |  |

X preserves client, amount, status, and due date on the phone; Y’s visible mobile table shows only client and invoice number, hiding essential information. X’s overdue panel makes follow-up priorities clear, while its clover branding and botanical illustration give the product a more specific identity. Both use small, faint secondary text, but Y also has unexplained dark green blocks obscuring an amount on desktop and the table footer on mobile.

### invoice-dashboard-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 2 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 3 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X offers a more useful overview: the payment chart adds context, and the overdue reminder connects a specific balance to an action. Its burgundy palette and stronger text contrast also give it more character and readability than Y’s pale typography and conventional purple styling. Both mobile tables compromise the brief: X clips statuses and due dates and visibly overflows the viewport, while Y prioritizes invoice numbers and leaves amounts, statuses, and due dates outside the visible area.

### landing-page-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X’s climbing-wall illustration and clearly labeled sample workspace give it a focused, product-specific story. Its compact mobile feature tabs also keep the page easier to scan, while Y’s “Your community is unique” heading becomes a choppy stack on mobile. Y has polished feature cards and attractive typographic contrasts, but its $99 pricing and apparent customer-logo strip introduce claims the brief does not substantiate.

### landing-page-run-2

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (with-skill) | 4 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X’s climbing photograph, community illustration, and integrated product previews create a richer identity specific to climbing gyms. Y has clearer mobile feature stacking, but its plain outlined buttons and repetitive section treatments feel more conventional. X wins narrowly: its cramped mobile feature cards and customer-logo strip implying unsupported social proof weaken an otherwise more polished, memorable design.

### logo-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 3 | 2 |  | 2 |

X’s leafy F connects directly to Fernway and retains a recognizable silhouette at favicon size. Y’s open book and sprig communicate the business more explicitly, but its numerous leaves and narrow stem lose definition at 16px. Both show polished typography, although X’s sturdier letterforms reproduce more reliably; both lose substantial contrast with dark green on near-black backgrounds.

### logo-run-2

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  | 3 |  | 3 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

Y’s open-book base and growing leaves connect the business and botanical name more specifically, with balanced geometry and a more cohesive wordmark lockup. X’s simpler, F-like sprout holds its silhouette better at favicon size, while Y’s narrow central gaps become harder to distinguish. Both work in one color on white, but their dark-green artwork loses substantial visibility on the dark backgrounds shown.

### pricing-restyle-run-1

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y has the stronger identity: its terracotta headline accent, book mark, and outlined Pro card create a cohesive visual language and a clearer focal point for conversion. Feature-group headings also make the plan differences easier to scan. X is polished and retains useful navigation on mobile, while Y needs another typography pass for the visibly joined sentences in its mobile introduction and FAQ heading.

### pricing-restyle-run-2

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X feels more cohesive: serif plan names, individual tier icons, and the dark Pro card give the page a recognizable identity and a clear focal point. Its mobile cards also keep prices and billing units together, while Y strands the units on separate lines and leaves excessive space above the desktop prices. Y has clearer feature-section headings and a more assertive billing toggle, but X’s small, muted supporting text could use stronger contrast.

### rsvp-page-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 3 | 3 | 3 |  | 4 |  |  |  |  |  | 3 |  |

X’s farm illustration and restrained plum palette give the invitation a more specific identity, while its darker field borders and larger form text improve readability. X also handles the phone layout more comfortably; Y’s oversized couple names nearly touch the right edge, and its pale placeholders lack contrast. Y’s compact desktop event details work well, but “Joyfully accepts” is awkward response wording; X’s device-only preview notice is its main content distraction.

### rsvp-page-run-2

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 3 | 4 | 3 |  | 3 |  |  |  |  |  | 4 |  |
| Y (baseline) | 3 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s farm illustration and invitation card feel more specific to the venue, with a clearer progression from invitation to RSVP on mobile. X’s oversized photographic panel delays the mobile form, while its instruction to download and share the reply adds uncertainty about how to RSVP. X has stronger field contrast; Y’s faint borders and small secondary text need more definition.

### svg-animation-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |

Y’s open envelope and checkmarked card communicate completion clearly, with a calm silhouette and economical detail. X is cleanly drawn, but its solid green badge, background halo, and tiny sparkles add visual activity at this small size. Both show subtle bobbing across the sampled frames; neither demonstrates especially expressive timing or easing.

### svg-animation-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |
| Y (baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |

X’s muted green palette and clear, dark check badge convey completion with particularly good restraint. Y’s lavender envelope and mint badge are cohesive, but the surrounding sparkle and dots add unnecessary decoration. Both show subtle vertical movement across the frames; neither demonstrates especially expressive motion or clearly assessable easing.
