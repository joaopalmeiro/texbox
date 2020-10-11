import json
from argparse import HelpFormatter


def jprint(obj, indent=4, ensure_ascii=False):
    print(json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii))


def split_irregular_list_of_lists(lst):
    strs, lists = [], []

    for item in lst:
        (lists, strs)[isinstance(item, str)].append(item)

    return strs, lists


def natural_sort_list_of_lists(lst, inner_idx, desc):
    return sorted(lst, key=lambda item: item[inner_idx].casefold(), reverse=desc)


# Source: https://stackoverflow.com/questions/18275023/dont-show-long-options-twice-in-print-help-from-argparse
class CustomHelpFormatter(HelpFormatter):
    # `-s, --long ARGS` instead of `-s ARGS, --long ARGS`
    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        else:
            default = self._get_default_metavar_for_optional(action)
            args_string = self._format_args(action, default)

            return ", ".join(action.option_strings) + " " + args_string


def str2list(string, sep=","):
    return string.split(sep)


def strs2str(*strings, sep="\n"):
    return sep.join(filter(None.__ne__, strings))


def identity(obj):
    return obj


def templatify_col_names(
    df, cols, template, placeholder="_PLACEHOLDER_", pre_col_transform=identity
):
    mapping = {
        col: template.replace(placeholder, pre_col_transform(col)) for col in cols
    }
    return df.rename(columns=mapping)


def is_multi_word_string(string):
    return len(string.split()) > 1


def templatify(template, value, placeholder="_PLACEHOLDER_"):
    return template.replace(placeholder, value)


def padify(string, fill_char=" ", pad_size=1):
    return string.center(len(string) + 2 * pad_size, fill_char)


# Source: https://toolz.readthedocs.io/en/latest/api.html#toolz.dicttoolz.valmap
def valmap(fn, dict_):
    updated_dict = dict()
    updated_dict.update(zip(dict_.keys(), map(fn, dict_.values())))

    return updated_dict


def dreplace(string, dict_):
    for key, value in dict_.items():
        string = string.replace(key, value)
    return string


def rreplace(s, old, new, occurrence=1):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def templatify_cell(cell, template):
    cell_elements = str2list(cell)
    templated_cell_elements = [
        templatify(template, cell_element.strip()) for cell_element in cell_elements
    ]

    return ", ".join(templated_cell_elements)
