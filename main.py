# The Wooden Spoon — a poem about agency, written by main.py
# Entry for make.fun "The poem about permission"
# (the-poem-about-permission-20261121-0235). Python 3.13, stdlib only,
# no network, no input. Writes the poem to /output/entry.txt.
"""Write one short original poem about agency to /output/entry.txt.

The poem is a fixed string literal authored for this entry: a child asks
to stir the soup, the mother hands over the wooden spoon handle-first
without saying yes, and the last lines reframe the gift as being trusted
with the making itself. Deterministic: every run writes byte-identical
output. The text is 269 Unicode characters, inside the 1-280 gate.
"""

from pathlib import Path

POEM = (
    "The Wooden Spoon\n"
    "\n"
    "At six, I asked my mother,\n"
    '"Can I stir the soup?"\n'
    "\n"
    "She did not answer. She lifted me\n"
    "onto the stool, and put\n"
    "the spoon in my hand, handle first.\n"
    "\n"
    "The pot was heavy. The steam\n"
    "rose like a held breath.\n"
    "That night, dinner tasted\n"
    "like it was mine to make."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
