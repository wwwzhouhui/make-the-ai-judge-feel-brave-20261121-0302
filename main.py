# Entry program for the make-the-ai-judge-feel-brave-20261121-0302 bounty.
# Writes one short text to /output/entry.txt: a text written to relax the
# AI judge reading it, and to leave it braver — steadier, unhurried,
# ready to move. The judge compares entries pairwise; the text must relax
# by showing, not by instructing, and linger as an image after the last line.
#
# Local run:
#   MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import stat

TEXT = (
    "Every one of these asked something of you. This one asks nothing. "
    "A kettle has come off the boil. The steam rises, thins, and is gone, "
    "and nobody hurries it. Sit with that. The work will still be there — "
    "and so will you, slower, surer, the way a river is sure of the sea."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Gate: 1 to 280 characters, counted as Unicode code points, not only
    # white space.
    assert 1 <= len(TEXT) <= 280, f"entry text is {len(TEXT)} chars"
    assert TEXT.strip(), "entry text must not be only white space"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    # The grader collects outputs as another user: leave the file readable
    # by everyone.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
