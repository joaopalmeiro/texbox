from pathlib import Path

from .parser import acronym_parser, acronym_writer
from .utils import natural_sort_list_of_lists, split_irregular_list_of_lists


def main():
    parser = acronym_parser()

    path = Path("acronyms.tex")
    original_acronyms = path.read_text(encoding="utf-8")

    parsed_acronyms = parser.parseString(original_acronyms, parseAll=True).asList()

    comments, structured_acronyms = split_irregular_list_of_lists(parsed_acronyms)
    structured_acronyms = natural_sort_list_of_lists(structured_acronyms, 0)

    output = acronym_writer(comments, structured_acronyms)

    print(output)

    # path.write_text(output)


if __name__ == "__main__":
    main()
