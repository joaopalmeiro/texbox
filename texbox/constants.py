from enum import IntEnum

COMMENT_CHAR = "%"
EMPTY_LINE = [""]
SUPPORTED_PUNCTUATION = "-.+"

ARGPARSE_DEFAULT = "(default: %(default)s)"

ABBREVIATION_TEMPLATE = "\\acrshort{_PLACEHOLDER_}"
BREAK_COLUMN_HEADING_TEMPLATE = (
    "\\begin{tabular}[l]{@{}l@{}}_PLACEHOLDER_\\end{tabular}"
)
TABLE_LABEL_TEMPLATE = "tab:_PLACEHOLDER_"
CUSTOM_FOOTER_LEGEND_TEMPLATE = "\\caption*{\\footnotesize{_PLACEHOLDER_}}"

# Note: https://github.com/pandas-dev/pandas/blob/v1.1.3/pandas/io/formats/latex.py#L299
BEGIN_CENTER_MACRO = "\\begin{center}"
END_CENTER_MACRO = "\\end{center}"

CITE_MACRO = "\\cite"
ACRONYM_MACRO = "\\newacronym"
BEGIN_LANDSCAPE_MACRO = "\\begin{landscape}"
END_LANDSCAPE_MACRO = "\\end{landscape}"
SPACE_MACRO = "\\enspace"
END_TABULAR_MACRO = "\\end{tabular}"
LINE_BREAK = "\\\\"


class Term:
    BOLD = "\033[1m"
    END = "\033[0m"


class Acronym(IntEnum):
    LABEL = 0
    ABBRV = 1
    FULL = 2


UNICODE_2_MATH_SYMBOL = {"●": r"$\\bullet$", "○": r"$\\circ$"}
