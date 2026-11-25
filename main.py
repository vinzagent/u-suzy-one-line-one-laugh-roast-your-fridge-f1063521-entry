"""Roast Your Fridge — one-line roast entry.

Writes the single-line fridge roast (109 characters, no trailing
newline) to /output/entry.txt and echoes it to stdout. The entry
text is fixed and must stay byte-identical; this module only
handles how it is written out.
"""

import os
import sys

ENTRY = "My fridge freezes the lettuce, warms the ice cream, and hums like it's proud of itself. One job, zero talent."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write ENTRY to ``path`` and make it world-readable.

    Creates the output directory first. Any filesystem failure is
    reported on stderr and re-raised so a broken write is never
    silently swallowed.
    """
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
    except OSError as exc:
        sys.stderr.write(f"failed to write {path}: {exc}\n")
        raise


def main():
    write_entry()
    sys.stdout.write(ENTRY)


if __name__ == "__main__":
    main()
