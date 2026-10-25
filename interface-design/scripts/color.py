#!/usr/bin/env python3
"""Color utilities for interface design. No dependencies.

Subcommands
  contrast FG BG        WCAG 2 contrast ratio + APCA Lc for a text/background pair
  ramp                  Generate a perceptually even OKLCH ramp (50-950), gamut-mapped to sRGB
  convert COLOR         Show a color as hex, rgb(), and oklch()

Colors may be given as #rgb, #rrggbb, rgb(r g b) / rgb(r, g, b), or oklch(L C H)
where L is 0-1 or a percentage.

Examples
  python3 color.py contrast "#6b7280" "#ffffff"
  python3 color.py contrast "oklch(0.55 0.15 255)" white
  python3 color.py ramp --hue 255 --chroma 0.15
  python3 color.py ramp --hue 70 --chroma 0.012 --name neutral --format css
  python3 color.py convert "#3b82f6"
"""

import argparse
import math
import re
import sys

NAMED = {"white": "#ffffff", "black": "#000000"}

# Lightness targets for each ramp step. Tuned so 500 sits near 4.5:1 on white,
# and 50/950 are usable as page backgrounds in light and dark themes.
STEPS = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]
LIGHTNESS = [0.985, 0.967, 0.925, 0.870, 0.730, 0.560, 0.490, 0.420, 0.345, 0.270, 0.200]
# Chroma multipliers: colors are most saturated in the mid-tones and must
# desaturate toward white and black to stay in gamut and avoid looking garish.
CHROMA_SHAPE = [0.045, 0.10, 0.23, 0.42, 0.92, 1.00, 0.98, 0.88, 0.74, 0.58, 0.42]


# --- conversions ------------------------------------------------------------

def srgb_to_linear(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def linear_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055


def oklch_to_oklab(L, C, H):
    h = math.radians(H)
    return L, C * math.cos(h), C * math.sin(h)


def oklab_to_linear_rgb(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def linear_rgb_to_oklab(r, g, b):
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklch_to_srgb(L, C, H):
    """Return (r, g, b) in 0-1, unclamped."""
    lin = oklab_to_linear_rgb(*oklch_to_oklab(L, C, H))
    return tuple(linear_to_srgb(c) if c >= 0 else -linear_to_srgb(-c) for c in lin)


def srgb_to_oklch(r, g, b):
    L, a, bb = linear_rgb_to_oklab(*(srgb_to_linear(c) for c in (r, g, b)))
    C = math.hypot(a, bb)
    H = math.degrees(math.atan2(bb, a)) % 360
    return L, C, H


def in_gamut(rgb, eps=1e-4):
    return all(-eps <= c <= 1 + eps for c in rgb)


def gamut_map(L, C, H):
    """Reduce chroma (keeping L and H) until the color fits in sRGB."""
    if in_gamut(oklch_to_srgb(L, C, H)):
        return L, C, H, False
    lo, hi = 0.0, C
    for _ in range(30):
        mid = (lo + hi) / 2
        if in_gamut(oklch_to_srgb(L, mid, H)):
            lo = mid
        else:
            hi = mid
    return L, lo, H, True


def to_hex(rgb):
    return "#" + "".join(f"{round(min(1, max(0, c)) * 255):02x}" for c in rgb)


# --- parsing ----------------------------------------------------------------

def parse_color(text):
    s = text.strip().lower()
    s = NAMED.get(s, s)
    m = re.fullmatch(r"#?([0-9a-f]{3}|[0-9a-f]{6})", s)
    if m:
        h = m.group(1)
        if len(h) == 3:
            h = "".join(ch * 2 for ch in h)
        return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    m = re.fullmatch(r"rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+).*\)", s)
    if m:
        return tuple(float(v) / 255 for v in m.groups())
    m = re.fullmatch(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)(?:deg)?\s*(?:/.*)?\)", s)
    if m:
        L = float(m.group(1)) / (100 if m.group(2) else 1)
        L, C, H, _ = gamut_map(L, float(m.group(3)), float(m.group(4)))
        return tuple(min(1, max(0, c)) for c in oklch_to_srgb(L, C, H))
    raise ValueError(f"Can't parse color: {text!r}")


# --- contrast ---------------------------------------------------------------

def wcag_luminance(rgb):
    r, g, b = (srgb_to_linear(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def wcag_ratio(fg, bg):
    l1, l2 = sorted((wcag_luminance(fg), wcag_luminance(bg)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def apca_lc(fg, bg):
    """APCA-W3 0.0.98G-4g lightness contrast. Positive = dark text on light bg."""
    def y(rgb):
        r, g, b = (c ** 2.4 for c in rgb)
        v = 0.2126729 * r + 0.7151522 * g + 0.0721750 * b
        return v + (0.022 - v) ** 1.414 if v < 0.022 else v

    yt, yb = y(fg), y(bg)
    if abs(yb - yt) < 0.0005:
        return 0.0
    if yb > yt:
        sapc = (yb ** 0.56 - yt ** 0.57) * 1.14
        out = 0 if sapc < 0.1 else sapc - 0.027
    else:
        sapc = (yb ** 0.65 - yt ** 0.62) * 1.14
        out = 0 if sapc > -0.1 else sapc + 0.027
    return out * 100


def wcag_verdict(ratio):
    if ratio >= 7:
        return "AAA all text"
    if ratio >= 4.5:
        return "AA all text (AAA large)"
    if ratio >= 3:
        return "AA large text & UI components only"
    return "FAIL (decorative only)"


def apca_verdict(lc):
    a = abs(lc)
    if a >= 90:
        return "excellent for body text"
    if a >= 75:
        return "fine for body text"
    if a >= 60:
        return "ok for content text >=16px medium / >=24px regular"
    if a >= 45:
        return "headlines & large/bold text, icons"
    if a >= 30:
        return "non-text UI, placeholder, disabled only"
    if a >= 15:
        return "dividers / decorative only"
    return "invisible"


# --- commands ---------------------------------------------------------------

def cmd_contrast(args):
    fg, bg = parse_color(args.fg), parse_color(args.bg)
    ratio = wcag_ratio(fg, bg)
    lc = apca_lc(fg, bg)
    print(f"text {to_hex(fg)} on {to_hex(bg)}")
    print(f"  WCAG 2  {ratio:5.2f}:1   {wcag_verdict(ratio)}")
    print(f"  APCA    Lc {lc:6.1f}   {apca_verdict(lc)}")


def cmd_convert(args):
    rgb = parse_color(args.color)
    L, C, H = srgb_to_oklch(*rgb)
    print(f"hex    {to_hex(rgb)}")
    print(f"rgb    rgb({' '.join(str(round(c * 255)) for c in rgb)})")
    print(f"oklch  oklch({L:.3f} {C:.3f} {H:.1f})")
    print(f"vs white {wcag_ratio(rgb, (1, 1, 1)):.2f}:1   vs black {wcag_ratio(rgb, (0, 0, 0)):.2f}:1")


def cmd_ramp(args):
    rows = []
    for step, L, k in zip(STEPS, LIGHTNESS, CHROMA_SHAPE):
        # Optional hue shift across the ramp (e.g. yellows drift warmer as they darken).
        t = (STEPS.index(step)) / (len(STEPS) - 1)
        H = (args.hue + args.hue_shift * (t - 0.5)) % 360
        L2, C2, H2, clipped = gamut_map(L, args.chroma * k, H)
        rgb = tuple(min(1, max(0, c)) for c in oklch_to_srgb(L2, C2, H2))
        rows.append((step, L2, C2, H2, clipped, rgb))

    name = args.name
    if args.format == "css":
        for step, L, C, H, _, _ in rows:
            print(f"  --{name}-{step}: oklch({L:.3f} {C:.3f} {H:.1f});")
        return
    if args.format == "hex":
        for step, *_, rgb in rows:
            print(f"  --{name}-{step}: {to_hex(rgb)};")
        return

    white, black = (1, 1, 1), (0, 0, 0)
    print(f"{'step':>5}  {'oklch':<24} {'hex':<8} {'on white':>9} {'on black':>9}  note")
    for step, L, C, H, clipped, rgb in rows:
        ow, ob = wcag_ratio(rgb, white), wcag_ratio(rgb, black)
        note = []
        if ow >= 4.5:
            note.append("text-on-white ok")
        if ob >= 4.5:
            note.append("text-on-black ok")
        if clipped:
            note.append("chroma reduced to fit sRGB")
        print(f"{step:>5}  oklch({L:.3f} {C:.3f} {H:5.1f})  {to_hex(rgb):<8} {ow:8.2f}  {ob:8.2f}   {', '.join(note)}")
    print("\nTip: white text works on steps whose 'on white' ratio is >= 4.5; "
          "dark text on steps whose 'on black' ratio is >= 4.5.")


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("contrast", help="contrast of text FG on background BG")
    c.add_argument("fg")
    c.add_argument("bg")
    c.set_defaults(func=cmd_contrast)

    r = sub.add_parser("ramp", help="generate a 50-950 OKLCH ramp")
    r.add_argument("--hue", type=float, required=True, help="OKLCH hue in degrees (e.g. 255 blue, 25 red, 150 green, 70 warm neutral)")
    r.add_argument("--chroma", type=float, default=0.14, help="peak chroma (0.005-0.02 neutrals, 0.10-0.20 accents)")
    r.add_argument("--hue-shift", type=float, default=0.0, help="degrees of hue drift from lightest to darkest step")
    r.add_argument("--name", default="color", help="token prefix for css/hex output")
    r.add_argument("--format", choices=["table", "css", "hex"], default="table")
    r.set_defaults(func=cmd_ramp)

    v = sub.add_parser("convert", help="convert a color between formats")
    v.add_argument("color")
    v.set_defaults(func=cmd_convert)

    args = p.parse_args(argv)
    try:
        args.func(args)
    except ValueError as e:
        sys.exit(str(e))


if __name__ == "__main__":
    main()
