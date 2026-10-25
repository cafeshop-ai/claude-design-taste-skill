#!/usr/bin/env python3
"""Strip shell command output from Codex event logs before publishing.

Codex's logs include the raw output of every command it ran. When an agent
explores (looking for a browser, say), that output can list directories and
environment variable names on the host machine. We keep what the agent did
(messages, reasoning summaries, commands, exit codes, file changes) and drop
command output, replacing it with its length.

    python3 sanitize-events.py <events.jsonl> [...]
"""
import json
import sys

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
            out.append(json.dumps(e, ensure_ascii=False))
    with open(path, "w") as f:
        f.write("\n".join(out) + "\n")
