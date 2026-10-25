#!/usr/bin/env python3
"""Independent blind judge: ask Codex to compare each blinded pair.

    python3 judge.py <iteration-dir> [--out blind] [--parallel 6]

For every pair folder in <iteration-dir>/<out>/, sends the X and Y screenshots
plus the case's original brief to `codex exec` (read-only sandbox, empty
workspace, no skills of ours installed) with the same rubric the human-style
judging uses, and a JSON schema for the answer. Writes
<out>/judgments-codex.json in the format blind.py reveal reads.

The judge is told it is comparing two designers' work; it is not told about
the skill or which side is which.
"""
import json
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXP = HERE.parent

WEB_DIMS = {
    "hierarchy": "is the most important thing obvious and the page easy to scan",
    "typography": "typeface choice, scale, line length, rhythm",
    "color": "a purposeful, restrained palette with good contrast",
    "content": "clear, specific, and appropriate to the brief; nothing unnecessary, filler, or made up",
    "craft": "alignment, spacing, consistency, polish, and the phone layout",
    "distinctiveness": "designed for this product rather than looking like a template",
}
LOGO_DIMS = {
    "concept": "a specific idea that fits the name and business",
    "simplicity": "few shapes, memorable, drawable from memory",
    "small-size legibility": "the mark still reads at 16 and 32 px",
    "craft": "geometry, curves, spacing, type quality",
    "versatility": "works on light and dark backgrounds and in one color",
}
ANIM_DIMS = {
    "restraint": "calm and appropriate for an empty state; not distracting or fussy",
    "motion quality": "timing, easing, a visible but gentle loop",
    "illustration craft": "clean drawing, consistent style and palette",
    "fit for context": "suits a 'you're all caught up' moment in an email app",
}


def kind(case):
    return "logo" if case == "logo" else "anim" if case == "svg-animation" else "web"


def build(pair_dir):
    case = pair_dir.name.rsplit("-run-", 1)[0]
    brief = (EXP / "cases" / case / "prompt.md").read_text().strip()
    k = kind(case)
    if k == "web":
        names = ["desktop-light", "mobile-light"]
        dims = WEB_DIMS
        legend = ("Images, in order: 1) X on a 1440px desktop, full page; 2) X on a 390px phone, full page; "
                  "3) Y on a 1440px desktop; 4) Y on a 390px phone.")
    elif k == "logo":
        names, dims = ["sheet"], LOGO_DIMS
        legend = ("Images, in order: 1) X's presentation sheet; 2) Y's. Each sheet shows the full logo on light and dark, "
                  "the icon at 128, 64, 32 and 16 px on light and dark, and the icon in a browser tab.")
    else:
        names, dims = ["filmstrip"], ANIM_DIMS
        legend = ("Images, in order: 1) X's filmstrip; 2) Y's. Each filmstrip is 10 frames captured 650 ms apart from "
                  "page load, read left to right, top row then bottom row.")
    images = [pair_dir / f"{side}-{n}.jpg" for side in ("X", "Y") for n in names]
    rubric = "\n".join(f"- {d}: {why}" for d, why in dims.items())
    prompt = f"""You are a senior product designer reviewing two candidate designs, X and Y, made by different designers for the same brief.

Brief given to both designers:
\"\"\"{brief}\"\"\"

{legend}

Score each candidate from 1 to 5 on each criterion (3 = competent, 4 = strong, 5 = exceptional; be critical):
{rubric}

Then give your overall preference: "X", "Y", or "tie" only if they are genuinely equal. In "notes", give 2 to 4 sentences on the decisive differences, naming specific elements. Judge only what you can see."""
    dim_schema = {"type": "object", "properties": {d: {"type": "integer", "minimum": 1, "maximum": 5} for d in dims},
                  "required": list(dims), "additionalProperties": False}
    schema = {"type": "object", "additionalProperties": False, "required": ["preference", "scores", "notes"],
              "properties": {"preference": {"type": "string", "enum": ["X", "Y", "tie"]},
                             "scores": {"type": "object", "additionalProperties": False, "required": ["X", "Y"],
                                        "properties": {"X": dim_schema, "Y": dim_schema}},
                             "notes": {"type": "string"}}}
    return prompt, images, schema


def judge(pair_dir):
    prompt, images, schema = build(pair_dir)
    with tempfile.TemporaryDirectory() as work:
        schema_path = Path(work) / "schema.json"
        schema_path.write_text(json.dumps(schema))
        out_path = Path(work) / "answer.json"
        args = ["codex", "exec", "--ignore-user-config", "--skip-git-repo-check", "--ephemeral",
                "-c", f'model="{os.environ.get("CODEX_MODEL", "gpt-6.1-sol")}"',
                "-c", f'model_reasoning_effort="{os.environ.get("CODEX_EFFORT", "high")}"',
                "-c", 'approval_policy="never"', "-s", "read-only", "-C", work,
                "--output-schema", str(schema_path), "-o", str(out_path)]
        if os.environ.get("CODEX_BASE_URL"):
            args += ["-c", 'model_provider="proxy"', "-c", 'model_providers.proxy.name="proxy"',
                     "-c", f'model_providers.proxy.base_url="{os.environ["CODEX_BASE_URL"]}"',
                     "-c", 'model_providers.proxy.wire_api="responses"',
                     "-c", "model_providers.proxy.requires_openai_auth=true"]
        for img in images:
            args += ["-i", str(img)]
        args += ["--", prompt]
        for attempt in range(3):
            subprocess.run(args, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=900)
            try:
                answer = json.loads(out_path.read_text())
                return {"pair": pair_dir.name, **answer}
            except (FileNotFoundError, json.JSONDecodeError):
                continue
    return {"pair": pair_dir.name, "error": "no valid answer after 3 attempts"}


def main():
    it = Path(sys.argv[1])
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "blind"
    par = int(sys.argv[sys.argv.index("--parallel") + 1]) if "--parallel" in sys.argv else 6
    pairs = sorted(p for p in (it / out).iterdir() if p.is_dir())
    with ThreadPoolExecutor(par) as pool:
        results = list(pool.map(judge, pairs))
    for r in results:
        print(r["pair"], r.get("preference", r.get("error")))
    (it / out / "judgments-codex.json").write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    main()
