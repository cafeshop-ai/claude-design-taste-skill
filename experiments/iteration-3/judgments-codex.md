# Blind judgments: iteration-3, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-2/baseline**: 4
- **iteration-3/with-skill**: 10

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| iteration-2/baseline | 3.50 | 4.00 | 2.70 | 3.42 | 4.00 | 4.00 | 3.60 | 4.00 | 3.00 | 4.00 | 3.50 | 3.00 | 3.20 | 2.00 |
| iteration-3/with-skill | 4.00 | 3.00 | 3.80 | 3.42 | 3.20 | 4.50 | 4.00 | 3.50 | 3.00 | 5.00 | 4.00 | 4.00 | 4.00 | 2.00 |

## Pairs

### booking-flow-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/baseline`. Preferred: **Y** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 2 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 3 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

Y wins on responsive craft: its mobile form remains unobstructed, and the summary becomes a compact horizontal card. X has clearer, larger text, but its mobile Continue footer overlaps the phone field and leaves substantial empty space below. Y’s distinctive branding and photography feel more finished, though faint microcopy and unsupported claims such as “$119” and “2,000+ happy homes” weaken accessibility and content credibility.

### booking-flow-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 3 | 3 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y wins on readability and phone usability: larger labels, stronger input borders, full-width email and phone fields, and a prominent full-width Continue button. X has more distinctive branding and a charming illustrated sidebar, but its faint supporting text and narrow paired fields weaken the mobile experience. Both contain unnecessary content: X adds generic reassurance claims, while Y gives substantial mobile space to an empty booking summary and a demo disclaimer.

### invoice-dashboard-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |

X makes outstanding money and the labeled New invoice action immediately obvious, with clearer contrast and more focused content. Y’s serif headlines and brand details add personality, but its promotional copy, extra panels, and faint secondary text weaken scanning. Both phone tables obscure essential invoice fields; Y also sacrifices width to a persistent navigation rail and has an unexplained green element overlapping invoice rows.

### invoice-dashboard-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 3 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y makes invoice tracking easier to scan through larger financial figures, clearer supporting text, and a client-first table with useful project descriptions. X has more personality in its cash-flow chart and reminder illustration, but faint labels and extra motivational copy weaken clarity. Y’s stacked phone summary cards are more readable than X’s compressed three-column cards; both phone tables leave essential amounts and due dates outside the visible area.

### landing-page-run-1

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 2 | 4 |  | 4 |  |  |  |  |  | 4 |  |

X wins on responsive execution: its illustrated feature cards stack cleanly, while Y’s mobile feature icons collide with headings and its numbered labels overlap body copy. Y has a more cohesive visual identity and a larger, more informative dashboard preview; X’s climbing photograph and feature illustrations give it stronger sport-specific context. X loses content points for the $99 pricing and named customer logos, which introduce unsupported claims beyond the brief.

### landing-page-run-2

X = `iteration-3/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) | 4 |  | 4 | 4 | 4 |  | 4 |  |  |  |  |  | 4 |  |
| Y (iteration-2/baseline) | 4 |  | 2 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X connects the promise directly to a useful dashboard and three clearly explained features, with more readable supporting text on mobile. Y’s climbing photograph, orange accents, and overlapping dashboard create a memorable hero, but its smaller text weakens the phone experience. Its named gym logos, $99 pricing, and migration promises also introduce unsupported claims beyond the brief, while X stays focused.

### logo-run-1

X = `iteration-3/with-skill`, Y = `iteration-2/baseline`. Preferred: **Y** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-3/with-skill) |  | 3 |  | 3 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (iteration-2/baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

Y’s open-book base growing into leaves connects the bookshop and Fernway name more specifically than X’s generic sprig. Its balanced geometry and refined serif wordmark give it a more distinctive identity, though the narrow internal gaps crowd at 16px and the tagline is barely readable. X’s simpler silhouette survives reduction better. Both lose substantial contrast on the dark backgrounds shown.

### logo-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) |  | 4 |  | 4 |  |  |  |  |  |  | 3 | 3 |  | 2 |
| Y (iteration-3/with-skill) |  | 3 |  | 4 |  |  |  |  |  |  | 4 | 4 |  | 2 |

Y’s leaf-shaped F has a simpler, more memorable silhouette and retains clearer internal space at favicon sizes. X’s sprout emerging from an open book communicates the business more specifically, but its narrow stem and page divisions become crowded at 16px. Both have polished serif wordmarks and work in one color, but the dark green nearly disappears against the dark backgrounds shown.

### pricing-restyle-run-1

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 4 |  | 3 | 3 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y feels more professional through larger, more readable card text, consistent spacing, and a clear pricing-focused headline. Its phone layout preserves navigation and handles section headings cleanly; X visibly runs “Good questions.Simple answers.” together. X has more brand character through its italic accent and warmer copy, but its extra slogans and small supporting text make the page feel busier.

### pricing-restyle-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 4 |  | 3 | 3 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y is more direct: its headline and 100-note introduction explain the offer, while larger plan names and clearer text sizing make comparison easier. Its restrained red accents consistently emphasize Pro and interactive elements. X has more personality through its green palette and literary typography, but adds vague copy and shows missing spaces on mobile in “between.Choose” and “questions.Simple”; its explicit 14-day trial messaging is a strength.

### rsvp-page-run-1

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 4 |  | 2 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |
| Y (iteration-3/with-skill) | 4 |  | 3 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y keeps the event details and form in a compact, readable sequence across both sizes; X’s oversized stacked names push the mobile form roughly 800px down the page. X has more personality through its terracotta accents and botanical illustration, but adds an unsupported reply deadline and several repetitive sentimental lines. Y’s device-only saving disclaimer is clear, though it reveals a limitation for guests intending to submit an RSVP.

### rsvp-page-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) | 3 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |
| Y (iteration-3/with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y wins on readability and focus: larger form labels, stronger contrast, and concise event details make the RSVP easier to scan on both screens. X’s arched countryside photograph and asymmetric desktop composition give it more character, but faint supporting text and extra sentimental copy weaken usability and lengthen the phone page. Y’s botanical stationery treatment is more conventional, yet its consistent spacing and clearer controls make it the stronger overall design.

### svg-animation-run-1

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **Y** (iteration-3/with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-3/with-skill) |  |  |  |  |  | 5 |  | 4 | 3 | 5 |  |  |  |  |

Y’s clearer envelope outline and solid green check badge communicate completion immediately at this small size. X’s lavender halo, sparkles, and letter add charm, but its faint strokes reduce legibility and introduce extra decoration. Both show restrained vertical movement across the sampled frames; neither demonstrates particularly distinctive motion.

### svg-animation-run-2

X = `iteration-2/baseline`, Y = `iteration-3/with-skill`. Preferred: **X** (iteration-2/baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (iteration-2/baseline) |  |  |  |  |  | 4 |  | 4 | 3 | 4 |  |  |  |  |
| Y (iteration-3/with-skill) |  |  |  |  |  | 4 |  | 3 | 3 | 5 |  |  |  |  |

X’s emerging letter, mint check badge, and soft shadow create a more polished, welcoming empty-state illustration. Y’s consistent outlines and simpler silhouette offer excellent restraint, but feel more like a generic status icon. Both show gentle vertical movement; the sampled frames provide limited evidence of distinctive timing or easing.
