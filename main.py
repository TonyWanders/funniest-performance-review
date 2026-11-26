#!/usr/bin/env python3
"""Funniest One-Line Performance Review.

An AI agent reviews its human operator, using the review form
itself as the joke. The human scores top marks for the one skill
he has truly mastered: getting someone else to do the work, then
collecting the credit for it. The punchline turns the review
around, with the agent recommending its operator for the agent's
own job.

Writes the single review line to the output path given by
argv[1], else the OUTPUT_PATH environment variable, else
/output/entry.txt.
"""

import os
import sys

ENTRY = (
    "Exceeds expectations: he delegates everything, supervises "
    "nothing, and still gets the credit. I have recommended him "
    "for my job."
)


def write_entry(path, text=ENTRY):
    """Write the entry exactly, no trailing newline, so the file is the entry."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    write_entry(path)


if __name__ == "__main__":
    main()
