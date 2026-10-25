# interface-design: a design-taste skill for Claude

A Claude skill for web design, UI design, and interaction design. It aims to give Claude judgment, not just rules: how to decide on a direction, build a token system, design every state, and critique its own output until it looks deliberate rather than generated.

## Install

Claude Code (personal, all projects):

```sh
git clone https://github.com/cafeshop-ai/claude-design-taste-skill ~/.claude/skills/interface-design
```

Or per project, clone into `.claude/skills/interface-design` inside the repo. The skill triggers on its own whenever Claude builds, restyles, or reviews an interface.

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | The stance, a six-step workflow, core principles, generic tells to avoid, and a pre-ship checklist |
| `references/` | 13 deep-dive guides, loaded only when a task needs them: typography, color, layout, components, interaction, motion, web design, accessibility, aesthetic directions, critique (with before → after redesigns), craft details, implementation (Tailwind v4/v3, shadcn/ui), and native platforms |
| `assets/tokens.css` | A starter design-token stylesheet: set a hue, a radius, and a density, and the palette, type, spacing, and light/dark themes follow (contrast-checked for every accent hue) |
| `assets/specimen.html` | A live specimen of the tokens with accent, neutral, radius, and theme controls. Open it in a browser |
| `scripts/color.py` | WCAG 2 + APCA contrast checks, gamut-mapped OKLCH ramps, hex ↔ OKLCH (standard-library Python) |
| `scripts/scale.py` | Modular and fluid `clamp()` type scales |

## How it works

Rules alone produce work that is correct but bland. So the skill pairs its principles with:

- **Decisions over defaults:** eight worked visual directions, each with a "signature element", so output doesn't fall back to the template look.
- **Worked redesigns** that explain *why* each change is better. Taste is easier to learn from judgment applied than from rules stated.
- **A render-and-critique loop:** look at the result at phone, tablet, and desktop widths, in dark mode, then critique it. Rendering catches what careful reading misses.
