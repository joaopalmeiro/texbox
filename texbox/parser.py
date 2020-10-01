import pyparsing as pp

from .constants import ACRONYM_MACRO, COMMENT_CHAR, SUPPORTED_PUNCTUATION


def acronym_parser():
    label_or_abbrv = (
        pp.Suppress("{")
        + pp.Word(pp.alphanums + SUPPORTED_PUNCTUATION)
        + pp.Suppress("}")
    )

    full = (
        pp.Suppress("{")
        + pp.Combine(
            pp.OneOrMore(pp.Word(pp.alphanums + SUPPORTED_PUNCTUATION) | pp.White(" "))
        )
        + pp.Suppress("}")
    )

    acronym = pp.Group(pp.Suppress(ACRONYM_MACRO) + label_or_abbrv * 2 + full)

    comment = pp.originalTextFor(
        pp.Char(COMMENT_CHAR)
        + pp.Combine(pp.OneOrMore(pp.Word(pp.printables) | pp.White(" ")))
    )

    return pp.ZeroOrMore(comment | acronym)
