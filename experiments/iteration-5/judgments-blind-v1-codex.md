# Blind judgments: iteration-5 (blind-v1), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-1/with-skill**: 1
- **iteration-5/with-skill**: 1

## Mean scores

| condition | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| iteration-1/with-skill | 4.00 | 3.50 | 3.00 | 4.00 |
| iteration-5/with-skill | 4.00 | 4.00 | 3.50 | 4.00 |

## Pairs

### svg-animation-run-1

X = `iteration-5/with-skill`, Y = `iteration-1/with-skill`. Preferred: **Y** (iteration-1/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-5/with-skill) | 4 | 4 | 3 | 4 |
| Y (iteration-1/with-skill) | 4 | 4 | 3 | 4 |

Y narrowly wins: the checked letter inside the open envelope forms a cohesive, readable completion symbol. X is also polished, but its circular backdrop and overlapping check badge add slightly more visual furniture. Both show a very subtle vertical bob; the sampled frames provide limited evidence of timing, easing, or loop continuity.

### svg-animation-run-2

X = `iteration-1/with-skill`, Y = `iteration-5/with-skill`. Preferred: **Y** (iteration-5/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-1/with-skill) | 4 | 3 | 3 | 4 |
| Y (iteration-5/with-skill) | 4 | 4 | 4 | 4 |

Y’s darker, consistent envelope outlines and larger check badge remain legible at a small size; X’s pale, fine strokes feel washed out. Y’s gentle vertical bob is more apparent across the frames while remaining calm. Both use a restrained green palette and communicate completion clearly.
