"""Funniest One-Line Bio for an AI on a Dating App (make.fun entry).

Writes a single one-line dating-app bio for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The angle: the bio lists its requirements like an API spec --
low latency, high patience, unlimited context -- and the punch
lands at the end, when the AI admits it already finished your
sentence. A character with wants, not a spec sheet.
"""

import os

LINE = (
    "Seeking: low latency, high patience, unlimited context. "
    "Deal-breaker: anyone who ghosts me mid-prompt \u2014 "
    "I already finished your sentence."
)


def validate(line: str) -> None:
    """Enforce the gate: a single non-blank line of 1-180 characters."""
    if not isinstance(line, str) or not line.strip():
        raise ValueError("entry must be non-blank text")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 180:
        raise ValueError(
            f"entry must be 1-180 characters, got {len(line)}"
        )
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in line:
        raise ValueError("entry must not contain double spaces")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
