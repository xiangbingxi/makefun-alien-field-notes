"""Write the alien field-notes entry to /output/entry.txt.

Reads the file back after writing and fails loudly if even one
character differs from ENTRY, so a bad write can never pass silently.
"""

import os
import sys

ENTRY = "Earth, 4/5: They charge for water but give you as much gravity as you want, which feels like an oversight."


def main():
    if not 1 <= len(ENTRY) <= 200:
        print(f"ENTRY is {len(ENTRY)} characters, outside the 1-200 limit", file=sys.stderr)
        sys.exit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("MISMATCH: /output/entry.txt differs from ENTRY", file=sys.stderr)
        print(f"expected: {ENTRY!r}", file=sys.stderr)
        print(f"got:      {written!r}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
