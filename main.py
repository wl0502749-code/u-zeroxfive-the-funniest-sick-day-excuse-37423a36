#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes a single original one-line sick-day excuse to /output/entry.txt.
The line must be 1-200 UTF-8 characters, one line, nothing else.
"""

import os
from pathlib import Path

EXCUSE = (
    "Can't come in today \u2014 I sneezed so hard I pulled a muscle "
    "I didn't know I had, and now I walk like a folding chair. "
    "Please don't make me prove it at the office."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "excuse must be a single line"
    (output_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
