# Blind judgments: iteration-5 (blind-v4), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **iteration-4/with-skill**: 2

## Mean scores

| condition | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| iteration-4/with-skill | 4.00 | 4.00 | 3.00 | 5.00 |
| iteration-5/with-skill | 4.00 | 4.00 | 3.00 | 4.00 |

## Pairs

### svg-animation-run-1

X = `iteration-5/with-skill`, Y = `iteration-4/with-skill`. Preferred: **Y** (iteration-4/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-5/with-skill) | 4 | 4 | 3 | 4 |
| Y (iteration-4/with-skill) | 4 | 4 | 3 | 5 |

Y’s simpler envelope and solid green check badge communicate completion clearly at a small size. X’s background circle, ground shadow, and layered fills add some unnecessary decoration. Both show only a slight vertical bob across the sampled frames, with no decisive motion advantage.

### svg-animation-run-2

X = `iteration-4/with-skill`, Y = `iteration-5/with-skill`. Preferred: **X** (iteration-4/with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (iteration-4/with-skill) | 4 | 4 | 3 | 5 |
| Y (iteration-5/with-skill) | 4 | 4 | 3 | 4 |

X’s simple envelope and clearly separated lower-right check badge communicate completion with excellent restraint. Y’s pale circle, ground shadow, and additional envelope seams make a polished illustration, but add visual weight to a small empty state. Both show a restrained vertical bob across the sampled frames; neither demonstrates notably richer motion.
