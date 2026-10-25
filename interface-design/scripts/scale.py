#!/usr/bin/env python3
"""Generate modular type scales and fluid clamp() values. No dependencies.

A modular scale multiplies a base size by a ratio for each step. A fluid scale
uses a smaller ratio on small screens and a larger one on wide screens, so big
headings grow faster than body text as the viewport widens.

Common ratios
  1.125  major second   dense app UI
  1.200  minor third    apps, dashboards, docs
  1.250  major third    general web
  1.333  perfect fourth marketing, landing pages
  1.500  perfect fifth  editorial, expressive display type

Examples
  python3 scale.py --base 16 --ratio 1.25
  python3 scale.py --base 16 --ratio 1.2 --max-base 18 --max-ratio 1.333
  python3 scale.py --base 16 --ratio 1.25 --steps -2 6 --format css --prefix text
  python3 scale.py --space --min 64 --max 128        # one fluid value, e.g. section padding
"""

import argparse

ROOT_PX = 16  # rem conversions assume the browser default; never set html font-size in px


def rem(px):
    return f"{px / ROOT_PX:.4g}rem"


def fluid(min_px, max_px, min_vw, max_vw):
    """clamp() that scales linearly from min_px at min_vw to max_px at max_vw.

    The preferred value mixes rem and vw so text still responds to browser zoom
    (a pure-vw value would not, which fails WCAG 1.4.4).
    """
    if abs(max_px - min_px) < 0.01:
        return rem(min_px)
    slope = (max_px - min_px) / (max_vw - min_vw)
    intercept = min_px - slope * min_vw
    lo, hi = sorted((min_px, max_px))
    sign = "+" if slope >= 0 else "-"
    return f"clamp({rem(lo)}, {intercept / ROOT_PX:.4g}rem {sign} {abs(slope) * 100:.4g}vw, {rem(hi)})"


def line_height(px):
    # Larger type needs proportionally less leading.
    if px <= 18:
        return 1.5
    if px <= 24:
        return 1.4
    if px <= 32:
        return 1.3
    if px <= 48:
        return 1.2
    if px <= 72:
        return 1.1
    return 1.05


def tracking(px):
    # Tighten large display type; loosen very small text slightly.
    if px <= 12:
        return "0.01em"
    if px < 24:
        return "0"
    if px < 40:
        return "-0.01em"
    if px < 64:
        return "-0.02em"
    return "-0.03em"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--base", type=float, default=16, help="base (body) size in px at the small viewport")
    p.add_argument("--ratio", type=float, default=1.25, help="scale ratio at the small viewport")
    p.add_argument("--max-base", type=float, help="base size at the wide viewport (enables fluid output)")
    p.add_argument("--max-ratio", type=float, help="ratio at the wide viewport (enables fluid output)")
    p.add_argument("--min-vw", type=float, default=375, help="small viewport width in px")
    p.add_argument("--max-vw", type=float, default=1440, help="wide viewport width in px")
    p.add_argument("--steps", type=int, nargs=2, default=[-2, 6], metavar=("LOW", "HIGH"))
    p.add_argument("--round", action="store_true", help="round sizes to whole pixels")
    p.add_argument("--format", choices=["table", "css"], default="table")
    p.add_argument("--prefix", default="step", help="custom property prefix for css output")
    p.add_argument("--space", action="store_true", help="just print one fluid value from --min to --max px")
    p.add_argument("--min", type=float, help="with --space: value at the small viewport (px)")
    p.add_argument("--max", type=float, help="with --space: value at the wide viewport (px)")
    a = p.parse_args()

    if a.space:
        if a.min is None or a.max is None:
            p.error("--space needs --min and --max")
        print(fluid(a.min, a.max, a.min_vw, a.max_vw))
        return

    is_fluid = a.max_base is not None or a.max_ratio is not None
    max_base = a.max_base if a.max_base is not None else a.base
    max_ratio = a.max_ratio if a.max_ratio is not None else a.ratio

    rows = []
    for i in range(a.steps[0], a.steps[1] + 1):
        lo = a.base * a.ratio ** i
        hi = max_base * max_ratio ** i
        if i < 0:
            hi = max(hi, lo)  # small text should never shrink as the screen grows
        if a.round:
            lo, hi = round(lo), round(hi)
        value = fluid(lo, hi, a.min_vw, a.max_vw) if is_fluid else rem(lo)
        rows.append((i, lo, hi, value))

    if a.format == "css":
        for i, lo, hi, value in rows:
            name = f"--{a.prefix}-{i}"  # negative steps read as --step--1, the Utopia convention
            print(f"  {name}: {value};  /* {lo:.1f}px{f' → {hi:.1f}px' if is_fluid else ''}, lh {line_height(hi)}, tracking {tracking(hi)} */")
        return

    head = f"{'step':>4}  {'px':>14}  {'line-height':>11}  {'tracking':>9}  css"
    print(head)
    for i, lo, hi, value in rows:
        px = f"{lo:.1f}" + (f" → {hi:.1f}" if is_fluid else "")
        print(f"{i:>4}  {px:>14}  {line_height(hi):>11}  {tracking(hi):>9}  {value}")
    print("\nStep 0 is body text. Use 3-6 steps above it for headings; most interfaces need no more than 6-8 sizes in total.")


if __name__ == "__main__":
    main()
