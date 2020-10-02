from pathlib import Path

from .constants import Acronym, Term
from .parser import acronym_parser, acronym_writer
from .utils import natural_sort_list_of_lists, split_irregular_list_of_lists


def summary(acronyms, order="ascending"):
    n_acronyms = len(acronyms)

    print(
        f"✨ {Term.BOLD}{n_acronyms}{Term.END} acronyms sorted in {Term.BOLD}{order}{Term.END} order!"
    )


def main():
    parser = acronym_parser()

    path = Path("acronyms.tex")
    original_acronyms = path.read_text(encoding="utf-8")

    parsed_acronyms = parser.parseString(original_acronyms, parseAll=True).asList()

    comments, structured_acronyms = split_irregular_list_of_lists(parsed_acronyms)
    structured_acronyms = natural_sort_list_of_lists(
        structured_acronyms, Acronym["LABEL"]
    )

    output = acronym_writer(comments, structured_acronyms)

    path.write_text(output)

    summary(structured_acronyms)


if __name__ == "__main__":
    main()
