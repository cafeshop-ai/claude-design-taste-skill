#!/usr/bin/env bash
# Run every case × condition × run for one iteration, in parallel.
#   run-iteration.sh <iteration> <skill-ref> [runs=2] [parallel=7] [conditions="baseline with-skill"] [cases=all]
set -euo pipefail
export ITER_N=$1 SKILL_REF=$2
RUNS=${3:-2} PAR=${4:-7} CONDS=${5:-"baseline with-skill"}
HERE=$(cd "$(dirname "$0")" && pwd)
CASES=${6:-$(ls "$HERE/../cases" | grep -v "^holdout")}  # held-out cases run only when named
for run in $(seq 1 "$RUNS"); do
  for case in $CASES; do
    for cond in $CONDS; do echo "$case $cond $run"; done
  done
done | xargs -P "$PAR" -L 1 sh -c 'exec "$0" "$ITER_N" "$1" "$2" "$3" "$SKILL_REF"' "$HERE/run.sh"
