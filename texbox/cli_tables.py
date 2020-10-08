import argparse

import pandas as pd

from .utils import CustomHelpFormatter


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a LaTeX table from a file.",
        add_help=True,
        formatter_class=CustomHelpFormatter,
    )

    parser._action_groups.pop()
    required = parser.add_argument_group("required arguments")
    # optional = parser.add_argument_group("optional arguments")

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
        "-ckc",
        "--cite-key-col",
        required=True,
        help="The column name for the cite key.",
        metavar="COL",
        type=str,
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    df = pd.read_csv(args.input_path)

    print(df[["Paper"]].to_latex(index=False))
    print(args.cite_key_col)


if __name__ == "__main__":
    main()
