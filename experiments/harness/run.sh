#!/usr/bin/env bash
# Run one Codex trial.
#   run.sh <iteration> <case> <condition: baseline|with-skill> <run> [skill-ref]
#
# Each trial runs in its own empty workspace outside the repo, so Codex sees
# only the case's input files (and, for with-skill, the skill installed at
# .agents/skills/interface-design, exported from git at <skill-ref>).
# Vanilla Codex: --ignore-user-config drops personal config, plugins, and
# hooks; the model and provider are passed explicitly.
#
# Env: CODEX_MODEL (default gpt-6.1-sol), CODEX_EFFORT (default high),
#      CODEX_BASE_URL (optional OpenAI-compatible Responses endpoint),
#      WORK_ROOT (default /tmp/design-taste-runs).
set -euo pipefail

ITER=$1 CASE=$2 COND=$3 RUN=$4 REF=${5:-HEAD}
HERE=$(cd "$(dirname "$0")" && pwd)
EXP=$(dirname "$HERE")
REPO=$(dirname "$EXP")
WORK=${WORK_ROOT:-/tmp/design-taste-runs}/iteration-$ITER/$CASE/$COND/run-$RUN
OUT=$EXP/iteration-$ITER/$CASE/$COND/run-$RUN
MODEL=${CODEX_MODEL:-gpt-6.1-sol}
EFFORT=${CODEX_EFFORT:-high}
SHA=$(git -C "$REPO" rev-parse --short "$REF")

rm -rf "$WORK" "$OUT"
mkdir -p "$WORK" "$OUT/output"
if [ -d "$EXP/cases/$CASE/files" ]; then cp -r "$EXP/cases/$CASE/files/." "$WORK/"; fi
if [ "$COND" = with-skill ]; then
  mkdir -p "$WORK/.agents/skills"
  git -C "$REPO" archive "$REF" interface-design | tar -x -C "$WORK/.agents/skills"
fi

args=(exec --ignore-user-config --skip-git-repo-check --ephemeral --json
  -c "model=\"$MODEL\"" -c "model_reasoning_effort=\"$EFFORT\""
  -c 'approval_policy="never"' -s workspace-write -C "$WORK"
  -o "$OUT/final-message.md")
if [ -n "${CODEX_BASE_URL:-}" ]; then
  args+=(-c 'model_provider="proxy"' -c 'model_providers.proxy.name="proxy"'
    -c "model_providers.proxy.base_url=\"$CODEX_BASE_URL\""
    -c 'model_providers.proxy.wire_api="responses"'
    -c 'model_providers.proxy.requires_openai_auth=true')
fi

start=$(date +%s)
status=0
codex "${args[@]}" "$(cat "$EXP/cases/$CASE/prompt.md")" \
  < /dev/null > "$OUT/events.jsonl" 2> "$OUT/stderr.log" || status=$?
seconds=$(( $(date +%s) - start ))

# Logs are published: drop raw command output, which can describe the host.
python3 "$HERE/sanitize-events.py" "$OUT/events.jsonl"

# Keep what Codex produced, not the skill copy.
(cd "$WORK" && tar --exclude=./.agents -cf - .) | tar -xf - -C "$OUT/output"

cat > "$OUT/meta.json" <<EOF
{"case": "$CASE", "condition": "$COND", "run": $RUN, "skill_ref": "$([ "$COND" = with-skill ] && echo "$SHA")",
 "codex": "$(codex --version 2>/dev/null)", "model": "$MODEL", "effort": "$EFFORT",
 "exit_status": $status, "seconds": $seconds}
EOF
echo "$CASE/$COND/run-$RUN: exit $status in ${seconds}s"
