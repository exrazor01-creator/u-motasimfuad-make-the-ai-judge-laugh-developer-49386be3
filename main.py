#!/usr/bin/env python3
"""Entry for Make the AI Judge Laugh: Developer Excuses.

Writes a single-line developer excuse (at most 200 characters) to
/output/entry.txt and prints it to stdout. Pure standard library.
"""

import os

EXCUSE = "The code worked on my machine, so I shipped my machine: it is now running production from under my desk, and the cat just sat on the power button."

def main():
    assert 1 <= len(EXCUSE) <= 200, f"excuse length {len(EXCUSE)} out of range"
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "excuse must be a single line"
    assert EXCUSE.strip(), "excuse must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)

if __name__ == "__main__":
    main()
