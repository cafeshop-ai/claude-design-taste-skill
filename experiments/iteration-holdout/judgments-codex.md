# Blind judgments: iteration-holdout, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **baseline**: 2
- **with-skill**: 8

## Mean scores

| condition | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 3.67 | 3.50 | 3.00 | 3.38 | 4.00 | 4.00 | 3.17 | 4.00 | 4.00 | 4.00 | 4.00 | 3.50 | 3.33 | 2.00 |
| with-skill | 4.00 | 4.00 | 4.50 | 4.00 | 3.00 | 3.50 | 4.33 | 4.00 | 3.00 | 4.50 | 4.50 | 3.50 | 4.00 | 3.00 |

## Pairs

### holdout-closed-notice-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 5 | 4 | 3 |  | 5 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |

X makes “Closed for renovations,” the dates, and the phone action immediately clear, with a focused layout that works well on mobile. Y’s storefront illustration and green palette give it more personality, but its generic headline and extra copy push the essential dates and catering contact much farther down the phone page. X better serves the brief’s simple, practical purpose.

### holdout-closed-notice-run-2

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 4 |  | 3 | 4 | 4 |  | 3 |  |  |  |  |  | 4 |  |
| Y (with-skill) | 4 |  | 5 | 4 | 3 |  | 5 |  |  |  |  |  | 4 |  |

Y makes “Closed for renovations” unmistakable, with the dates, reopening information, and catering phone action easy to scan. Its mobile layout keeps the complete notice within one screen, while X’s large storefront illustration pushes catering further down. X has a warmer, more distinctive identity, but its poetic headline and extra copy dilute the simple announcement.

### holdout-loader-run-1

X = `with-skill`, Y = `baseline`. Preferred: **Y** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  |  |  |  |  | 4 |  | 4 | 3 | 5 |  |  |  |  |
| Y (baseline) |  |  |  |  |  | 4 |  | 4 | 4 | 4 |  |  |  |  |

Y’s changing raindrop positions and opacity provide a clearer loading signal while keeping the illustration calm and compact. Its soft blue-gray outlines and warm yellow sun feel cohesive. X is exceptionally restrained, but the changing sun rays around an otherwise nearly static cloud make its activity less apparent.

### holdout-loader-run-2

X = `baseline`, Y = `with-skill`. Preferred: **X** (baseline).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) |  |  |  |  |  | 4 |  | 4 | 4 | 4 |  |  |  |  |
| Y (with-skill) |  |  |  |  |  | 3 |  | 4 | 3 | 4 |  |  |  |  |

X’s subtle cloud bob and changing three-dot emphasis communicate loading gently and clearly. Y has clean curves and stronger contrast, but its heavier outlines and prominent sun feel more like a weather condition icon, with motion concentrated in the rays. X better suits the waiting moment, although its pale blue details could be more legible.

### holdout-logo-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 5 | 4 |  | 3 |
| Y (baseline) |  | 3 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 2 |

X’s curved H combines the initial with a sail-like form, giving Halyard a more distinctive identity than Y’s familiar sailboat. Its single silhouette holds together better at favicon size, while Y’s mast and gaps become fragile. Both have clean curves and confident serif typography, but X supplies a readable reversed full logo; Y’s dark wordmark nearly disappears, and both candidates’ dark-panel icons lack contrast.

### holdout-logo-run-2

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) |  | 4 |  | 3 |  |  |  |  |  |  | 4 | 4 |  | 2 |
| Y (with-skill) |  | 4 |  | 4 |  |  |  |  |  |  | 4 | 3 |  | 3 |

Y’s sail-like diagonal integrated into the H and refined serif wordmark make a more distinctive, cohesive identity. X’s pennant contains a clearer H at favicon sizes, but its dark wordmark nearly disappears against black. Y supplies an effective reversed full logo, although its green standalone mark also loses contrast on dark backgrounds and can resemble an N when small.

### holdout-recipe-page-run-1

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (with-skill) | 4 |  | 5 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |
| Y (baseline) | 4 |  | 3 | 4 | 4 |  | 4 |  |  |  |  |  | 3 |  |

X makes the recipe easier to use through larger instruction text, clear step dividers, and direct Ingredients/Method navigation. Y has a more distinctive identity through its green display typography and editorial details, but its small supporting text compromises phone readability. Repeated slogans, the decorative badge, and the kitchen attribution also add clutter beyond the brief.

### holdout-recipe-page-run-2

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 4 |  | 3 | 3 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y offers clearer recipe navigation through its “Jump to recipe” action, shaded ingredients panel, and direct method headings, with more readable typography on mobile. X has more personality through its sun motifs and editorial details, but its oversized mobile title, small secondary text, and awkwardly wrapped difficulty label weaken usability. Y also stays closer to the brief, while X adds several slogans and conversational asides that compete with the cooking instructions.

### holdout-water-app-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 3 |  | 3 | 3 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y makes daily intake, the goal, and the “Add 250 ml” action immediately legible, with a clear drink history below. X has more personality through its coral palette and wave-filled progress ring, but its large motivational headline and tiny, faint supporting text weaken scanning. Y also handles spacing more consistently; X’s bottom navigation crowds and partially obscures the history on desktop.

### holdout-water-app-run-2

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | color | concept | content | craft | distinctiveness | fit for context | hierarchy | illustration craft | motion quality | restraint | simplicity | small-size legibility | typography | versatility |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| X (baseline) | 3 |  | 3 | 2 | 4 |  | 3 |  |  |  |  |  | 3 |  |
| Y (with-skill) | 4 |  | 4 | 4 | 3 |  | 4 |  |  |  |  |  | 4 |  |

Y makes progress easier to read with a larger water vessel, stronger text contrast, and a clear sequence from amount selection to the Add water button and drink history. X has more personality through its ripple branding and illustrated progress ring, but small, faint labels and motivational copy dilute the hierarchy. X’s navigation also interrupts the history section, especially on desktop, while Y presents three neatly aligned entries across both widths.
