#!/usr/bin/env python3
"""Fail on duplicate or near-duplicate ideas across the whole list.

Checks:
  * exact duplicate titles (case/punctuation-insensitive) across all categories
  * duplicate repos in Fork Suggestions
  * near-duplicate titles (similarity >= TITLE_THRESHOLD) -> error
  * near-duplicate pitches (similarity >= PITCH_THRESHOLD) -> warning for human review
  * entry format: every idea has Why + Difficulty lines (and Stack or Licence)
"""
import itertools
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TITLE_THRESHOLD = 0.9
PITCH_THRESHOLD = 0.8
ENTRY = re.compile(r"^- \*\*(?P<title>.+?)\*\*: (?P<pitch>.+?)\n(?P<body>(?:  - .+\n?)+)", re.M)
LINK = re.compile(r"^\[(?P<text>[^\]]+)\]\([^)]+\)$")


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def similar(a: str, b: str, threshold: float) -> bool:
    sm = SequenceMatcher(None, a, b)
    return sm.real_quick_ratio() >= threshold and sm.quick_ratio() >= threshold and sm.ratio() >= threshold


def main() -> int:
    entries = []
    errors = []
    for path in sorted((ROOT / "ideas").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        found = list(ENTRY.finditer(text))
        raw = len(re.findall(r"^- \*\*", text, re.M))
        if raw != len(found):
            errors.append(f"{path.name}: {raw - len(found)} entries do not match the entry format")
        for m in found:
            title = m["title"]
            link = LINK.match(title)
            if link:
                title = link["text"]
            body = m["body"]
            if "**Why:**" not in body or "**Difficulty:**" not in body:
                errors.append(f"{path.name}: '{title}' is missing Why or Difficulty")
            if "**Stack:**" not in body and "**Licence:**" not in body:
                errors.append(f"{path.name}: '{title}' is missing Stack (or Licence for forks)")
            entries.append((path.name, title, m["pitch"]))

    seen = {}
    for f, title, _ in entries:
        key = norm(title)
        if key in seen:
            errors.append(f"duplicate title '{title}' in {f} and {seen[key]}")
        seen[key] = f

    warnings = []
    for (f1, t1, p1), (f2, t2, p2) in itertools.combinations(entries, 2):
        if norm(t1) == norm(t2):
            continue
        if similar(norm(t1), norm(t2), TITLE_THRESHOLD):
            errors.append(f"near-duplicate titles: '{t1}' ({f1}) vs '{t2}' ({f2})")
        if similar(norm(p1), norm(p2), PITCH_THRESHOLD):
            warnings.append(f"similar pitches: '{t1}' ({f1}) vs '{t2}' ({f2})")

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    print(f"{len(entries)} entries checked, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
