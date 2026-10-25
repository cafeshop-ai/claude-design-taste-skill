# interface-design: a design-taste skill for Claude

A Claude skill for web design, UI design, and interaction design. It aims to give Claude judgment, not just rules: how to decide on a direction, build a token system, design every state, and critique its own output until it looks deliberate rather than generated.

## Install

The skill is the `interface-design/` folder. Copy it into your agent's skills directory:

```sh
git clone https://github.com/cafeshop-ai/claude-design-taste-skill
cp -r claude-design-taste-skill/interface-design ~/.claude/skills/    # Claude Code
cp -r claude-design-taste-skill/interface-design ~/.agents/skills/    # Codex and other Agent Skills hosts
```

Or per project, into `.claude/skills/` or `.agents/skills/` inside the repo. The skill triggers on its own whenever the agent builds, restyles, or reviews an interface.

## What's inside

Inside `interface-design/`:

| Path | What it is |
|---|---|
| `SKILL.md` | The stance, a six-step workflow, core principles, generic tells to avoid, and a pre-ship checklist |
| `references/` | 13 deep-dive guides, loaded only when a task needs them: typography, color, layout, components, interaction, motion, web design, accessibility, aesthetic directions, critique (with before → after redesigns), craft details, implementation (Tailwind v4/v3, shadcn/ui), and native platforms |
| `assets/tokens.css` | A starter design-token stylesheet: set a hue, a radius, and a density, and the palette, type, spacing, and light/dark themes follow (contrast-checked for every accent hue) |
| `assets/examples/` | Complete exemplar pages (a dense app screen, an editorial article) with their decisions explained |
| `assets/specimen.html` | A live specimen of the tokens with accent, neutral, radius, and theme controls. Open it in a browser |
| `scripts/color.py` | WCAG 2 + APCA contrast checks, gamut-mapped OKLCH ramps, hex ↔ OKLCH (standard-library Python) |
| `scripts/scale.py` | Modular and fluid `clamp()` type scales |

## How it works

Rules alone produce work that is correct but bland. So the skill pairs its principles with:

- **Decisions over defaults:** eight worked visual directions, each with a "signature element", so output doesn't fall back to the template look.
- **Worked redesigns** that explain *why* each change is better. Taste is easier to learn from judgment applied than from rules stated.
- **A render-and-critique loop:** look at the result at phone, tablet, and desktop widths, in dark mode, then critique it. Rendering catches what careful reading misses.

## The experiment

Can Claude teach another agent its design taste? [`experiments/`](experiments/README.md) runs the same design tasks through OpenAI's Codex with and without this skill, across web UI, interaction design, logo design, SVG animation, and content design. It audits the results automatically and has them judged blind. Every prompt, output, screenshot, score, and skill change is committed.

**Answer so far: partly, yes.** With the current skill, an independent blind judge (Codex itself) preferred the skill-guided work **12–2** on the cases the skill was refined against, and **8–2 on five unseen cases**:
- **Content:** the largest gain. No invented facts, half the words, task first.
- **Hierarchy, typography, color restraint:** clear gains.
- **Accessibility:** about 26 violations per page down to 2 (0 on unseen cases).
- **Logos:** better concepts, legible at 16px, with dark-background versions.

What doesn't transfer yet is visual personality, where the judge still rates baseline Codex more distinctive, and animation finesse. Details: [results](experiments/README.md) · [scoreboard](experiments/SCOREBOARD.md) · [gallery](experiments/GALLERY.md).
