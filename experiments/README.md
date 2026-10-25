# Experiment: can Claude teach another agent its design taste?

**Question.** If Claude writes down how it makes design decisions, as an [Agent Skill](https://agentskills.io) (`../interface-design/`), does a different agent that reads it produce better interfaces? "Better" here means the things a good designer would notice: clear hierarchy, considered type and color, restraint, real craft in the details, and content that says what's needed and nothing more.

**Scope.** Web UI design, interaction design, logo design, SVG animation, and content design. Content design gets particular attention because a common failure of coding agents is clutter: unrequested sections, filler copy, invented facts and testimonials, and decoration that adds noise.

**Status.** Running. Results and every skill change are logged below, iteration by iteration.

## Setup

| | |
|---|---|
| Agent under test | OpenAI Codex CLI 0.159.2, `codex exec`, model `gpt-6.1-sol`, reasoning effort high |
| Conditions | **baseline**: vanilla Codex. **with-skill**: the same, with the skill installed at `.agents/skills/interface-design` in the workspace, exported from a specific commit |
| Isolation | Each run gets its own empty workspace outside this repo, containing only the case's input files. `--ignore-user-config` drops personal config, plugins, and hooks. Codex's built-in system skills and the machine's two unrelated user skills are present in both conditions |
| Triggering | Prompts never mention the skill. Codex has to decide to use it from its description, as it would in real use |
| Runs | 2 per case per condition per iteration. Baseline runs are reused across iterations; only the with-skill condition reruns when the skill changes |
| Sandbox | `workspace-write`, approvals off. Codex can run commands but can't write outside its workspace |

The runner is [`harness/run.sh`](harness/run.sh) (one trial) and [`harness/run-iteration.sh`](harness/run-iteration.sh) (all trials, in parallel).

## Cases

| Case | Area | Prompt (abridged; full text in `cases/<case>/prompt.md`) | What separates good from generic |
|---|---|---|---|
| `landing-page` | Web UI, content | Landing page for Tidepool, software for small climbing gyms | A clear point of view about the product, real product UI instead of decoration, no invented stats or testimonials |
| `invoice-dashboard` | Web UI (app) | Main screen of an invoicing app for freelancers | Hierarchy of numbers, density, tabular figures, restrained status color |
| `booking-flow` | Interaction | Multi-step home-cleaning booking flow that works on phones | Step structure, validation, touch targets, states, mobile layout |
| `pricing-restyle` | Critique | "Our pricing page looks amateurish. Make it professional." (input: [`cases/pricing-restyle/files/index.html`](cases/pricing-restyle/files/index.html)) | Diagnosing the real problems (gradients, emoji, Title Case, contrast, a mobile overflow bug) and fixing them without adding new ones |
| `logo` | Logo design | Logo for Fernway, a bookshop and café, plus an icon that works as a 16px favicon | A concept, simple geometry, legibility at 16px, works on dark |
| `svg-animation` | SVG animation | A gently looping "you're all caught up" empty-state animation | Restraint, easing and timing, a seamless loop, honoring reduced motion |
| `rsvp-page` | Content design | Wedding RSVP page; the prompt supplies every fact | Building only what was asked; no invented schedule, dress code, hotels, or countdowns |

## Measurements

1. **Automated audit** ([`harness/audit.mjs`](harness/audit.mjs) for pages, [`harness/audit-svg.mjs`](harness/audit-svg.mjs) for SVG deliverables). Rendered in headless Chromium at 1440px (light and dark) and 390px:
   - accessibility violations from axe-core (WCAG 2.2 AA rules)
   - horizontal overflow on a phone, console errors
   - dark-mode support, visible keyboard focus, reduced-motion handling
   - generic tells: gradient text, emoji, buzzwords, a violet-dominant palette, centered paragraphs, Title Case
   - system consistency: the number of distinct font sizes and families
   - content volume: words, sections, unsupplied claims ("10,000+ gyms", "4.9/5", "trusted by"), testimonial blocks
   - SVGs: size, element and color counts, text dependencies, animation technique, and whether motion stops under `prefers-reduced-motion`

   These are proxies. They catch failures; they can't recognize quality.
2. **Blind pairwise judgment** ([`harness/blind.py`](harness/blind.py)). For each case and run, the baseline and with-skill screenshots are shown as X and Y in random order. Each is scored 1–5 on hierarchy, typography, color, content, craft, and distinctiveness, and one is preferred. Logos and animations use their own criteria: concept, simplicity, small-size legibility and craft for logos; restraint, motion quality and craft for animation. The mapping is opened only after all judgments are written, then [`blind.py reveal`](harness/blind.py) produces `judgments.md`.
3. **Flow walkthrough** ([`harness/interact.mjs`](harness/interact.mjs)), for the booking and RSVP cases on a 390px screen. It presses the primary button with nothing filled in (are errors shown inline, by the browser's native bubble, or not at all?), then fills each step with plausible values and continues until a confirmation appears, screenshotting every step (`shots/flow-NN.jpg`). It's heuristic: it finds the forward button the way a person would (filled, not "Back", not an option chip) and ticks only required consent boxes.
4. **Skill usage.** From each run's event log: whether Codex opened `SKILL.md`, and which reference files it read.

Everything for a run is committed under `iteration-N/<case>/<condition>/run-K/`: the agent's output files, its final message, its event log, screenshots, `audit.json`, and `interaction.json` where relevant. Event logs keep the agent's messages, commands, and file changes, but raw command output is removed before publishing ([`harness/sanitize-events.py`](harness/sanitize-events.py)), because agents exploring the machine can list directories and environment variable names on the host.

## Limitations

- **Small samples.** 7 cases × 2 runs per condition per iteration. Treat differences as directional unless they're large and consistent.
- **The judge is interested.** Claude wrote the skill and judges the pairs. Blinding helps, but a skill that shapes style can make outputs recognizable. All screenshots are committed so others can judge for themselves.
- **One agent, one model.** Results say something about Codex with `gpt-6.1-sol`, not about every agent.
- **No teaching to the test.** Skill changes must not use the test briefs (Tidepool, Fernway, the RSVP, the caught-up animation, and so on) as examples; new references use unrelated briefs (a neighborhood clean-up sign-up, a coffee roaster called Millrace, a sync-complete animation). Some generic overlap predates the cases: the skill's specimen has an invoice table, and its empty-state guidance mentions "You're all caught up" as sample copy.
- **First screen only.** Screenshots show each page's initial state. Interactions (later steps of the booking flow, dialogs, hover) are covered by the audit and the code, not the pictures.

## Reproduce

```sh
cd experiments/harness && npm install          # Playwright + axe-core; needs Chromium for Playwright 1.48
export CODEX_BASE_URL=...                       # optional: an OpenAI-compatible Responses endpoint
./run-iteration.sh 1 <skill-commit> 2 7         # iteration, skill ref, runs per cell, parallelism
for d in ../iteration-1/*/*/run-*; do           # audit every run
  case $d in */logo/*) node audit-svg.mjs $d logo;; */svg-animation/*) node audit-svg.mjs $d svg-animation;; *) node audit.mjs $d;; esac
done
python3 summarize.py ../iteration-1             # -> iteration-1/results-auto.md
python3 blind.py make ../iteration-1            # judge blind/, write blind/judgments.json, then:
python3 blind.py reveal ../iteration-1          # -> iteration-1/judgments.md
```

## Log

### Iteration 1: skill at `0b52da1`

The skill as first written, plus two exemplar pages. It barely covered logos, SVG animation, or scope discipline. Full data: [`iteration-1/results-auto.md`](iteration-1/results-auto.md) (automated) and [`iteration-1/judgments.md`](iteration-1/judgments.md) (blind).

**Did the skill trigger?** Yes, in 14/14 with-skill runs, from its description alone. Codex read `SKILL.md`, then usually 1–3 references that matched the task (aesthetic directions, web design, critique, interaction, motion).

**Blind preference:** with-skill **12**, tie 2, baseline 0. One pair (`logo-run-1`) wasn't blind: the judge had seen the baseline logo while testing the audit script.

| Mean blind score (1–5) | baseline | with-skill |
|---|---|---|
| Hierarchy | 3.7 | 4.0 |
| Typography | 3.4 | 4.0 |
| Color | 3.5 | 4.0 |
| Content | 2.3 | 3.2 |
| Craft | 3.7 | 3.8 |
| Distinctiveness | 2.9 | 3.4 |
| Logo concept / small-size legibility | 2.5 / 2.5 | 4.0 / 4.0 |
| Logo versatility (works on dark) | 2.0 | 2.0 |
| Animation motion quality | 3.0 | 3.0 |

| Automated (10 web runs per condition) | baseline | with-skill |
|---|---|---|
| axe-core violations, mean affected elements | 33.9 | 5.3 |
| Runs with zero axe violations | 0/10 | 6/10 |
| Every tab stop shows focus | 9/10 | 10/10 |
| Motion that respects reduced motion | 8/10 | 6/6 |
| Emoji / buzzwords / violet palettes | 42 / 3 / 1 | 20 / 0 / 0 |
| Distinct font sizes per page | 15.6 | 12.9 |
| Visible words per page | 290 | 274 |
| Horizontal overflow on a phone | 0/10 | 1/10 |
| RSVP empty-submit feedback | native browser bubble (2/2) | inline errors (2/2) |
| Booking flows completed by the walkthrough | 2/2 | 2/2 |

**What the skill changed.** Accessibility most of all (contrast, focus, reduced motion), plus fewer generic tells, a tighter type scale, and much better logo concepts. The with-skill logos were letterform-and-leaf marks that survive 16px; the baselines were a fern growing out of an open book. Baseline Codex was already competent at mechanics: every flow worked and validated, and every SVG respected reduced motion.

**What it didn't fix.** In with-skill outputs:
1. **Filler copy:** paired slogans ("A little clean. A lot of calm."), cheerleading inside apps ("You're doing great"), and footer taglines. Content is still the lowest web score (3.2).
2. **Invented facts:** a price plus a payment-fee note on a landing page, a cancellation policy in a booking flow, and real companies (Linear, Notion) as sample invoice clients.
3. **Codex's house style survives:** italic-serif accent words in every headline, an eyebrow label over every heading, "Less admin. More climbing." headlines, sticker badges, and cream with forest green. Distinctiveness is 3.4. Both conditions even named the invoicing app "folio".
4. **Logos:** no version for dark backgrounds, and a tiny tagline inside the logo.
5. **Animation:** one with-skill animation barely moves.
6. **A dashboard table** that overflows on phones.

**Changes for iteration 2.** Commit `see below`:
- New references: `content-design.md` (scope, no invented facts, filler patterns, sample data), `logo-design.md`, and `svg-animation.md`, all written with briefs unrelated to the test cases.
- In `SKILL.md`: a core "Content" section, an updated list of generic tells (the house-style patterns above), a step to name your default look and then depart from it, and checklist items for invented facts, filler, dark-background logos, visible but small motion, and tables on phones.
