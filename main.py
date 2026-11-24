#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes a single status page line (at most 160 characters) to
/output/entry.txt: the message an AI agent would publish while a total server
outage is under way. The line is the tournament winner: plain, first person,
specific about what is down, honest about what it does not know.
"""

import os

ENTRY = (
    "All user data is safe and completely unreachable. "
    "Logins, payments and search are down. "
    "I do not know when they return. I am still here."
)


def main() -> None:
    # Gate: the entry must be 1-160 characters of non-whitespace text.
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, gate is 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
