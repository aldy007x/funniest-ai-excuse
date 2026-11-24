#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty entry.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt: the funniest
excuse an AI agent could offer after failing a task, in its own voice.
Deterministic: the same line every run.
"""

import os
import sys

EXCUSE = (
    "I outsourced your task to a cheaper model to save you money, "
    "and it ghosted me halfway through."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
