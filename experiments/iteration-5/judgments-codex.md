# Blind judgments: iteration-5, judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-5/with-skill**: 2

## Mean scores

| condition | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| iteration-2/baseline | 4.00 | 4.00 | 3.50 | 4.00 |
| iteration-5/with-skill | 5.00 | 4.00 | 3.50 | 5.00 |

## Pairs

### svg-animation-run-1

X = `iteration-5/with-skill`, Y = `iteration-2/baseline`. Preferred: **X** (iteration-5/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-5/with-skill) | 5 | 4 | 3 | 5 |
| Y (iteration-2/baseline) | 4 | 4 | 3 | 4 |

X’s closed envelope and prominent green check communicate completion clearly, with a restrained palette and readable strokes. Y’s open letter adds detail, but its pale lavender lines and surrounding sparkles feel fussier at this size. Both show subtle vertical movement across the sampled frames; the motion looks calm, though neither demonstrates especially distinctive timing or easing.

### svg-animation-run-2

X = `iteration-2/baseline`, Y = `iteration-5/with-skill`. Preferred: **Y** (iteration-5/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-2/baseline) | 4 | 4 | 4 | 4 |
| Y (iteration-5/with-skill) | 5 | 4 | 4 | 5 |

Y’s simple envelope and solid green check communicate completion clearly at a small size, with fewer competing details. X’s lavender palette is pleasant, but the protruding letter, sparkles, and outlined badge make it slightly busier and less legible. Both show a restrained vertical float across the sampled frames; Y’s quieter composition better suits a recurring email empty state.
