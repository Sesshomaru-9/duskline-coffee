#!/usr/bin/env python3
"""Duskline Coffee -- One Letter: Coffee or Tea.

Writes exactly one letter, "A" (coffee), to $MAKEFUN_OUTPUT_DIR/entry.txt
and nowhere else. Python 3.13, standard library only, deterministic,
no network access.
"""

import os
import sys

ENTRY = "A"


def _validate_entry(text: str) -> None:
    """The gate requires exactly one letter, A for coffee or B for tea."""
    if len(text) != 1 or text not in ("A", "B"):
        raise ValueError("entry must be exactly one letter, A or B")
    if text != ENTRY:
        raise ValueError("entry does not match the chosen letter")


def main() -> int:
    _validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    _validate_entry(open(path, encoding="utf-8").read())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
