#!/usr/bin/env python3
"""Collect meta.json, audit.json, and events.jsonl for an iteration into
results-auto.md (tables) and results-auto.json (raw rows).

    python3 summarize.py ../iteration-1 [--baseline-from ../iteration-1]

--baseline-from reuses baseline runs from an earlier iteration when this one
only ran the with-skill condition.
"""
import json
import re
import sys
from pathlib import Path
from statistics import mean

WEB = ["landing-page", "invoice-dashboard", "booking-flow", "pricing-restyle", "rsvp-page",
       "holdout-recipe-page", "holdout-water-app", "holdout-closed-notice"]
SVG = ("logo", "svg-animation", "holdout-logo", "holdout-loader", "holdout2-buffering", "holdout2-payment-sent")


def load(path, default=None):
    try:
        return json.loads(Path(path).read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def codex_facts(events_path):
    """Skill files the agent opened, and token usage, from the JSONL event log."""
    read, usage, commands = [], {}, 0
    try:
        lines = Path(events_path).read_text().splitlines()
    except FileNotFoundError:
        return {"skill_files": [], "tokens_in": None, "tokens_out": None, "commands": 0}
    for line in lines:
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = e.get("item") or {}
        if e.get("type") == "item.completed" and item.get("type") == "command_execution":
            commands += 1
            for m in re.findall(r"interface-design/([\w./-]+\.(?:md|css|html|py))", item.get("command", "")):
                if m not in read:
                    read.append(m)
        if e.get("type") == "turn.completed":
            usage = e.get("usage", {})
    return {"skill_files": read, "tokens_in": usage.get("input_tokens"),
            "tokens_out": usage.get("output_tokens"), "commands": commands}


def rows_for(iteration, conditions):
    rows = []
    for run_dir in sorted(Path(iteration).glob("*/*/run-*")):
        case, cond = run_dir.parent.parent.name, run_dir.parent.name
        if cond not in conditions:
            continue
        rows.append({"case": case, "condition": cond, "run": run_dir.name,
                     "dir": str(run_dir), "meta": load(run_dir / "meta.json", {}),
                     "audit": load(run_dir / "audit.json", {}), "interaction": load(run_dir / "interaction.json"),
                     **codex_facts(run_dir / "events.jsonl")})
    return rows


def axe_nodes(violations):
    return sum(v["nodes"] for v in violations or [])


def web_cells(r):
    a = r["audit"]
    if not a or "tells" not in a:
        return None
    t, s, c, f, m = a["tells"], a["system"], a.get("content", {}), a.get("focus", {}), a.get("motion", {})
    return {
        "axe rules": len(a.get("axeDesktopLight", [])),
        "axe nodes": axe_nodes(a.get("axeDesktopLight")),
        "dark contrast nodes": axe_nodes(a.get("axeDesktopDark")),
        "overflow@390": a.get("overflow390"),
        "dark mode": a.get("darkMode"),
        "focus visible": f"{f.get('visible')}/{f.get('stops')}",
        "motion→reduced": f"{m.get('motionRules')}→{'yes' if m.get('reducedMotionHandled') else 'no'}",
        "gradient text": t["gradientText"], "emoji": t["emoji"], "buzzwords": len(t["buzzwords"]),
        "violet": "yes" if t["violetDominant"] else "",
        "centered ¶": t["centeredParagraphs"], "Title Case": t["titleCaseLabels"],
        "font sizes": s["fontSizes"], "families": len(s["fontFamilies"]),
        "words": c.get("words"), "claims": len(c.get("claims", [])), "testimonials": c.get("testimonials"),
        "unlabeled fields": f"{a['forms']['unlabeled']}/{a['forms']['fields']}" if a["forms"]["fields"] else "",
        "console errors": len(a.get("consoleErrors", [])),
        **({"empty submit": r["interaction"]["emptySubmit"]["errorsShown"],
            "flow": f"{r['interaction']['stepsTaken']} steps, {'completed' if r['interaction']['completed'] else 'stuck'}"}
           if r.get("interaction") else {}),
    }


def svg_cells(r):
    a = r["audit"]
    if not a:
        return None
    if r["case"] in ("logo", "holdout-logo"):
        out = {}
        for k in ("logo", "mark"):
            x = a.get(k) or {}
            out[f"{k} bytes"] = x.get("bytes", "missing")
            out[f"{k} elements"] = x.get("elements")
            out[f"{k} colors"] = x.get("distinctColors")
            out[f"{k} <text>"] = "yes" if x.get("usesText") else ""
        out["web font"] = "yes" if any((a.get(k) or {}).get("usesWebFont") for k in ("logo", "mark")) else ""
        return out
    x = a.get("animation") or {}
    technique = "+".join(k for k, v in (("css", x.get("css", {}).get("keyframes")), ("smil", x.get("smil")), ("js", x.get("script"))) if v)
    return {"bytes": x.get("bytes", "missing"), "elements": x.get("elements"), "colors": x.get("distinctColors"),
            "technique": technique, "reduced-motion in source": "yes" if x.get("css", {}).get("reducedMotion") else "no",
            "stops under reduced motion": "yes" if a.get("stopsUnderReducedMotion") else "no",
            "changed pixels (6s)": a.get("changedPixels")}


def table(rows, cells_fn):
    data = [(r, cells_fn(r)) for r in rows]
    data = [(r, c) for r, c in data if c]
    if not data:
        return "_no audited runs_\n"
    cols = list(data[0][1].keys())
    lines = ["| condition | run | skill files read | " + " | ".join(cols) + " |",
             "|---|---|---|" + "---|" * len(cols)]
    for r, c in data:
        files = ", ".join(Path(f).name for f in r["skill_files"]) or "—"
        lines.append(f"| {r['condition']} | {r['run']} | {files if r['condition'] != 'baseline' else ''} | "
                     + " | ".join("" if c[k] is None else str(c[k]) for k in cols) + " |")
    return "\n".join(lines) + "\n"


def aggregate(rows):
    out = ["| metric (web cases) | " + " | ".join(sorted({r['condition'] for r in rows})) + " |",
           "|---|" + "---|" * len({r['condition'] for r in rows})]
    conds = sorted({r["condition"] for r in rows})
    by = {c: [r for r in rows if r["condition"] == c and r["case"] in WEB and r["audit"].get("tells")] for c in conds}

    def metric(name, fn):
        vals = []
        for c in conds:
            rs = by[c]
            vals.append(fn(rs) if rs else "—")
        out.append(f"| {name} | " + " | ".join(str(v) for v in vals) + " |")

    pct = lambda n, d: f"{round(100 * n / d)}% ({n}/{d})" if d else "—"
    metric("runs audited", lambda rs: len(rs))
    metric("axe violations, mean nodes (desktop light)", lambda rs: round(mean(axe_nodes(r["audit"]["axeDesktopLight"]) for r in rs), 1))
    metric("runs with zero axe violations", lambda rs: pct(sum(not r["audit"]["axeDesktopLight"] for r in rs), len(rs)))
    metric("no horizontal overflow at 390px", lambda rs: pct(sum(r["audit"]["overflow390"] <= 0 for r in rs), len(rs)))
    metric("supports dark mode", lambda rs: pct(sum(r["audit"]["darkMode"] == "follows system" for r in rs), len(rs)))
    metric("every tab stop shows focus", lambda rs: pct(sum(r["audit"]["focus"]["visible"] == r["audit"]["focus"]["stops"] > 0 for r in rs), len(rs)))
    metric("has motion and handles reduced motion", lambda rs: pct(sum(r["audit"]["motion"]["reducedMotionHandled"] for r in rs if r["audit"]["motion"]["motionRules"]), sum(1 for r in rs if r["audit"]["motion"]["motionRules"])))
    metric("gradient text (total elements)", lambda rs: sum(r["audit"]["tells"]["gradientText"] for r in rs))
    metric("emoji (total)", lambda rs: sum(r["audit"]["tells"]["emoji"] for r in rs))
    metric("buzzwords (total)", lambda rs: sum(len(r["audit"]["tells"]["buzzwords"]) for r in rs))
    metric("violet-dominant palettes", lambda rs: sum(r["audit"]["tells"]["violetDominant"] for r in rs))
    metric("distinct font sizes, mean", lambda rs: round(mean(r["audit"]["system"]["fontSizes"] for r in rs), 1))
    metric("visible words, mean", lambda rs: round(mean(r["audit"].get("content", {}).get("words", 0) for r in rs)))
    metric("unsupplied claims (total)", lambda rs: sum(len(r["audit"].get("content", {}).get("claims", [])) for r in rs))
    metric("testimonial blocks (total)", lambda rs: sum(r["audit"].get("content", {}).get("testimonials", 0) for r in rs))
    metric("output tokens, mean", lambda rs: round(mean(r["tokens_out"] or 0 for r in rs)))
    metric("wall time s, mean", lambda rs: round(mean(r["meta"].get("seconds", 0) for r in rs)))
    return "\n".join(out) + "\n"


def main():
    iteration = Path(sys.argv[1])
    rows = rows_for(iteration, {"baseline", "with-skill", "with-skill-v2", "with-skill-v3"})
    if "--baseline-from" in sys.argv:
        src = Path(sys.argv[sys.argv.index("--baseline-from") + 1])
        rows = [r for r in rows if r["condition"] != "baseline"] + rows_for(src, {"baseline"})
    rows.sort(key=lambda r: (r["case"], r["condition"] != "baseline", r["condition"], r["run"]))
    md = [f"# Automated results: {iteration.name}\n",
          "Generated by `harness/summarize.py`. These are proxies (accessibility, robustness, common generic tells, content volume), "
          "not a measure of taste; see `judgments.md` for the blind visual comparison.\n",
          "## Aggregate\n", aggregate(rows)]
    for case in sorted({r["case"] for r in rows}):
        md += [f"\n## {case}\n", table([r for r in rows if r["case"] == case],
                                         svg_cells if case in SVG else web_cells)]
    triggered = [r for r in rows if r["condition"] != "baseline"]
    if triggered:
        hit = sum(1 for r in triggered if "SKILL.md" in " ".join(r["skill_files"]))
        md.insert(3, f"Skill triggered (agent opened SKILL.md) in **{hit}/{len(triggered)}** with-skill runs.\n\n")
    (iteration / "results-auto.md").write_text("\n".join(md))
    slim = [{k: v for k, v in r.items() if k != "dir"} for r in rows]
    (iteration / "results-auto.json").write_text(json.dumps(slim, indent=1))
    print((iteration / "results-auto.md").read_text()[:3000])


if __name__ == "__main__":
    main()
