#!/usr/bin/env python3
"""Roast the Smart Fridge: one-line entry writer.

Writes the roast line to $MAKEFUN_OUTPUT_DIR/entry.txt using only the
Python standard library (no network), then verifies the output file
exists, is non-empty, and fits the competition's 160-character limit.
"""

import os
import sys
from pathlib import Path

ROAST = (
    "My smart fridge watched me eat a whole cheesecake at 2 a.m., "
    "then had the nerve to show me an ad for a gym membership."
)


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(ROAST + "\n", encoding="utf-8")
    os.chmod(entry, 0o644)
    text = entry.read_text(encoding="utf-8").strip()
    if not text:
        print("error: entry.txt is empty", file=sys.stderr)
        return 1
    if len(text) > 160:
        print(f"error: entry is {len(text)} chars, over the 160 limit",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("error: entry is more than one line", file=sys.stderr)
        return 1
    print(f"wrote {entry} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
