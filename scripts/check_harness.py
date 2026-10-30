#!/usr/bin/env python3
"""Offline structural checks for this harness. No package installs or network calls."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    root = Path(root)
    errors = []
    skills = sorted((root / ".agents/skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills discovered")
    names = set()
    for path in skills:
        text = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            errors.append(f"Missing frontmatter: {path}")
            continue
        fields = {}
        for line in match[1].splitlines():
            if ": " not in line:
                errors.append(f"Expected simple key/value frontmatter: {path}")
                continue
            key, value = line.split(": ", 1)
            fields[key] = value.strip()
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
            errors.append(f"Invalid name: {path}")
        if name in names or name != path.parent.name:
            errors.append(f"Duplicate name or folder mismatch: {path}")
        names.add(name)
        if not fields.get("description") or len(fields["description"]) > 1024:
            errors.append(f"Invalid description: {path}")
        if "[TODO:" in text:
            errors.append(f"Unfinished scaffold: {path}")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"[a-z]+://|#", target):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).exists():
                errors.append(f"Broken local link in {path}: {target}")
    guide = (root / "AGENTS.md").read_text(encoding="utf-8")
    if len(guide.encode()) > 16_384:
        errors.append("Root instructions exceed the harness's 16 KiB budget")
    for name in names:
        if f"`{name}`" not in guide:
            errors.append(f"Missing skill routing: {name}")
    try:
        import tomllib
    except ImportError:
        print("NOTE: Python 3.11+ is needed for the optional TOML configuration check.")
    else:
        try:
            config = tomllib.loads((root / "mcp/codex.toml").read_text(encoding="utf-8"))
            for name, server in config["mcp_servers"].items():
                if server.get("enabled") is not False:
                    errors.append(f"Preset must be dormant: {name}")
                if ("url" in server) == ("command" in server):
                    errors.append(f"Preset needs exactly one transport: {name}")
            for name in ("aws_resources", "azure_resources"):
                if "--read-only" not in config["mcp_servers"][name]["args"]:
                    errors.append(f"Missing resource read-only flag: {name}")
        except (ValueError, KeyError, OSError) as exc:
            errors.append(f"Invalid MCP config: {exc}")
    return skills, errors


if __name__ == "__main__":
    found, errors = check()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"PASS: {len(found)} skills, routing, local links, instruction size, and available config checks")
