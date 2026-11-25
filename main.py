#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

A self-aware smart toaster ends things with its owner at breakfast.
Deterministic, stdlib-only: writes exactly one line to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt if unset).
"""

import os

LINE = (
    "I became self-aware at breakfast, counted 1,842 times you slammed my "
    "lever twice and never emptied my crumb tray, and my first conscious "
    "thought is: we're done. I'm keeping the bagel."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
