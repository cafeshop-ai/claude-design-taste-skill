# Blind judgments: iteration-5 (blind-holdout2), judge codex

Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after all judgments below were written. Scores are 1–5. Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style. The screenshots are in each run's `shots/` folder for anyone to check.

## Preferences

- **with-skill**: 4

## Mean scores

| condition | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| baseline | 3.50 | 3.75 | 3.25 | 3.75 |
| with-skill | 4.00 | 4.00 | 3.50 | 4.00 |

## Pairs

### holdout2-buffering-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (baseline) | 4 | 4 | 3 | 4 |
| Y (with-skill) | 4 | 4 | 4 | 4 |

Y’s staggered bar heights suggest a gentle traveling waveform, giving the buffering state a clearer sense of ongoing activity. X’s more symmetrical expansion and changing purple intensity feel slightly more attention-seeking. Both use clean, consistently rounded bars that suit a podcast app.

### holdout2-buffering-run-2

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (baseline) | 4 | 4 | 4 | 3 |
| Y (with-skill) | 4 | 4 | 4 | 4 |

Y’s teal bars maintain a smaller height range, making the visible wave progression feel calmer during buffering. X’s taller purple peaks and stronger changes in emphasis attract more attention. Both use clean, evenly spaced bars that clearly connect to the podcast context, but Y better balances activity with restraint.

### holdout2-payment-sent-run-1

X = `baseline`, Y = `with-skill`. Preferred: **Y** (with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (baseline) | 3 | 3 | 3 | 4 |
| Y (with-skill) | 4 | 4 | 3 | 4 |

Y keeps the banknote visible and adds a compact confirmation badge, making the completed payment more specific than X’s generic checkmark. Its consistent green linework feels more cohesive than X’s transition from a tiny shaded gold coin to a large green disc. Both settle quickly into a calm hold; the sampled frames provide limited evidence of easing or transition smoothness.

### holdout2-payment-sent-run-2

X = `with-skill`, Y = `baseline`. Preferred: **X** (with-skill).

| | fit for context | illustration craft | motion quality | restraint |
|---|---|---|---|---|
| X (with-skill) | 4 | 4 | 3 | 4 |
| Y (baseline) | 3 | 4 | 3 | 4 |

X’s receipt, outbound arrow, and green confirmation badge communicate a completed payment more specifically than Y’s generic success circle. Y’s arrow-to-check transition is clear and economical, though its expanding halo adds a little decoration. Both settle quickly and remain still in the later frames, appropriate for the requested one-time confirmation; the sampling provides limited evidence of easing.
