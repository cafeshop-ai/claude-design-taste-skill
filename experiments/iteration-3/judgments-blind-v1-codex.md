# Blind judgments: iteration-3 (blind-v1), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-1/with-skill**: 10
- **iteration-3/with-skill**: 4

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-1/with-skill | 4.00 | 3.50 | 3.30 | 3.75 | 4.00 | 4.00 | 3.80 | 4.00 | 3.00 | 5.00 | 4.00 | 3.50 | 4.00 | 2.00 |
| iteration-3/with-skill | 4.00 | 3.50 | 3.80 | 3.42 | 2.80 | 4.00 | 3.90 | 3.50 | 3.00 | 4.50 | 4.50 | 3.50 | 3.70 | 2.00 |

## Pairs

### booking-flow-run-1

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 2 | 2 |  | 4 |  |  |  |  |  | 3 |  |

X’s editorial serif headline, room illustration, and compact mobile price summary create a more distinctive, cohesive service experience. Y stages the contact step more simply, but its mobile action area visibly cuts across the phone field and leaves a large empty block underneath. X loses content points for presenting an unexplained $120 estimate and assumed home configuration; Y’s placeholder-heavy summary and repeated “Booking preview” text add little useful information.

### booking-flow-run-2

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y keeps the first step focused on contact details, with a prominent full-width Continue button on mobile and clear placeholders for choices still to come. X adds address fields immediately and presents an unexplained $110 estimate, two-bedroom home, and cleaning duration before home details are collected. X has more distinctive branding and expressive typography, but Y’s concise copy and shorter phone layout better support the booking task.

### invoice-dashboard-run-1

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 2 | 3 |  | 4 |  |  |  |  |  | 4 |  |

X wins through its phone layout: client, amount, status, and due date remain visible, while Y’s table crops amounts and leaves status and due date offscreen. X’s overdue reminders provide specific next actions, and its botanical branding gives the product a more individual character. Y emphasizes total outstanding more clearly, but X feels more complete overall, despite small secondary text and an ambiguous plus-only create button on mobile.

### invoice-dashboard-run-2

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 3 | 2 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 2 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s plum outstanding card, stronger headline, and actionable overdue panel create clearer priorities and a more recognizable product. X is concise and internally consistent, but its uniformly pale cards feel generic, and its phone table hides both amounts and due dates. Y keeps invoice amounts visible on mobile, although clipped statuses and the large empty right gutter substantially weaken its execution; its motivational copy also adds unnecessary content.

### landing-page-run-1

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 2 | 3 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y’s climbing-wall illustration, rust accents, and selective serif emphasis give it a more distinctive identity for this product. Its mobile feature tabs and product preview stay orderly, whereas X’s feature icons, headings, and section labels visibly overlap on the phone. X’s desktop dashboard hero communicates the product well, but Y sustains stronger polish across both sizes.

### landing-page-run-2

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y has the stronger identity: expressive serif headlines, concrete membership/calendar/pass previews, and the dark green section create a more memorable page with clear changes in rhythm. X is focused and polished across desktop and phone, but its feature section feels more generic. Y loses content points for introducing an unsupported $89 price, and its gray outlined feature buttons feel less considered than X’s understated links.

### logo-run-1

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (iteration-3/with-skill) |  | 3 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

X’s upright stem and two right-facing leaves form a clearer F, giving the botanical idea a stronger connection to Fernway. Its heavier construction also holds together better at favicon size; Y’s curved stem feels graceful but becomes delicate and reads more like a generic sprout. Both use restrained serif typography, but both lose substantial contrast with dark green on near-black backgrounds.

### logo-run-2

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) |  | 3 |  | 3 |  |  |  |  |  |  | 4 | 3 |  | 2 |
| Y (iteration-3/with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 5 | 4 |  | 2 |

Y combines leaf-shaped arms with a clear F, giving Fernway a more specific identity than X’s sprout. Its upright stem and open gap retain clearer structure at 16–32 px, while its heavier wordmark feels more assured; X’s tiny descriptor becomes unreadable. Both marks work in one color, but the dark green loses substantial contrast on the dark backgrounds shown.

### pricing-restyle-run-1

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more specific to Marginalia: the italic “train of thought” headline, green accents, and notebook mark form a cohesive identity. Its plan-specific buttons, explicit trial terms, and visible cancellation answer provide clearer decision support than X’s generic buttons and closed FAQs. Both layouts are polished across desktop and phone, though Y’s tiny uppercase section labels are less readable than X’s larger headings.

### pricing-restyle-run-2

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-1/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more tailored to a notebook product: the editorial hero, italic green emphasis, and coordinated section headings establish a stronger identity. Its tinted Pro card and feature-group labels make the recommendation and plan differences easier to scan. X is polished but more conventional; it does keep prices and billing units together more effectively on mobile, where Y splits them across lines.

### rsvp-page-run-1

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y’s compact invitation header brings the RSVP fields much earlier on mobile, while X’s large illustrated introduction pushes the task below the first screen. Y also pairs “Save my RSVP” with an explicit “Not sent to Sam & Priya” disclosure, making the visible behavior clearer than X’s “Confirm” wording. X has more personality through its countryside illustration and plum palette, but Y’s restrained stationery composition and tighter content better serve the task.

### rsvp-page-run-2

X = `iteration-1/with-skill`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 |  | 3 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y’s compact invitation and clear form sequence make the RSVP easier to reach, especially on mobile, where X’s oversized photographic introduction substantially delays the fields. Y also pairs “Save RSVP” with an explicit browser-only explanation; X’s “Confirm RSVP” and download instruction leave the outcome less clear. X has more personality through its photography and expressive typography, while Y’s wrapping decline label is a small polish issue.

### svg-animation-run-1

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-1/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |

Y’s checked letter sits cohesively inside the open envelope, with pale green fills and a soft oval shadow that feel especially calm. X’s solid green check badge is more immediately legible, but draws more attention and feels closer to a delivery-status icon. Both show subtle vertical movement across the sampled frames; neither demonstrates particularly expressive timing or easing.

### svg-animation-run-2

X = `iteration-3/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 5 |  |  |  |  |
| Y (iteration-1/with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |

Y’s pale circular backdrop, soft grounding shadow, and filled green check create a more polished, reassuring empty-state illustration. X is clear and calm, but its heavier outlines and larger lower-right badge feel more utilitarian. Both show gentle vertical movement with limited variation across the sampled frames; neither demonstrates exceptional motion timing.
