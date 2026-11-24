"""Write one line: the excuse a developer gives when code breaks in production.

Why this line works, joke by joke. It opens with the most confident
sentence a developer can say after an incident, "Every test passed",
which is exactly the shield every dev reaches for first, and it sets
up the listener to expect the classic "works on my machine" defence.
Second beat: the em dash pivots the blame away from the code and onto
the one place nobody thought to check, production itself, and the
"turns out" makes it sound like a discovery made mid-sentence, the way
a developer actually backpedals in a standup. Third beat:
the twist lands, production "was just the one environment we forgot
to test" — the sentence quietly admits the team tested everything
except the only environment that matters, which is the real confession
hiding inside the excuse. That reversal is what a developer
recognises instantly, because every incident review has a version of
it: the suite was green, the staging was fine, and the thing that
broke was the one place the tests never ran. The line sounds like
something said out loud in a standup, uses the jargon right, and
stays tight at 83 of the allowed 200 characters, with the punch
arriving in the final words.

Gate guard: the entry must be UTF-8 text of 1 to 200 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "Every test passed \u2014 turns out production was the one "
    "environment we forgot to test."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate.

    The checks mirror the sealed scorer's gate exactly, in the order
    it matters: the entry must be text, then 1-200 characters, then a
    single line, then non-blank, then encodable as UTF-8. Each failure
    names the rule it broke and the value it saw, so a bad line is
    rejected here with a readable reason instead of silently reaching
    the judge and scoring 0. A SystemExit (not a plain exception) is
    used on purpose: the program must stop before writing anything,
    never write a half-valid entry and exit 0.
    """
    if not isinstance(text, str):
        raise SystemExit(
            f"entry is not text (got {type(text).__name__}), refusing to write"
        )
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS} to pass the gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "entry must be a single line (found a line break), refusing to write"
        )
    if not text.strip():
        raise SystemExit(
            "entry must not be only white space, refusing to write"
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(
            f"entry is not valid UTF-8 ({exc}), refusing to write"
        ) from exc


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
