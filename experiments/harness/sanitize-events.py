#!/usr/bin/env python3
"""Strip shell command output from Codex event logs before publishing.

Codex's logs include the raw output of every command it ran. When an agent
explores (looking for a browser, say), that output can list directories and
environment variable names on the host machine. We keep what the agent did
(messages, reasoning summaries, commands, exit codes, file changes) and drop
command output, replacing it with its length, and redact the model endpoint's
host name wherever it appears (set CODEX_BASE_URL when running this).

    python3 sanitize-events.py <events.jsonl> [...]
"""
import json
import os
import re
import sys

# The model endpoint is private even when it's not a secret: redact it wherever
# it appears (an agent may probe its own API host with curl).
ENDPOINT = os.environ.get("CODEX_BASE_URL", "")
HOST = re.sub(r"^https?://", "", ENDPOINT).split("/")[0] if ENDPOINT else ""

for path in sys.argv[1:]:
    out = []
    with open(path) as f:
        for line in f:
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                continue
            item = e.get("item")
            if isinstance(item, dict) and item.get("type") == "command_execution" and item.get("aggregated_output"):
                item["aggregated_output"] = f"[{len(item['aggregated_output'])} chars of command output removed before publishing]"
            line_out = json.dumps(e, ensure_ascii=False)
            if HOST:
                line_out = line_out.replace(HOST, "[model-endpoint]")
            out.append(line_out)
    with open(path, "w") as f:
        f.write("\n".join(out) + "\n")
