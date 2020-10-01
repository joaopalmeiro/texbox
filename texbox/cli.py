from pathlib import Path

from .parser import acronym_parser
from .utils import jprint


def main():
    parser = acronym_parser()

    path = Path("acronyms.tex")
    original_acronyms = path.read_text(encoding="utf-8")

    parsed_acronyms = parser.parseString(original_acronyms)

    jprint(parsed_acronyms.asList())


if __name__ == "__main__":
    main()
