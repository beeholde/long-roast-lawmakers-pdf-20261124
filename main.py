#!/usr/bin/env python3
"""Long Roast entry: one satirical sentence about lawmakers and the PDF.

Writes the line to /output/entry.txt (or $OUTPUT_DIR/entry.txt for local
runs). Gate: 1-320 characters, exactly one sentence, valid UTF-8, no
trailing newline. Shorter text wins ties, so the line is kept tight
(132 chars / 134 bytes at last check).
"""

import os
import sys

LINE = "The senator who wrote the law requiring every government document to be a PDF has filed his own bill as a Word document \u2014 six times."

MAX_CHARS = 320


def gate(line: str) -> str:
    """Reject anything the sealed scorer would refuse; return the cleaned line."""
    text = line.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(text)} chars / {len(text.encode('utf-8'))} bytes, "
            f"over the {MAX_CHARS} gate (fewer bytes wins ties)"
        )
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    return text


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = gate(LINE)
    data = text.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as fh:
        fh.write(data)
    print(f"wrote {len(data)} bytes / {len(text)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    sys.exit(main())
