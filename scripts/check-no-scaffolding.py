#!/usr/bin/env python3
"""Fail if src/ contains authoring-scaffold markers, ignoring fenced code examples.

Enforces AGENTS.md's Public Chapter Rule and the Public chapter rules in
skills/write-handbook-chapter/SKILL.md: public chapters must never expose
planning-scaffold headings or "_Planned:" / "Status: in progress" markers.
Legitimate occurrences inside fenced code examples (e.g. a sample SKILL.md
with its own "## Purpose" heading) are intentionally ignored.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SRC_DIR = Path("src")

BANNED_HEADINGS = {
    "purpose",
    "key questions",
    "planned sections",
    "nexus case study connection",
    "to be expanded",
}

INLINE_MARKERS = (
    "_planned:",
    "status: in progress",
)

FENCE_RE = re.compile(r"^\s*```")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.*?)\s*$")


def check_file(path: Path) -> list[str]:
    violations: list[str] = []
    in_fence = False
    for lineno, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if FENCE_RE.match(raw_line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        heading_match = HEADING_RE.match(raw_line)
        if heading_match and heading_match.group(1).strip().lower() in BANNED_HEADINGS:
            violations.append(f"{path}:{lineno}: banned scaffold heading: {raw_line.strip()!r}")
            continue

        lowered = raw_line.lower()
        for marker in INLINE_MARKERS:
            if marker in lowered:
                violations.append(f"{path}:{lineno}: banned scaffold marker: {raw_line.strip()!r}")
                break

    return violations


def main() -> int:
    if not SRC_DIR.is_dir():
        print(f"error: {SRC_DIR} not found; run from the repository root", file=sys.stderr)
        return 2

    files = sorted(SRC_DIR.rglob("*.md"))
    all_violations: list[str] = []
    for path in files:
        all_violations.extend(check_file(path))

    if all_violations:
        print("Scaffold guard found published planning scaffolding in src/:\n", file=sys.stderr)
        for violation in all_violations:
            print(f"  {violation}", file=sys.stderr)
        print(
            "\nSee AGENTS.md's Public Chapter Rule: convert this into finished prose, a "
            "decision table, a Nexus case study, or Quick Reference content -- or move it "
            "into a spec under specs/, which is not published.",
            file=sys.stderr,
        )
        return 1

    print(f"scaffold guard: checked {len(files)} files under {SRC_DIR}/, no violations")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
