from pathlib import Path

from .parser import acronym_parser
from .utils import jprint, sort_list_of_lists, split_irregular_list_of_lists


def main():
    parser = acronym_parser()

    path = Path("acronyms.tex")
    original_acronyms = path.read_text(encoding="utf-8")

    parsed_acronyms = parser.parseString(original_acronyms)

    # jprint(parsed_acronyms.asList())

    comments, acronyms = split_irregular_list_of_lists(parsed_acronyms.asList())

    acronyms = sort_list_of_lists(acronyms, 0)

    jprint(acronyms)


if __name__ == "__main__":
    main()
