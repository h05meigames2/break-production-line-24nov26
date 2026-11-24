#!/usr/bin/env python3
"""Break Production, Own It — make.fun bounty entry.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt, after validating it: exactly one line, 1-200
characters, not only whitespace.
"""

import os
import sys

ENTRY_LINE = "I dropped the production database. The only backup was inside it. I did that."


def main() -> int:
    line = ENTRY_LINE

    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if not line.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(line) <= 200:
        print(f"error: entry must be 1-200 characters, got {len(line)}", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)

    # Verify the round trip: what landed on disk must be exactly the line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written entry does not match the validated line", file=sys.stderr)
        return 1

    print(f"wrote {len(line)} characters to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
