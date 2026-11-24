"""Write the make.fun dad joke entry to entry.txt.

The whole entry is one short text. It is written as UTF-8 bytes with no
trailing newline, into MAKEFUN_OUTPUT_DIR when that is set, else /output.
"""

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for "
    "it. The waiter said, 'Sir, that's not how well done works.'"
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    entry = out_dir / "entry.txt"
    with open(entry, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(f"{len(TEXT)} characters written to {entry}", file=sys.stderr)


if __name__ == "__main__":
    main()
