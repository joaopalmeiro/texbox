from enum import IntEnum

ACRONYM_MACRO = "\\newacronym"
COMMENT_CHAR = "%"
EMPTY_LINE = [""]
SUPPORTED_PUNCTUATION = "-.+"

ARGPARSE_DEFAULT = "(default: %(default)s)"

CITE_MACRO = "\\cite"
ABBREVIATION_TEMPLATE = "\\acrshort{_PLACEHOLDER_}"
BREAK_COLUMN_HEADING_TEMPLATE = (
    "\\begin{tabular}[l]{@{}l@{}}_PLACEHOLDER_\\end{tabular}"
)
LINE_BREAK = "\\\\"

BEGIN_CENTER_MACRO = "\\begin{center}"
END_CENTER_MACRO = "\\end{center}"
BEGIN_LANDSCAPE_MACRO = "\\begin{landscape}"
END_LANDSCAPE_MACRO = "\\end{landscape}"


class Term:
    BOLD = "\033[1m"
    END = "\033[0m"


class Acronym(IntEnum):
    LABEL = 0
    ABBRV = 1
    FULL = 2


UNICODE_2_MATH_SYMBOL = {"●": r"$\\bullet$", "○": r"$\\circ$"}
