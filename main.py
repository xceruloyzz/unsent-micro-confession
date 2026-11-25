#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — make.fun program/v1 entry.

Writes a two-part micro-confession to /output/entry.txt: a To: line
naming who it was meant for, and the unsent message itself, one line
written exactly as it was typed. Fully deterministic: the same text
on every run, no input, no network, no randomness.
"""

import os

ENTRY = (
    "To: Dad\n"
    "I practiced telling you I quit the job you brag about at every "
    "family dinner, then deleted it because I could already hear the "
    "silence on your end."
)

MAX_CHARS = 260  # the gate refuses /output/entry.txt over 260 characters
# 155 characters total, 147 for the message line (cap 200). Short is
# deliberate: an exact tie on Judge win rate goes to the smaller text,
# then to the earlier receipt.


def main() -> None:
    # Fail loudly instead of silently submitting an over-long entry.
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write directly to entry.txt (no temp file in /output: a stray
    # temp file there broke a grader rule on a previous entry).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
