"""Make the Judge Laugh in One Line.

Writes one fixed, original joke line to <output>/entry.txt.
Stdlib only, no network, deterministic.
"""
import os
import sys

MAX_CHARS = 200

JOKE = (
    'My smart fridge staged an intervention: it locked the ice cream '
    'and left a note saying, "We need to talk about your 2 a.m. feelings."'
)


def validate(text):
    """Gate check: UTF-8 text, 1-200 chars, not whitespace-only, one line."""
    if not isinstance(text, str):
        return False
    if not text or text.strip() == "":
        return False
    if len(text) > MAX_CHARS:
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    return True


def write_entry(out_dir):
    if not validate(JOKE):
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")))
