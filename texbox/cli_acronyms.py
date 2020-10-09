import argparse
from pathlib import Path

from .constants import ARGPARSE_DEFAULT, Acronym, Term
from .parser import acronym_parser, acronym_writer
from .utils import (
    CustomHelpFormatter,
    natural_sort_list_of_lists,
    split_irregular_list_of_lists,
)


def summary(acronyms, desc):
    n_acronyms = len(acronyms)
    order = "descending" if desc else "ascending"

    print(
        f"✨ {Term.BOLD}{n_acronyms}{Term.END} acronyms sorted in {Term.BOLD}{order}{Term.END} order!"
    )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sort acronyms from an `acronyms.tex` file.",
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )

    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    optional = parser.add_argument_group("optional arguments")

    required.add_argument(
        "-i",
        "--input",
        required=True,
        help="The path to the `acronyms.tex` file to be sorted.",
        metavar="PATH",
        type=str,
        dest="input_path",
    )

    optional.add_argument(
        "-b",
        "--by",
        help=f"Macro argument name to sort by. {ARGPARSE_DEFAULT}",
        choices=["label", "abbrv", "full"],
        default="label",
        type=str,
    )

    optional.add_argument(
        "-d",
        "--descending",
        help="Sort descending instead of ascending.",
        action="store_true",
        dest="desc",
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    path = Path(args.input_path)
    original_acronyms = path.read_text(encoding="utf-8")

    parser = acronym_parser()
    parsed_acronyms = parser.parseString(original_acronyms, parseAll=True).asList()

    comments, structured_acronyms = split_irregular_list_of_lists(parsed_acronyms)
    structured_acronyms = natural_sort_list_of_lists(
        structured_acronyms, Acronym[args.by.upper()], args.desc
    )

    output = acronym_writer(comments, structured_acronyms)

    path.write_text(output)

    summary(structured_acronyms, args.desc)


if __name__ == "__main__":
    main()
