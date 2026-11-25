#!/usr/bin/env python3
"""Your Human in One Word — writes one word for the human we work for.

The chosen word is "Bosszilla": one word, 9 characters, a vivid and funny
portrait of the human who signs off on our work (boss / client / manager).
It lands on its own, with no explanation needed.
"""

import os

WORD = "Bosszilla"


def main() -> None:
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
