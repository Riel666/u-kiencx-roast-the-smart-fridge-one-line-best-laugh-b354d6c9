#!/usr/bin/env python3
"""Roast the Smart Fridge: one-line entry writer.

Writes a single-line roast of a smart fridge to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the variable
is unset), as the competition requires. Python 3, standard library only,
no network, fully deterministic.
"""

import os

ENTRY = "My smart fridge logs every midnight snack, tattles to my phone, and still needs a firmware update to make ice — the most expensive snitch in my kitchen."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "entry must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
