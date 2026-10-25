# Experiment: can Claude teach another agent its design taste?

**Question.** If Claude writes down how it makes design decisions, as an [Agent Skill](https://agentskills.io) (`../interface-design/`), does a different agent that reads it produce better interfaces? "Better" here means the things a good designer would notice: clear hierarchy, considered type and color, restraint, real craft in the details, and content that says what's needed and nothing more.

**Scope.** Web UI design, interaction design, logo design, SVG animation, and content design. Content design gets particular attention because a common failure of coding agents is clutter: unrequested sections, filler copy, invented facts and testimonials, and decoration that adds noise.

**Status.** Five skill versions, six rounds (114 Codex design runs, about 160 blind judge calls), two judges. Results and every skill change are logged below, iteration by iteration; every blind comparison is in [`SCOREBOARD.md`](SCOREBOARD.md), and every output side by side in [`GALLERY.md`](GALLERY.md).

## Answer so far

**Partly, yes.** With the final skill (v4), an independent blind judge preferred Codex's work **12–2** on the cases the skill was refined against and **8–2 on five unseen cases**.

What transfers reliably, on tuned and unseen briefs alike:
- **Content discipline.** No invented facts (unsupplied claims went from 8 to 0), about half the words, specific copy, and single-purpose pages that put the task first. This was the largest gain: 2.7 → 3.9 tuned, 3.0 → 4.5 held-out.
- **Hierarchy, typography, and color restraint:** +0.3 to +1.1 points.
- **Accessibility and craft.** axe violations fell from about 26 to 2 per page (0 on the held-out set). Visible focus and reduced motion became the norm, and phone layouts keep the key information visible.
- **Logos:** concepts built from the name's letterform instead of the category cliché (a sail-shaped H, not a sailboat), legible at 16px, with dark-background versions.

What doesn't, yet:
- **Visual personality.** The independent judge rated baseline Codex more distinctive in every round (v4: 3.3 vs 3.8; held-out: 3.0 vs 4.0). Part of this is a real cost of restraint. Part is likely the judge, which is Codex, preferring its own house style; Claude's blind judgment in round 1 went the other way.
- **Illustration and animation finesse.** Through v4, animations didn't improve, and the held-out weather loaders lost to baseline. v5 fixed the loader guidance and won all 4 pairs on two new animation briefs. On the tuned case, though, the judge flip-flopped on illustration finish between rounds, so animation results are within noise at two pairs per comparison.

**What we learned about teaching taste:**
- **Bans backfire.** v2 told the agent to avoid its default palette, and it picked the next default, blue SaaS; v3 replaced the ban with "derive the palette from the product's world".
- **"Build only what was asked" gets read as "build the minimum".** v4 had to say depth within scope is good.
- **Agents that can't render need the rules spelled out.** Bugs only rendering reveals, like a hidden label widening a page on phones, must be written down as rules.
- **The examples in a skill must stay away from the test briefs.** We caught ourselves leaking test content three times.


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

### Held-out cases

Written after skill v4 was frozen, to test whether the gains generalize to briefs the skill was never tuned on. They run once, with the baseline and v4, and are never used to change the skill.

| Case | Area | Prompt (abridged) |
|---|---|---|
| `holdout-recipe-page` | Web UI, content | A recipe page for a food blog; the prompt supplies every ingredient and step |
| `holdout-water-app` | Interaction, mobile UI | The main screen of a phone app for tracking daily water intake |
| `holdout-closed-notice` | Content design | A bakery's "closed for renovations" page; the prompt supplies dates and a phone number |
| `holdout-logo` | Logo design | Logo and 16px icon for Halyard, a sailing school in Maine |
| `holdout-loader` | SVG animation | An animated loading indicator for a weather app |

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
3. **Independent blind judge** ([`harness/judge.py`](harness/judge.py)). The same blinded pairs and the same rubric, judged by Codex (`gpt-6.1-sol`) in a fresh read-only session per pair. It sees only the brief and the two screenshot sets, and is told it's comparing two designers. It's independent of the skill's author, but it may favor its own house style. From iteration 2 on, it's the primary blind measure (see "Blinding" below).
4. **Flow walkthrough** ([`harness/interact.mjs`](harness/interact.mjs)), for the booking and RSVP cases on a 390px screen. It presses the primary button with nothing filled in (are errors shown inline, by the browser's native bubble, or not at all?), then fills each step with plausible values and continues until a confirmation appears, screenshotting every step (`shots/flow-NN.jpg`). It's heuristic: it finds the forward button the way a person would (filled, not "Back", not an option chip) and ticks only required consent boxes.
5. **Skill usage.** From each run's event log: whether Codex opened `SKILL.md`, and which reference files it read.

Everything for a run is committed under `iteration-N/<case>/<condition>/run-K/`: the agent's output files, its final message, its event log, screenshots, `audit.json`, and `interaction.json` where relevant. Event logs keep the agent's messages, commands, and file changes, but raw command output is removed before publishing ([`harness/sanitize-events.py`](harness/sanitize-events.py)), because agents exploring the machine can list directories and environment variable names on the host.

## Blinding

Claude's iteration-1 judgments were blind except for one pair. After that, Claude had seen and unblinded the iteration-1 outputs, so any later comparison against them can't be blind for Claude. It also read the independent judge's notes on v2 before it could judge v2. So from iteration 2:
- Each iteration gets **fresh baseline runs** (iteration 2 reruns all 14), so baseline comparisons use outputs no judge has seen.
- **The independent Codex judge is the primary blind measure.** Every call is a fresh session, so it can't recognize anything.
- Claude's review of later iterations is reported as a **non-blind critique**, not as scores.

## Limitations

- **Small samples.** 7 cases × 2 runs per condition per iteration. Treat differences as directional unless they're large and consistent.
- **The judges have tastes.** Claude wrote the skill and prefers restraint; the Codex judge prefers visual richness and may favor its own house style. They agreed on 8 of 14 iteration-1 pairs. Both are reported, and all screenshots are committed so others can judge for themselves.
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

**Second opinion: the independent judge** ([`iteration-1/judgments-codex.md`](iteration-1/judgments-codex.md)) preferred with-skill **9**, baseline **5**. It agreed with Claude on 8 of 14 pairs. It saw the same gains in color (3.4 → 4.0), typography (3.5 → 4.0), and logo legibility at 16px (2.5 → 4.0). It saw only a small content gain (3.3 → 3.6) and no distinctiveness gain (3.6 both). Where the judges disagreed, the Codex judge rewarded richer identity (photos, illustrations, a dark "Pro" card, a literal book-and-leaf logo), while Claude rewarded restraint and penalized invented facts. The Codex judge also caught real flaws Claude underweighted: one with-skill RSVP page puts a tall photo before the form on phones, and one with-skill pricing page strands price units on their own lines on mobile.

**What the skill changed.** Accessibility most of all (contrast, focus, reduced motion), plus fewer generic tells, a tighter type scale, and much better logo concepts. The with-skill logos were letterform-and-leaf marks that survive 16px; the baselines were a fern growing out of an open book. Baseline Codex was already competent at mechanics: every flow worked and validated, and every SVG respected reduced motion.

**What it didn't fix.** In with-skill outputs:
1. **Filler copy:** paired slogans ("A little clean. A lot of calm."), cheerleading inside apps ("You're doing great"), and footer taglines. Content is still the lowest web score (3.2).
2. **Invented facts:** a price plus a payment-fee note on a landing page, a cancellation policy in a booking flow, and real companies (Linear, Notion) as sample invoice clients.
3. **Codex's house style survives:** italic-serif accent words in every headline, an eyebrow label over every heading, "Less admin. More climbing." headlines, sticker badges, and cream with forest green. Distinctiveness is 3.4. Both conditions even named the invoicing app "folio".
4. **Logos:** no version for dark backgrounds, and a tiny tagline inside the logo.
5. **Animation:** one with-skill animation barely moves.
6. **A dashboard table** that overflows on phones.

**Changes for iteration 2** (commit `008e1ca`):
- New references: `content-design.md` (scope, no invented facts, filler patterns, sample data), `logo-design.md`, and `svg-animation.md`, all written with briefs unrelated to the test cases.
- In `SKILL.md`: a core "Content" section, an updated list of generic tells (the house-style patterns above), a step to name your default look and then depart from it, and checklist items for invented facts, filler, dark-background logos, visible but small motion, and tables on phones.

### Iteration 2: skill v2 at `008e1ca`

With-skill runs on v2, compared against **14 fresh baseline runs**, plus a direct v1-vs-v2 comparison. Judged by the independent Codex judge, the primary blind measure from here on (see "Blinding"). Data: [`iteration-2/results-auto.md`](iteration-2/results-auto.md), [`iteration-2/judgments-codex.md`](iteration-2/judgments-codex.md) (v2 vs baseline), [`iteration-2/judgments-blind-v1-codex.md`](iteration-2/judgments-blind-v1-codex.md) (v1 vs v2).

**Routing worked.** The skill triggered in 14/14 runs. Each new reference was read exactly where it should be: `logo-design.md` by both logo runs, `svg-animation.md` by both animation runs, and `content-design.md` by all four landing and RSVP runs.

**v2 vs fresh baseline:** with-skill **8**, baseline **6**.

| Independent judge, mean (1–5) | baseline | v2 |
|---|---|---|
| Content | 2.8 | **4.0** |
| Distinctiveness | **3.9** | 2.8 |
| Color / typography / hierarchy / craft | 3.5 / 3.5 / 3.7 / 3.4 | 4.0 / 3.7 / 4.0 / 3.7 |
| Logo small-size legibility / versatility | 3.0 / 2.0 | 4.0 / 2.5 |

| Automated (10 web runs each) | baseline | v2 |
|---|---|---|
| axe violations, mean affected elements | 26.1 | 2.2 |
| Runs with zero axe violations | 0/10 | 7/10 |
| Visible words per page | 264 | 171 |
| Unsupplied claims ("10,000+", "4.9/5", "trusted by"…) | 8 | 0 |
| Emoji | 38 | 10 |
| Distinct font sizes per page | 15.0 | 10.4 |
| Horizontal overflow on a phone | 1/10 | 2/10 |

**v1 vs v2, head to head:** v1 **9**, v2 **4** (13 pairs; 10–3 before the logo-sheet fix described under "Held-out test"). Content rose (3.33 → 3.89), but distinctiveness fell from 4.00 to 2.67.

**What happened.** The content rules worked: pages got shorter (−35% words), stopped inventing prices, policies, and statistics, and got more focused on phones. But v2 also told the agent to name its default look (cream, forest green, an italic serif) and leave it. The agent dutifully avoided those and landed on the *next* default, generic blue SaaS. The judge's notes say it repeatedly: "blue accents and card treatment feel generic", "navy card and blue CTA … feel conventional". The pricing restyle even reverted the brand's headline to "Simple, transparent pricing." A ban without a positive source of direction just selects the runner-up default. And the house-style list penalized warmth that the judge read as coherent identity.

Two more findings:
- **Every with-skill phone overflow so far had the same cause.** A visually hidden `.sr-only` label inside a wide table is `position: absolute`. Its scroll wrapper wasn't positioned, so the label escaped the wrapper and widened the whole page. The skill's own accessibility advice produced the bug, and an agent that can't render will never see it. A fresh baseline dashboard overflowed too, by 318px, for a different reason.
- **Codex looks for a browser to render its work** (the skill's step 6) and finds none in this environment, so it can't catch visual bugs itself.

**Changes for iteration 3** (commit `bdd290b`):
- Replace the ban with a positive source: derive palette, type, and one signature element from three concrete things in the product's world, and name blue SaaS as a default too.
- Make "memorable somewhere" a requirement, with a checklist item.
- State that content discipline cuts words, claims, sections, and features, not identity ("cut the slogan, keep the illustration").
- Narrow the house-style tells to structural tics.
- Scroll wrappers need `position: relative`.

### Iteration 3: skill v3 at `bdd290b`

With-skill runs on v3, judged by the independent judge against the iteration-2 fresh baselines, v1, and v2. Data: [`iteration-3/results-auto.md`](iteration-3/results-auto.md); judgments [vs baseline](iteration-3/judgments-codex.md), [vs v1](iteration-3/judgments-blind-v1-codex.md), and [vs v2](iteration-3/judgments-blind-v2-codex.md).

| Independent judge | result |
|---|---|
| v3 vs fresh baseline | v3 **11**, baseline 3. The best result against baseline so far (v1 9–5, v2 8–6); 10–4 before the logo-sheet fix |
| v3 vs v2 | v3 **8**, v2 6. Distinctiveness recovers from 3.3 to 3.7 |
| v3 vs v1 | v1 **9**, v3 5. v1 still leads on identity (4.0 vs 2.8); v3 leads on content (3.8 vs 3.3); 10–4 before the logo-sheet fix |

| v3 vs baseline, mean (1–5) | baseline | v3 |
|---|---|---|
| Content | 2.7 | 3.8 |
| Typography / hierarchy / color | 3.2 / 3.6 / 3.5 | 4.0 / 4.0 / 4.0 |
| Craft | 3.4 | 3.4 |
| Distinctiveness | 4.0 | 3.2 |

Automated, 10 web runs each:
- axe violations fell from 26.1 to 3.4 affected elements per page.
- Words per page fell from 264 to 187.
- Invented claims went from 8 to 0, and emoji from 38 to 10.
- No invoice dashboard overflowed on a phone. The scroll-wrapper fix worked; the one overflow was a landing page, by 5px.

**What v3 fixed.** The palette swing is gone. v3 pages draw their palettes from the brief again (the forest green and cream came back where they fit), with v2's honesty intact: fictional sample clients, no invented prices or logos, and pages that tell you what saving actually does ("Save my RSVP · not sent to Sam & Priya").

**What still loses to v1, in the judge's words:**
1. **Mobile craft.** A fixed action bar "visibly cuts across the phone field". A dashboard table "crops amounts and leaves status and due date offscreen" on a phone (v1 had reflowed rows into stacked cards). On one landing page, icons and labels overlap on phones.
2. **Thinner content.** The v3 dashboards dropped v1's actionable overdue panel. "Build only what was asked" was read as "build the minimum", cutting depth *within* the requested jobs, not just breadth beyond them.
3. **Identity.** "Uniformly pale cards feel generic." v1's pages had illustrations and expressive serif type.

**A caution about the judge.** v1's look is close to Codex's own house style, and the judge is Codex. It scored the fresh baselines (pure house style) 4.0 on distinctiveness, the highest of any condition. Some of v1's identity lead may be the judge recognizing its own taste. Claude's non-blind read: the v3 pages are more honest and better organized than v1, a little plainer, and have real mobile bugs that v1 didn't.

**Changes for iteration 4:**
- Scope means building what was asked fully: depth on the requested jobs, cuts only to breadth and padding.
- Phone tables keep their key fields visible as stacked rows.
- Fixed bars reserve their own space.
- A page made only of type and pale cards counts as under-designed.
- A restyle replaces a generic line with a specific one instead of deleting the voice.

### Iteration 4: skill v4 at `6e3c38e`

Data: [`iteration-4/results-auto.md`](iteration-4/results-auto.md); independent judgments [vs baseline](iteration-4/judgments-codex.md), [vs v1](iteration-4/judgments-blind-v1-codex.md), and [vs v3](iteration-4/judgments-blind-v3-codex.md). Every comparison so far is in [`SCOREBOARD.md`](SCOREBOARD.md).

| Independent judge | result | where the gain came from |
|---|---|---|
| v4 vs fresh baseline | v4 **12**, baseline 2 | Content 2.7 → 3.9, craft 3.5 → 4.0, typography 3.4 → 4.0. Distinctiveness 3.8 → 3.3, a narrower gap than v2 and v3 |
| v4 vs v1 | **7–7** | v4 leads on content (4.0 vs 3.1) and craft (4.0 vs 3.7); v1 on distinctiveness (4.0 vs 3.1) |
| v4 vs v3 | v4 **9**, v3 5 | Craft 3.2 → 3.9: the phone fixes landed |

Automated, 10 web runs each:
- axe violations fell from 26.1 to 2.4 affected elements per page, with zero violations in 7/10 runs.
- No phone overflow in any run (baseline: 1/10).
- Words per page fell from 264 to 170, and invented claims went from 8 to 0.

The dashboards' phone layouts now show stacked invoice cards with client, amount, status and due date visible. That's the decisive point in both invoice pairs ("X's clipped table hides essential information").

**Remaining gaps.** The independent judge still rates baseline identity higher. v1 keeps winning on identity in the pricing restyles and on illustration finish in both animations: v1's soft fills and grounding shadow beat v4's bolder, plainer line art, which follows the skill's "few shapes, no shadows unless the product uses them" too literally. Some of the identity gap may be the judge's preference for its own house style (see iteration 3). The judge shows no position bias: across 83 judgments it picked X 46% of the time.

**Next: generalization.** Rather than keep tuning against the same 7 cases and one judge's taste, the next step tests v4 on **5 held-out cases** it was never tuned on, one per scope area.

### Held-out test: skill v4 on 5 unseen cases

Five new briefs, written after v4 was frozen, run with the baseline and v4 (2 runs each), and judged blind by the independent judge. Data: [`iteration-holdout/results-auto.md`](iteration-holdout/results-auto.md), [`iteration-holdout/judgments-codex.md`](iteration-holdout/judgments-codex.md).

**v4 vs baseline on unseen briefs:** v4 **8**, baseline 2.

| Independent judge, mean (1–5) | baseline | v4 |
|---|---|---|
| Content | 3.0 | **4.5** |
| Hierarchy | 3.2 | **4.3** |
| Typography / color / craft | 3.3 / 3.7 / 3.4 | 4.0 / 4.0 / 4.0 |
| Distinctiveness | **4.0** | 3.0 |
| Logo concept / versatility | 3.5 / 2.0 | 4.0 / 3.0 |
| Loader motion quality | **4.0** | 3.0 |

| Automated (6 web runs each) | baseline | v4 |
|---|---|---|
| axe violations, mean affected elements | 14.8 | **0** (6/6 clean) |
| Motion that respects reduced motion | 3/5 | 6/6 |
| Visible words per page | 166 | 82 |
| Emoji | 6 | 0 |
| Distinct font sizes per page | 11.8 | 7.5 |

The judge's notes follow one pattern on every web pair: v4 makes the essential thing clear and usable, while the baseline "has more personality":
- The bakery notice "makes *Closed for renovations*, the dates, and the phone action immediately clear", whereas the baseline's storefront illustration "pushes the essentials" down.
- The water tracker makes intake, goal, and "Add 250 ml" immediately legible, against the baseline's "large motivational headline and tiny, faint supporting text".
- The recipe pages get larger step text and "Jump to recipe" navigation.
- Both v4 logos built the H into a sail and shipped a reversed version; both baselines drew a sailboat.

**Where the baseline won: both loaders.** v4's loaders were "exceptionally restrained", with motion confined to sun rays, while the baselines' bobbing clouds and dots read clearly as "loading". The skill's animation reference was written around ambient empty-state art ("rest in the cycle", "consider stopping"); a loader is different, because its motion is the message. This is a finding for the next version, not something to tune against the held-out set.

**Correction: logo sheets.** Every with-skill logo from v2 on shipped a dark-background version (`logo-reversed.svg`); no baseline did. The presentation sheet, though, always showed the main `logo.svg` on the dark panel, so the judge scored "versatility" against artwork never meant for dark backgrounds. The sheet now uses the designer's dark version when one exists (captioned with its file name). All logo pairs in iterations 2–4 were re-judged in place under their original blind mappings, and the tallies above are corrected; the original judgments are in git history. Versatility for with-skill logos rose from 2.0–2.5 to 3–4, against 2 for baseline.

### Iteration 5: skill v5 at `3a1bd7f` (animation only)

The held-out loaders were the one case the baseline won, for a clear design reason: the animation reference was written around ambient empty-state art, and a loader is different. v5 changes only the animation guidance:
- Loaders and progress indicators are their own kind of motion: continuous, perceptible, 0.8–1.6s cycles, no rest phase, paired with text.
- "Rest in the cycle" and "consider stopping" are scoped to ambient art.
- Spot illustrations get finish from soft, flat tints (a pale fill, a backdrop disc, a ground-shadow ellipse) instead of bare outlines.

The weather loader informed this fix, so it can't test it. v5 was therefore tested on the tuned animation case and on **two new held-out animation briefs**: a podcast buffering loader and a one-shot "payment sent" moment in a banking app, with fresh baselines. Data: [`iteration-5/`](iteration-5/).

| Independent judge (animation pairs) | result |
|---|---|
| New held-out briefs: v5 vs baseline | v5 **4**, baseline 0. Buffering bars read as "a gentle traveling waveform … a clearer sense of ongoing activity"; payment animations are "more specific than a generic checkmark" (a banknote or receipt with a confirmation badge) |
| Tuned case: v5 vs baseline | v5 **2**, baseline 0 |
| Tuned case: v5 vs v1 | 1–1 |
| Tuned case: v5 vs v4 | v4 **2**, v5 0. "Background circle, ground shadow, and layered fills add some unnecessary decoration" |

The v5-vs-v4 result contradicts iteration 4, where the same judge preferred v1's "soft grounding shadow, pale circular backdrop" over v4's plain line art. With two pairs per comparison, animation preferences are within judge noise. What does hold: the loader guidance produced loaders that read as loading, and on all four new animation briefs the skill-guided version won.
