from enum import IntEnum

ACRONYM_MACRO = "\\newacronym"
COMMENT_CHAR = "%"
EMPTY_LINE = [""]
SUPPORTED_PUNCTUATION = "-.+"

ARGPARSE_DEFAULT = "(default: %(default)s)"

CITE_MACRO = "\\cite"
BEGIN_CENTER_MACRO = "\\begin{center}"
END_CENTER_MACRO = "\\end{center}"


class Term:
    BOLD = "\033[1m"
    END = "\033[0m"


class Acronym(IntEnum):
    LABEL = 0
    ABBRV = 1
    FULL = 2
