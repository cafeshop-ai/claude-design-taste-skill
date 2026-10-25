# Blind judgments: iteration-4 (blind-v1), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-1/with-skill**: 7
- **iteration-4/with-skill**: 7

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-1/with-skill | 4.00 | 3.50 | 3.10 | 3.67 | 4.00 | 4.50 | 3.80 | 4.00 | 3.00 | 4.50 | 4.00 | 3.00 | 4.00 | 2.00 |
| iteration-4/with-skill | 4.00 | 4.00 | 4.00 | 4.00 | 3.10 | 4.00 | 4.00 | 3.50 | 3.00 | 4.50 | 4.00 | 3.50 | 3.90 | 2.00 |

## Pairs

### booking-flow-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 2 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |

X offers a more focused booking experience: its compact mobile stepper, concise introduction, and shorter form keep the Continue action readily accessible. Y’s serif headline and living-room illustration add personality, but the promotional copy and additional address fields make the first step substantially longer on phones. Y also presents an unexplained $120 estimate and preset bedroom/bathroom counts before the home-details step.

### booking-flow-run-2

X = `iteration-1/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y keeps the contact step focused, with four fields, a clear next-step cue, and a much shorter phone layout. X has stronger brand character through its expressive headline, photography, and coordinated icons, but address fields and repeated reassurance make the mobile page unnecessarily long. Its $110 estimate and “2 beds · 1 bath” summary also present assumptions before the home-details step.

### invoice-dashboard-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y has a more distinctive identity through its serif branding, warm sage sidebar, and cohesive chart styling. Its compact mobile invoice rows make amounts, statuses, and due dates easier to compare than X’s taller cards. X is more focused and preserves a clearly labeled “New invoice” button on mobile; Y’s promotional copy and icon-only create action weaken an otherwise stronger design.

### invoice-dashboard-run-2

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 2 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X better fulfills the brief across screen sizes: its mobile invoice rows retain client, amount, status, and due date in a readable layout. Y’s mobile table clips statuses and hides due dates, while its chart and large follow-up panel push recent invoices far down the page. Y has a more distinctive plum identity, but X’s focused content and stronger responsive layout are decisive.

### landing-page-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s indoor climbing illustration, italic headline accents, and lime badge create a more specific identity than X’s photo-and-floating-dashboard composition. Y also adapts its desktop feature list into compact mobile tabs and addresses concrete buying questions in the FAQ. X offers a calmer, more concise page and a clearer at-a-glance product summary, but Y feels more tailored to small climbing gyms.

### landing-page-run-2

X = `iteration-1/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 3 | 3 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-4/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s feature cards integrate explanations, product examples, and links more cohesively, with comfortable typography and spacing on mobile. Its climbing illustration and membership/pass artifacts give the product a clear identity. X’s expressive serif headings and dark green section are compelling, but its browser-like secondary buttons weaken the polish, and the $89 pricing introduces an unsupported commercial claim.

### logo-run-1

X = `iteration-1/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) |  | 4 |  | 3 |  |  |  |  |  |  | 4 | 3 |  | 2 |
| Y (iteration-4/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

Y’s bolder serif wordmark and more open spacing between the fern’s leaves create a more cohesive, confident logo. X’s “BOOKSHOP & CAFÉ” descriptor adds useful context but becomes too small to read comfortably. Both botanical F marks remain recognizable as small silhouettes, but the dark green loses substantial contrast on the dark backgrounds.

### logo-run-2

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (iteration-1/with-skill) |  | 3 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

X’s upright stem and two horizontal leaves form a clearer F, giving Fernway a more distinctive silhouette that holds together better at favicon sizes. Y’s organic sprout and fine serif wordmark feel graceful, but the mark reads more generically as a plant and the tiny “BOOKSHOP & CAFÉ” descriptor loses readability. Both work in one color on white, but their dark green nearly disappears against the dark backgrounds shown.

### pricing-restyle-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y wins narrowly through a more distinctive composition: the split desktop hero, italic green headline, and stronger functional headings give Marginalia a coherent identity. Its mobile benefits use rules and aligned icon columns to create clearer grouping, while expanded device-sync and SSO labels improve clarity. X is polished and slightly more concise, but its centered hero and uniform serif headings feel more conventional.

### pricing-restyle-run-2

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more cohesive: the notebook mark, green italic headline, and pale green Pro card establish a recognizable identity, with the filled Pro button providing clear emphasis. Its feature-group headings and explicit trial information also support comparison. X is clean and professional, with more compact mobile pricing, but its dark featured card and simpler headline treatment feel more conventional; Y’s extra introductory copy and stacked mobile price units slightly weaken its efficiency.

### rsvp-page-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s farm illustration, plum accents, and coordinated cream panels create a more distinctive wedding invitation, with polished section transitions on mobile. X is similarly readable and more economical with copy, but its botanical arch feels more familiar. Y loses content points for decorative filler and “Confirm my RSVP,” which overstates an action described below as saving only on the device; X’s “Save RSVP” is clearer.

### rsvp-page-run-2

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |

X better prioritizes the RSVP task: its compact invitation and clear form bring the first field much earlier on mobile. Y’s photographic panel and split desktop composition have more visual character, but the oversized names, extra navigation, and repeated romantic copy add substantial scrolling on phones. X also pairs “Save RSVP” with an explicit notice that the response is not sent; Y’s “Confirm RSVP” suggests more completion than its local-save notice supports.

### svg-animation-run-1

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-1/with-skill) |  |  |  |  |  | 5 |  | 4 | 3 | 4 |  |  |  |  |

Y’s checked letter emerging from an open envelope feels especially apt for a cleared inbox, with cohesive pale green fills and a subtle grounding shadow. X’s closed envelope and dark green badge communicate completion clearly, but feel more like a delivery confirmation. Both show restrained vertical movement across the sampled frames, though neither demonstrates particularly expressive motion.

### svg-animation-run-2

X = `iteration-4/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-4/with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 5 |  |  |  |  |
| Y (iteration-1/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |

Y’s envelope folds, pale circular backdrop, and soft grounding shadow create a more finished empty-state illustration while remaining calm. X’s larger envelope and bolder check badge read more clearly, but feel more like a standard status icon. Both show subtle vertical movement across the frames; neither demonstrates particularly distinctive motion.
