from enum import IntEnum

ACRONYM_MACRO = "\\newacronym"
COMMENT_CHAR = "%"
EMPTY_LINE = [""]
SUPPORTED_PUNCTUATION = "-.+"


class Term:
    BOLD = "\033[1m"
    END = "\033[0m"


class Acronym(IntEnum):
    LABEL = 0
    ABBREV = 1
    FULL = 2
