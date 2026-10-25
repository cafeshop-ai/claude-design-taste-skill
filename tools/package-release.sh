#!/usr/bin/env sh
# Build the release asset: dist/interface-design.zip, containing interface-design/
# exactly as committed at <ref> (default HEAD). Upload it to a GitHub release:
#   tools/package-release.sh v5.0.0 && gh release create v5.0.0 dist/interface-design.zip ...
set -eu
REF="${1:-HEAD}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$ROOT/dist"
rm -f "$ROOT/dist/interface-design.zip"
git -C "$ROOT" archive --format=zip -o "$ROOT/dist/interface-design.zip" "$REF" interface-design
unzip -l "$ROOT/dist/interface-design.zip" | grep -q "interface-design/SKILL.md" || { echo "SKILL.md missing from archive" >&2; exit 1; }
if command -v sha256sum >/dev/null 2>&1; then sha256sum "$ROOT/dist/interface-design.zip"; else shasum -a 256 "$ROOT/dist/interface-design.zip"; fi
ls -l "$ROOT/dist/interface-design.zip"
