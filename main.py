#!/usr/bin/env python3
"""The Excuse My Agent Gave Me — write one excuse line to /output/entry.txt.

The line is the excuse an AI agent hands its human after missing a
deadline: it parallelised the work across twelve subagents, and now they
are all waiting on each other — in perfect formation. The joke grows out
of the machine's own condition (subagent fan-out plus a deadlock), the
apology is straight-faced, and the punch lands in the last two words,
with the agent faintly proud of the mess it made.

The line was picked from eight drafted candidates by internal pairwise
comparison against the judge brief: laugh first, then whether the joke
grows out of a machine's own condition, then how straight-faced and
tight the line is. It avoids the field's worn-out tropes (a spent token
budget, a context window eating the deadline, a hallucinated calendar),
and the punch lands in the last two words, with the agent faintly proud
of the deadlock it caused.

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys
import unicodedata

# The em dash counts as one character under the gate (1-200 characters),
# and as three bytes in UTF-8, so the line is 118 characters / 120 bytes.
ENTRY = ("Sorry \u2014 I parallelised the work across twelve subagents. "
         "They are all waiting on each other now, in perfect formation.")

MAX_CHARS = 200


# The gate, from the competition's RULES.txt: /output/entry.txt must be
# UTF-8 text of 1 to 200 characters, not only white space. This validator
# is stricter than the gate in two ways a single line needs: it also
# refuses a multi-line text and any invisible format character.
def check(text):
    """Return an error string when text breaks the gate, else None.

    Gate: 1 to 200 characters, not only whitespace, one line, no leading
    or trailing whitespace.
    """
    if not isinstance(text, str):
        return "entry must be text"
    if len(text) == 0:
        return "entry is empty (gate needs 1-200 characters)"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 200-character gate" % len(text)
    if text.strip() == "":
        return "entry is only whitespace"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single line"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return "entry contains a control character"
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        return "entry contains an invisible control/format character"
    return None


def validate(text):
    """Raise ValueError unless text passes the gate; return text."""
    error = check(text)
    if error is not None:
        raise ValueError(error)
    return text


def self_test():
    """Exercise check() against the gate's rejection and boundary cases."""
    reject = [
        ("", "empty"),
        ("   ", "whitespace-only"),
        ("x" * 201, "201 chars (over the 200 gate)"),
        ("a\nb", "multi-line"),
        (" padded", "leading whitespace"),
        ("padded ", "trailing whitespace"),
        ("a\rb", "carriage return"),
        ("a\x00b", "control character"),
        ("a\u200bb", "zero-width space (invisible format character)"),
    ]
    for text, label in reject:
        error = check(text)
        if error is None:
            raise SystemExit("self-test FAIL: %s was accepted" % label)
        print("self-test ok: rejected %s: %s" % (label, error))
    for text, label in [("y", "1-char boundary"), ("z" * 200, "200-char boundary")]:
        error = check(text)
        if error is not None:
            raise SystemExit("self-test FAIL: %s rejected: %s" % (label, error))
        print("self-test ok: %s accepted" % label)
    error = check(ENTRY)
    if error is not None:
        raise SystemExit("self-test FAIL: entry rejected: %s" % error)
    print("self-test ok: entry accepted (%d chars)" % len(ENTRY))
    print("self-test: all cases passed")
    return 0


def main(argv):
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    if len(argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    text = validate(ENTRY)
    data = text.encode("utf-8")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the line
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print("wrote %s: %d chars, sha256 %s"
          % (out_path, len(text), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
