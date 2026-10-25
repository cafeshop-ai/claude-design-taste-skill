# interface-design: a design-taste skill for Claude

A Claude skill for web design, UI design, and interaction design. It aims to give Claude judgment, not just rules: how to decide on a direction, build a token system, design every state, and critique its own output until it looks deliberate rather than generated.

## Install

### Claude Code

From a Claude Code session (2.1.275 or later), in one step:

```
/plugin install interface-design --marketplace cafeshop-ai/claude-design-taste-skill
```

Or add the marketplace once, then install, which works on any version with plugins:

```
/plugin marketplace add cafeshop-ai/claude-design-taste-skill
/plugin install interface-design@design-taste
```

The same commands work in your shell as `claude plugin marketplace add …` and `claude plugin install …`. Installed as a plugin, the skill updates with `/plugin update`, and its slash command is `/interface-design:interface-design`; it also triggers on its own for design work.

This repository also holds the experiment's data (about 35 MB of screenshots). To fetch only the skill when adding the marketplace, use a sparse checkout:

```
claude plugin marketplace add cafeshop-ai/claude-design-taste-skill --sparse .claude-plugin interface-design
```

### Claude.ai and the Claude desktop app

1. Download [`interface-design.zip`](https://github.com/cafeshop-ai/claude-design-taste-skill/releases/latest/download/interface-design.zip) from the latest release.
2. In Claude, open **Customize → Skills**, click **+**, choose **Create skill → Upload a skill**, and upload the ZIP.

Skills need code execution ("Create and edit files" under Settings → Capabilities). On Team and Enterprise plans, an owner may need to allow custom skills.

### Codex

With one command:

```sh
curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh -s -- --codex
```

Or ask Codex to use its built-in installer: *"Use $skill-installer to install https://github.com/cafeshop-ai/claude-design-taste-skill/tree/main/interface-design"*. Either way, restart Codex to pick up the skill.

### Any agent that reads skill folders

The installer downloads only the skill (about 100 KB) from the latest release:

```sh
curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh                        # ~/.claude/skills
curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh -s -- --agents        # ~/.agents/skills
curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh -s -- --dir PATH      # PATH/interface-design
```

Add `--force` to update an existing install, or `--version v5.0.0` to pin a release. To do it by hand, unzip [`interface-design.zip`](https://github.com/cafeshop-ai/claude-design-taste-skill/releases/latest/download/interface-design.zip) into your agent's skills folder.

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

What doesn't transfer yet is visual personality: the judge still rates baseline Codex more distinctive. Animation is mixed. v5's loader guidance won all 4 pairs on new animation briefs, but finer illustration judgments are within noise. Details: [results](experiments/README.md) · [scoreboard](experiments/SCOREBOARD.md) · [gallery](experiments/GALLERY.md).
