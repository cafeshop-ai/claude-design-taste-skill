#!/usr/bin/env python3
"""Write experiments/GALLERY.md: every case, baseline next to each skill version.

    python3 gallery.py

Columns come from what exists: baseline (iteration 1 and 2 runs), v1
(iteration-1 with-skill), v2 (iteration-2), v3 (iteration-3), and so on.
GitHub renders the Markdown with the screenshots inline.
"""
from pathlib import Path

EXP = Path(__file__).resolve().parent.parent
SHOT = {"logo": "sheet.jpg", "svg-animation": "filmstrip.jpg"}


def columns():
    cols = []
    for it in sorted(EXP.glob("iteration-*"), key=lambda p: int(p.name.split("-")[1])):
        n = it.name.split("-")[1]
        if (it / "landing-page" / "baseline").exists():
            cols.append((f"baseline (iteration {n})", it.name, "baseline"))
        if (it / "landing-page" / "with-skill").exists():
            cols.append((f"skill v{n}", it.name, "with-skill"))
    return cols


def main():
    cols = columns()
    cases = sorted(p.name for p in (EXP / "cases").iterdir())
    md = ["# Gallery",
          "",
          "Every case, side by side: vanilla Codex (baseline) and Codex with each version of the skill. "
          "Run 1 is shown; run 2 is linked. Desktop screenshots at 1440px, full page; click through for phone (390px) "
          "and dark-mode shots, the agent's files, and its final message. Logos show a presentation sheet; animations a "
          "10-frame filmstrip. See [README.md](README.md) for method and results.",
          ""]
    for case in cases:
        prompt = (EXP / "cases" / case / "prompt.md").read_text().strip()
        md += [f"## {case}", "", f"> {prompt}", ""]
        shot = SHOT.get(case, "desktop-light.jpg")
        md.append("| " + " | ".join(c[0] for c in cols) + " |")
        md.append("|" + "---|" * len(cols))
        cells = []
        for _, it, cond in cols:
            run1 = Path(it) / case / cond / "run-1"
            run2 = Path(it) / case / cond / "run-2"
            if not (EXP / run1 / "shots" / shot).exists():
                cells.append("—")
                continue
            links = [f"[files]({run1}/output/)", f"[run 2]({run2}/shots/{shot})"]
            if shot == "desktop-light.jpg":
                links.insert(0, f"[phone]({run1}/shots/mobile-light.jpg)")
            cells.append(f"<a href=\"{run1}/shots/{shot}\"><img src=\"{run1}/shots/{shot}\" width=\"260\"></a><br>"
                         + " · ".join(links))
        md += ["| " + " | ".join(cells) + " |", ""]
    (EXP / "GALLERY.md").write_text("\n".join(md))
    print(f"GALLERY.md: {len(cases)} cases x {len(cols)} columns")


if __name__ == "__main__":
    main()
