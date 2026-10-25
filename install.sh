#!/usr/bin/env sh
# Install the interface-design skill from the latest GitHub release.
#
#   curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh
#   curl -fsSL https://raw.githubusercontent.com/cafeshop-ai/claude-design-taste-skill/main/install.sh | sh -s -- --codex
#
# Targets (default --claude):
#   --claude         ~/.claude/skills/interface-design   (Claude Code, all projects)
#   --codex          ~/.codex/skills/interface-design    (Codex CLI)
#   --agents         ~/.agents/skills/interface-design   (other Agent Skills hosts)
#   --project        ./.claude/skills/interface-design   (this project only)
#   --dir <path>     <path>/interface-design
# Options:
#   --force          replace an existing install
#   --version <tag>  install a specific release (e.g. v5.0.0) instead of the latest
#
# Downloads only the skill (a ~150 KB zip), never the repository's experiment data.
set -eu

REPO="cafeshop-ai/claude-design-taste-skill"
NAME="interface-design"
DEST_ROOT="${HOME}/.claude/skills"
FORCE=0
TAG=""

usage() {
  cat <<'USAGE'
Install the interface-design skill from the latest GitHub release.
Usage: install.sh [--claude | --codex | --agents | --project | --dir <path>] [--force] [--version <tag>]
  --claude    ~/.claude/skills (default)     --codex    ~/.codex/skills
  --agents    ~/.agents/skills               --project  ./.claude/skills
  --dir PATH  PATH/interface-design          --force    replace an existing install
  --version   a release tag such as v5.0.0 (default: latest)
USAGE
}

while [ $# -gt 0 ]; do
  case "$1" in
    --claude)  DEST_ROOT="${HOME}/.claude/skills" ;;
    --codex)   DEST_ROOT="${CODEX_HOME:-${HOME}/.codex}/skills" ;;
    --agents)  DEST_ROOT="${HOME}/.agents/skills" ;;
    --project) DEST_ROOT="$(pwd)/.claude/skills" ;;
    --dir)     shift; DEST_ROOT="$1" ;;
    --force)   FORCE=1 ;;
    --version) shift; TAG="$1" ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1 (try --help)" >&2; exit 2 ;;
  esac
  shift
done

if [ -n "$TAG" ]; then
  URL="https://github.com/${REPO}/releases/download/${TAG}/${NAME}.zip"
else
  URL="https://github.com/${REPO}/releases/latest/download/${NAME}.zip"
fi
DEST="${DEST_ROOT}/${NAME}"

if [ -e "$DEST" ] && [ "$FORCE" -ne 1 ]; then
  echo "${DEST} already exists. Re-run with --force to replace it." >&2
  exit 1
fi

TMP="$(mktemp -d 2>/dev/null || mktemp -d -t interface-design)"
trap 'rm -rf "$TMP"' EXIT INT TERM

echo "Downloading ${URL}"
if command -v curl >/dev/null 2>&1; then
  curl -fsSL "$URL" -o "$TMP/skill.zip"
elif command -v wget >/dev/null 2>&1; then
  wget -q "$URL" -O "$TMP/skill.zip"
else
  echo "Needs curl or wget." >&2; exit 1
fi

mkdir -p "$TMP/x"
if command -v unzip >/dev/null 2>&1; then
  unzip -q "$TMP/skill.zip" -d "$TMP/x"
elif command -v python3 >/dev/null 2>&1; then
  python3 -m zipfile -e "$TMP/skill.zip" "$TMP/x"
else
  echo "Needs unzip or python3 to extract the download." >&2; exit 1
fi

if [ ! -f "$TMP/x/${NAME}/SKILL.md" ]; then
  echo "The download doesn't look like the skill (no ${NAME}/SKILL.md)." >&2; exit 1
fi

mkdir -p "$DEST_ROOT"
rm -rf "$DEST"
mv "$TMP/x/${NAME}" "$DEST"
chmod +x "$DEST"/scripts/*.py 2>/dev/null || true

echo "Installed ${NAME} to ${DEST}"
echo "Start a new session; the skill triggers on its own for design work."
