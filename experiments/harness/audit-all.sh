#!/usr/bin/env bash
# Audit every finished run in an iteration (skips runs already audited unless FORCE=1).
#   audit-all.sh <iteration-dir> [parallel=4]
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
ITER_DIR=$(cd "$1" && pwd); PAR=${2:-4}
for d in "$ITER_DIR"/*/*/run-*; do
  [ -f "$d/meta.json" ] || continue                       # still running
  [ -f "$d/audit.json" ] && [ "${FORCE:-0}" != 1 ] && continue
  echo "$d"
done | xargs -P "$PAR" -I{} sh -c '
  d={}; case $d in
    */holdout-logo/*) node "'"$HERE"'/audit-svg.mjs" "$d" logo "Halyard Sailing" ;;
    */logo/*) node "'"$HERE"'/audit-svg.mjs" "$d" logo "Fernway Books" ;;
    */svg-animation/*|*/holdout-loader/*) node "'"$HERE"'/audit-svg.mjs" "$d" svg-animation ;;
    *) node "'"$HERE"'/audit.mjs" "$d" ;;
  esac'
