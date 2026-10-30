#!/usr/bin/env python3
"""Install project instructions and skills; preview by default, never overwrite conflicts."""
import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import tempfile

START = "<!-- codex-harness:start -->"
END = "<!-- codex-harness:end -->"
ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Change:
    path: Path
    content: bytes
    before: object


def safe_destination(target, relative):
    path = target / relative
    current = target
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f"Refusing symlink destination: {current}")
        if current != path and current.exists() and not current.is_dir():
            raise ValueError(f"Parent is not a directory: {current}")
    if path.exists() and not path.is_file():
        raise ValueError(f"Destination is not a file: {path}")
    return path


def plan_install(target, source=ROOT):
    target, source = Path(target).absolute(), Path(source).resolve()
    if target.is_symlink() or not target.is_dir():
        raise ValueError("Target must be an existing, non-symlink directory")
    target = target.resolve()
    if target == source or source in target.parents or target in source.parents:
        raise ValueError("Keep the harness source outside the target project")
    changes = []
    skills = source / ".agents" / "skills"
    if not skills.is_dir() or not list(skills.glob("*/SKILL.md")):
        raise ValueError("No source skills found")
    for src in sorted(skills.rglob("*")):
        if src.is_symlink():
            raise ValueError(f"Refusing source symlink: {src}")
        if not src.is_file():
            continue
        dest = safe_destination(target, src.relative_to(source))
        data = src.read_bytes()
        before = dest.read_bytes() if dest.exists() else None
        if before is not None and before != data:
            raise ValueError(f"Existing file differs; merge manually: {dest}")
        if before is None:
            changes.append(Change(dest, data, None))

    dest = safe_destination(target, Path("AGENTS.md"))
    before = dest.read_bytes() if dest.exists() else None
    guide = (source / "AGENTS.md").read_text(encoding="utf-8").strip()
    block = (START + "\n\n" +
             "Host project instructions outside this block take precedence over "
             "this portable harness when they conflict.\n\n" + guide +
             "\n\n" + END + "\n").encode("utf-8")
    if before is None:
        changes.append(Change(dest, block, None))
    else:
        start, end = START.encode(), END.encode()
        if start in before or end in before:
            if before.count(start) != 1 or before.count(end) != 1 or block not in before:
                raise ValueError("Existing harness block differs or is malformed; merge manually")
        else:
            separator = b"\n\n" if before else b""
            changes.append(Change(dest, before + separator + block, before))
    return changes


def apply_changes(changes):
    # Verify every observed file again before starting writes.
    for change in changes:
        actual = change.path.read_bytes() if change.path.exists() else None
        if change.path.is_symlink() or actual != change.before:
            raise ValueError(f"Destination changed since preview: {change.path}")
    for change in changes:
        change.path.parent.mkdir(parents=True, exist_ok=True)
        mode = change.path.stat().st_mode & 0o777 if change.path.exists() else 0o644
        fd, temporary = tempfile.mkstemp(prefix=".harness-", dir=change.path.parent)
        try:
            with os.fdopen(fd, "wb") as stream:
                stream.write(change.content)
            os.chmod(temporary, mode)
            os.replace(temporary, change.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--apply", action="store_true", help="Apply the previewed installation")
    args = parser.parse_args()
    try:
        changes = plan_install(args.target)
        if (args.target / "AGENTS.override.md").exists():
            print("NOTE: AGENTS.override.md may shadow AGENTS.md. Review host instructions.")
        for change in changes:
            action = "create" if change.before is None else "append"
            print(f"{action}: {change.path.relative_to(args.target.resolve())}")
        if args.apply:
            apply_changes(changes)
            print(f"Installed {len(changes)} file(s). Start a new Codex session to check discovery.")
        else:
            print(f"Preview: {len(changes)} file(s); no writes. Add --apply to install.")
    except (ValueError, OSError, UnicodeError) as exc:
        parser.exit(1, f"Installation stopped: {exc}\n")


if __name__ == "__main__":
    main()
