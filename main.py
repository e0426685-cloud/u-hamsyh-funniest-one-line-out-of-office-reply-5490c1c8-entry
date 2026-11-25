"""Funniest One-Line Out-of-Office Reply.

Writes a single-line out-of-office email auto-reply to
/output/entry.txt. Stdlib only.

Usage:
    python3 main.py

The entry is one line of 1-160 characters. The program validates the
line before writing it, creates the output directory if it is
missing, and writes the file world-readable (mode 0644) so the
grader can read it.
"""

import os

ENTRY = "I'm out of the office until Monday, letting my inbox age like fine wine — by the time I return, every urgent email will be vintage."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path, text):
    """Validate text, then write it to path and return its character count."""
    if not validate(text):
        raise ValueError("entry is not a valid one-line out-of-office reply (1-160 chars)")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return len(text)


def validate(text):
    """Return True only if text is a valid one-line entry (1-160 chars)."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 160):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(c) < 32 for c in text):
        return False
    return True


def main():
    count = write_entry(OUTPUT_PATH, ENTRY)
    print(f"wrote {count}-character out-of-office reply to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
