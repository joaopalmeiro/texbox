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
    return sep.join(strings)
