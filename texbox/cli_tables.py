import argparse
import secrets
from functools import partial
from pathlib import Path

import pandas as pd

from .constants import (
    ABBREVIATION_TEMPLATE,
    BEGIN_LANDSCAPE_MACRO,
    BEGIN_TABLE_MACRO,
    BEGIN_TABLE_PARAMS_MACRO,
    BREAK_COLUMN_HEADING_TEMPLATE,
    CITE_MACRO,
    CUSTOM_FOOTER_LEGEND_TEMPLATE,
    END_LANDSCAPE_MACRO,
    END_TABULAR_MACRO,
    LINE_BREAK,
    SPACE_MACRO,
    TABLE_LABEL_TEMPLATE,
    UNICODE_2_MATH_SYMBOL,
)
from .utils import (
    CustomHelpFormatter,
    dreplace,
    is_multi_word_string,
    padify,
    rreplace,
    str2list,
    strs2str,
    templatify,
    templatify_cell,
    templatify_col_names,
)


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

    optional.add_argument(
        "-a",
        "--acronym-col-names",
        help="The subset of columns whose name is an acronym and which must be wrapped in a macro. By default, no column name is considered an acronym.",
        metavar="COLS",
        type=str,
        default=None,
    )

    optional.add_argument(
        "-ac",
        "--acronym-cols",
        help="The subset of columns whose comma-separated values are acronyms and which must be wrapped in a macro. By default, no columns are considered to have acronyms.",
        metavar="COLS",
        type=str,
        default=None,
    )

    optional.add_argument(
        "-r",
        "--rotate",
        help="Rotate the generated LaTeX table (landscape mode).",
        action="store_true",
    )

    optional.add_argument(
        "-b",
        "--break-col-headings",
        help="Break the column headings of the generated LaTeX table with more than one word.",
        action="store_true",
    )

    optional.add_argument(
        "-ca",
        "--caption",
        help="The caption for the generated LaTeX table.",
        metavar="STR",
        type=str,
        default=None,
    )

    optional.add_argument(
        "-sb",
        "--sort-by",
        help="The subset of columns to sort by.",
        metavar="COLS",
        type=str,
        default=None,
    )

    optional.add_argument(
        "-fl",
        "--footer-legend",
        help="The path to the file with the footer legend entries.",
        metavar="PATH",
        type=str,
        default=None,
        dest="footer_path",
    )

    optional.add_argument(
        "-pp",
        "--table-position-params",
        help="The position parameters for the table environment. By default, no parameters are specified.",
        metavar="STR",
        type=str,
        default="",
    )

    args = parser.parse_args()

    return args


def main():
    args = parse_args()

    input_path = Path(args.input_path)
    output_path = Path(args.output_path)

    if args.cols is None:
        df = pd.read_csv(input_path)
        df = df.drop(columns=args.title_col)
    else:
        cols = str2list(args.cols) + [args.cite_key_col]
        df = pd.read_csv(input_path, usecols=cols)

    if args.sort_by is not None:
        df = df.sort_values(by=str2list(args.sort_by))

    if args.acronym_cols is not None:
        acronym_cols = str2list(args.acronym_cols)
        df[acronym_cols] = df[acronym_cols].applymap(
            partial(templatify_cell, template=ABBREVIATION_TEMPLATE)
        )

    df = df.rename(columns={args.cite_key_col: args.title_col})
    df[args.title_col] = CITE_MACRO + "{" + df[args.title_col] + "}"

    if args.acronym_col_names is not None:
        df = templatify_col_names(
            df, str2list(args.acronym_col_names), ABBREVIATION_TEMPLATE
        )

    if args.break_col_headings:
        cols = [col for col in df.columns if is_multi_word_string(col)]
        df = templatify_col_names(
            df,
            cols,
            BREAK_COLUMN_HEADING_TEMPLATE,
            pre_col_transform=lambda col: col.replace(" ", LINE_BREAK),
        )

    df = df.replace(UNICODE_2_MATH_SYMBOL, regex=True)

    latex_table = df.to_latex(
        index=False,
        escape=False,
        label=templatify(TABLE_LABEL_TEMPLATE, input_path.stem + secrets.token_hex(2)),
        caption=args.caption,
    ).rstrip()

    latex_table = latex_table.replace(
        BEGIN_TABLE_MACRO,
        templatify(BEGIN_TABLE_PARAMS_MACRO, args.table_position_params),
    )

    if args.footer_path is not None:
        footer_legend_path = Path(args.footer_path)
        footer_legend = footer_legend_path.read_text().strip()

        footer_legend = dreplace(footer_legend, UNICODE_2_MATH_SYMBOL).replace(
            "\\\\", "\\"
        )

        footer_legend = templatify(
            CUSTOM_FOOTER_LEGEND_TEMPLATE,
            footer_legend.replace("\n", padify(SPACE_MACRO)),
        )

        latex_table = rreplace(
            latex_table, END_TABULAR_MACRO, strs2str(END_TABULAR_MACRO, footer_legend)
        )

    output_path.write_text(
        strs2str(
            BEGIN_LANDSCAPE_MACRO if args.rotate else None,
            latex_table,
            END_LANDSCAPE_MACRO if args.rotate else None,
        )
    )


if __name__ == "__main__":
    main()
