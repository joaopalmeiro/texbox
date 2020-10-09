import argparse
from pathlib import Path

import pandas as pd

from .constants import BEGIN_CENTER_MACRO, CITE_MACRO, END_CENTER_MACRO
from .utils import CustomHelpFormatter, str2list, strs2str


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a LaTeX table from a bibliography-based file.",
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
        help="The path to the file to be tabulated.",
        metavar="PATH",
        type=str,
        dest="input_path",
    )

    required.add_argument(
        "-o",
        "--output",
        required=True,
        help="The path to the file for the generated LaTeX table.",
        metavar="PATH",
        type=str,
        dest="output_path",
    )

    required.add_argument(
        "-ck",
        "--cite-key-col",
        required=True,
        help="The column name for the cite key.",
        metavar="COL",
        type=str,
    )

    required.add_argument(
        "-t",
        "--title-col",
        required=True,
        help="The column name for the title.",
        metavar="COL",
        type=str,
    )

    optional.add_argument(
        "-c",
        "--cols",
        help="The subset of columns to maintain. By default, all columns are kept except the title column.",
        metavar="COLS",
        type=str,
        default=None,
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    if args.cols is None:
        df = pd.read_csv(args.input_path)
        df = df.drop(columns=args.title_col)
    else:
        cols = str2list(args.cols) + [args.cite_key_col]
        df = pd.read_csv(args.input_path, usecols=cols)

    df = df.rename(columns={args.cite_key_col: args.title_col})
    df[args.title_col] = CITE_MACRO + "{" + df[args.title_col] + "}"

    output_path = Path(args.output_path)

    output_path.write_text(
        strs2str(
            BEGIN_CENTER_MACRO,
            df.to_latex(index=False, escape=False).strip(),
            END_CENTER_MACRO,
        )
    )


if __name__ == "__main__":
    main()
