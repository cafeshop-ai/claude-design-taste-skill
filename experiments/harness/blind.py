#!/usr/bin/env python3
"""Blind pairwise judging.

    python3 blind.py make   ../iteration-2 [--b with-skill] [--a-from ../iteration-1] [--a-cond baseline] [--out blind]
    python3 blind.py reveal ../iteration-2 [--out blind]

make: for each case and run number, pairs the baseline run with the
with-skill run, assigns them to X/Y at random, and copies their screenshots
to blind/<case>-run-<n>/{X,Y}-*.jpg. The mapping goes to blind/mapping.json,
which the judge must not open until judgments.json is complete.

reveal: reads blind/judgments.json (written by the judge, one entry per pair:
{"pair", "preference": "X"|"Y"|"tie", "scores": {"X": {...}, "Y": {...}}, "notes"})
and writes judgments.md with the unblinded results.
"""
import json
import random
import shutil
import sys
from pathlib import Path


def make(iteration, b_cond="with-skill", a_from=None, a_cond="baseline", out="blind"):
    iteration = Path(iteration)
    a_root = Path(a_from) if a_from else iteration
    blind = iteration / out
    blind.mkdir(exist_ok=True)
    mapping = {}
    rng = random.SystemRandom()
    for b_run in sorted(iteration.glob(f"*/{b_cond}/run-*")):
        case, run = b_run.parent.parent.name, b_run.name
        a_run = a_root / case / a_cond / run
        if not (a_run / "shots").exists() or not (b_run / "shots").exists():
            continue
        pair = f"{case}-{run}"
        flip = rng.random() < 0.5
        sides = {"X": b_run if flip else a_run, "Y": a_run if flip else b_run}
        out = blind / pair
        out.mkdir(exist_ok=True)
        for label, src in sides.items():
            for shot in (src / "shots").glob("*.jpg"):
                shutil.copy(shot, out / f"{label}-{shot.name}")
        mapping[pair] = {label: str(src.relative_to(iteration.parent)) for label, src in sides.items()}
    (blind / "mapping.json").write_text(json.dumps(mapping, indent=1))
    print(f"{len(mapping)} pairs in {blind}")


def reveal(iteration, out="blind", judge=None):
    iteration = Path(iteration)
    blind = iteration / out
    mapping = json.loads((blind / "mapping.json").read_text())
    judgments = [j for j in json.loads((blind / (f"judgments-{judge}.json" if judge else "judgments.json")).read_text()) if "error" not in j]
    # Label by condition, or by iteration/condition when comparing across iterations.
    iters = {Path(v).parts[0] for m in mapping.values() for v in m.values()}
    cond = (lambda path: f"{Path(path).parts[0]}/{Path(path).parent.name}") if len(iters) > 1 else (lambda path: Path(path).parent.name)
    wins, lines = {}, []
    dims = sorted({d for j in judgments for side in j["scores"].values() for d in side})
    totals = {}
    for j in judgments:
        m = mapping[j["pair"]]
        pref = j["preference"]
        winner = "tie" if pref == "tie" else cond(m[pref])
        wins[winner] = wins.get(winner, 0) + 1
        for label in ("X", "Y"):
            c = cond(m[label])
            for d, v in j["scores"][label].items():
                totals.setdefault(c, {}).setdefault(d, []).append(v)
        lines.append(f"### {j['pair']}\n\nX = `{cond(m['X'])}`, Y = `{cond(m['Y'])}`. "
                     f"Preferred: **{pref}** ({winner}).\n\n"
                     + "| | " + " | ".join(dims) + " |\n|---|" + "---|" * len(dims) + "\n"
                     + "\n".join(f"| {label} ({cond(m[label])}) | " + " | ".join(str(j['scores'][label].get(d, '')) for d in dims) + " |" for label in ("X", "Y"))
                     + f"\n\n{j['notes']}\n")
    summary = ["| condition | " + " | ".join(dims) + " |", "|---|" + "---|" * len(dims)]
    for c, ds in sorted(totals.items()):
        summary.append(f"| {c} | " + " | ".join(f"{sum(ds[d]) / len(ds[d]):.2f}" for d in dims) + " |")
    who = ("Judge: Codex (`gpt-6.1-sol`, via `harness/judge.py`), an independent judge that saw only the brief, the two "
           "screenshot sets, and the rubric; it was not told about the skill. It may favor its own house style."
           if judge == "codex" else
           "Judge: Claude (the skill's author), so read these as one informed but interested opinion.")
    md = [f"# Blind judgments: {iteration.name}{' (' + out + ')' if out != 'blind' else ''}{', judge ' + judge if judge else ''}\n",
          "Judged from screenshots with conditions hidden behind random X/Y labels; the mapping was opened only after "
          f"all judgments below were written. Scores are 1–5. {who} The screenshots are in each run's `shots/` folder for anyone to check.\n",
          "## Preferences\n", "\n".join(f"- **{k}**: {v}" for k, v in sorted(wins.items())) + "\n",
          "## Mean scores\n", "\n".join(summary) + "\n", "## Pairs\n", "\n".join(lines)]
    name = "judgments" + ("" if out == "blind" else f"-{out}") + (f"-{judge}" if judge else "") + ".md"
    (iteration / name).write_text("\n".join(md))
    print("\n".join(md[:6]))


if __name__ == "__main__":
    cmd, it = sys.argv[1], sys.argv[2]
    opt = lambda name, default: sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default
    if cmd == "make":
        make(it, opt("--b", "with-skill"), opt("--a-from", None), opt("--a-cond", "baseline"), opt("--out", "blind"))
    else:
        reveal(it, opt("--out", "blind"), opt("--judge", None))
