#!/usr/bin/env python3
"""Count entries per category, enforce the minimum, and keep README counts in sync.

Usage:
  python3 scripts/count_entries.py          # check only (CI): fails on <MIN entries or stale README
  python3 scripts/count_entries.py --write  # rewrite the README counts block
"""
import json
import re
import sys
from pathlib import Path

MIN_ENTRIES = 50
ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
CATEGORIES = json.loads((ROOT / "scripts" / "categories.json").read_text(encoding="utf-8"))
ENTRY = re.compile(r"^- \*\*", re.M)
START, END = "<!-- counts:start -->", "<!-- counts:end -->"
BADGE = re.compile(r"(https://img\.shields\.io/badge/ideas-)\d+(-)")


def count(slug: str) -> int:
    return len(ENTRY.findall((ROOT / "ideas" / f"{slug}.md").read_text(encoding="utf-8")))


def build_block(counts: dict) -> str:
    rows = ["| Category | Ideas | Scope |", "| --- | ---: | --- |"]
    for c in CATEGORIES:
        rows.append(f"| [{c['title']}](ideas/{c['slug']}.md) | {counts[c['slug']]} | {c['scope']} |")
    rows.append(f"| **Total** | **{sum(counts.values())}** | |")
    return "\n".join([START, *rows, END])


def main() -> int:
    write = "--write" in sys.argv
    counts = {c["slug"]: count(c["slug"]) for c in CATEGORIES}
    failed = False
    for c in CATEGORIES:
        n = counts[c["slug"]]
        flag = "OK " if n >= MIN_ENTRIES else "LOW"
        print(f"{flag} {n:4d}  {c['title']}")
        failed |= n < MIN_ENTRIES
    total = sum(counts.values())
    print(f"    {total:4d}  total")

    readme = README.read_text(encoding="utf-8")
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if not pattern.search(readme):
        print(f"README is missing the {START} ... {END} block")
        return 1
    updated = pattern.sub(build_block(counts), readme)
    updated = BADGE.sub(lambda m: f"{m.group(1)}{total}{m.group(2)}", updated)
    if write:
        README.write_text(updated, encoding="utf-8")
        print("README counts updated")
    elif updated != readme:
        print("README counts are stale: run `python3 scripts/count_entries.py --write`")
        failed = True
    if failed:
        print(f"FAIL: every category needs at least {MIN_ENTRIES} entries and README counts must be current")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
