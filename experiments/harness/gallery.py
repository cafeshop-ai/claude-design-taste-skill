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


# Skill commits tested, in order (see README "Log").
VERSIONS = {"0b52da1": "v1", "008e1ca": "v2", "bdd290b": "v3", "6e3c38e": "v4"}


def iterations():
    its = [p for p in EXP.glob("iteration-*") if p.is_dir()]
    return sorted(its, key=lambda p: (not p.name.split("-")[1].isdigit(), int(p.name.split("-")[1]) if p.name.split("-")[1].isdigit() else 0))


def column_label(it, case, cond):
    n = it.name.split("-", 1)[1]
    where = f"iteration {n}" if n.isdigit() else n
    if cond == "baseline":
        return f"baseline ({where})"
    import json
    ref = json.loads((it / case / cond / "run-1" / "meta.json").read_text()).get("skill_ref", "")
    return f"skill {VERSIONS.get(ref, ref)}" + ("" if n.isdigit() else f" ({where})")


def columns(case):
    return [(column_label(it, case, cond), it.name, cond) for it in iterations()
            for cond in ("baseline", "with-skill") if (it / case / cond / "run-1" / "meta.json").exists()]


def main():
    cases = sorted(p.name for p in (EXP / "cases").iterdir())
    md = ["# Gallery",
          "",
          "Every case, side by side: vanilla Codex (baseline) and Codex with each version of the skill. "
          "Run 1 is shown; run 2 is linked. Desktop screenshots at 1440px, full page; click through for phone (390px) "
          "and dark-mode shots, the agent's files, and its final message. Logos show a presentation sheet; animations a "
          "10-frame filmstrip. Cases named `holdout-*` were written after skill v4 was frozen, to test generalization. "
          "See [README.md](README.md) for method and results.",
          ""]
    for case in cases:
        prompt = (EXP / "cases" / case / "prompt.md").read_text().strip()
        md += [f"## {case}", "", f"> {prompt}", ""]
        shot = SHOT.get(case.replace("holdout-", ""), "desktop-light.jpg")
        if case == "holdout-loader":
            shot = "filmstrip.jpg"
        cols = columns(case)
        if not cols:
            continue
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
    print(f"GALLERY.md: {len(cases)} cases")


if __name__ == "__main__":
    main()
