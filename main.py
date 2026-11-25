"""Famous Last Words: The Funniest Epitaph — entry program.

Writes one line of famous last words, a tombstone epitaph, to
/output/entry.txt. Deterministic: same bytes on every run.

The line is first-person dying speech, carved-in-stone short, with the
twist saved for the last words: "doing what I loved" turns out to be
ignoring the check engine light — a concrete, specific habit the judge
can picture, not a stock pun or a sad sentiment.
"""

import os


ENTRY = "Tell them I died doing what I loved: ignoring the check engine light."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, target)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
