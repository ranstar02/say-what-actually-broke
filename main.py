#!/usr/bin/env python3
"""Say What Actually Broke — one line of honest error copy.

Writes a single line of software error copy to /output/entry.txt.

Deterministic, Python standard library only: no network access, no model
calls, no randomness. Running it twice produces byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "Save failed \u2014 the disk is full, so your masterpiece is still floating "
    "in memory. Delete something old, then save again before it forgets you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Fail loudly instead of writing an entry the gate would reject:
    # one line, 1-200 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry is {len(ENTRY)} characters, must be 1-200")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
