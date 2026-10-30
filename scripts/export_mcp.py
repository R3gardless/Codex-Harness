#!/usr/bin/env python3
"""Export exactly one MCP preset as generic mcpServers JSON. Does not connect."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def export_server(name):
    try:
        import tomllib
    except ImportError as exc:
        raise ValueError("MCP export requires Python 3.11 or newer") from exc
    data = tomllib.loads((ROOT / "mcp/codex.toml").read_text(encoding="utf-8"))
    servers = data["mcp_servers"]
    if name not in servers:
        raise ValueError("Choose one of: " + ", ".join(sorted(servers)))
    server = servers[name]
    # Keep command arguments (including read-only flags), but not Codex-only keys.
    fields = ("url",) if "url" in server else ("command", "args", "env")
    result = {key: server[key] for key in fields if key in server}
    if "url" in server:
        result["type"] = "http"
    return {"mcpServers": {name: result}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--server", required=True)
    args = parser.parse_args()
    try:
        result = export_server(args.server)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"Export stopped: {exc}\n")
    print("Example only: importing may activate this server. Check the host schema and permissions. "
          "Codex-specific tool filters and timeouts are not exported.", file=sys.stderr)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
