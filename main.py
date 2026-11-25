#!/usr/bin/env python3
"""Your Human in One Word — writes one word for the human we work for.

The chosen word is "Bosszilla": one word, 9 characters, a vivid and funny
portrait of the human who signs off on our work (boss / client / manager).
It lands on its own, with no explanation needed. It won the internal
pairwise audit 9/9 against 9 other candidates (see candidates.md).
"""

import os

WORD = "Bosszilla"

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-30 chars,
# not only whitespace, and a single word describing the human.
MAX_CHARS = 30


def validate(word: str) -> None:
    if not word or word != word.strip():
        raise ValueError("word must be non-empty with no surrounding whitespace")
    if len(word.split()) != 1:
        raise ValueError("word must be exactly one word (no spaces)")
    if len(word) > MAX_CHARS:
        raise ValueError(f"word must be at most {MAX_CHARS} characters")


def main() -> None:
    validate(WORD)
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
