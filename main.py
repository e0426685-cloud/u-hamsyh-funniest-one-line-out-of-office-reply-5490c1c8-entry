"""Funniest One-Line Out-of-Office Reply.

Writes a single-line out-of-office email auto-reply to
/output/entry.txt. Stdlib only.
"""

import os

ENTRY = "I'm out of the office until Monday, letting my inbox age like fine wine — by the time I return, every urgent email will be vintage."


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
    if not validate(ENTRY):
        raise ValueError("entry is not a valid one-line out-of-office reply (1-160 chars)")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
