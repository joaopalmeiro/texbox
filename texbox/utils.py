import json
from operator import itemgetter


def jprint(obj, indent=4, ensure_ascii=False):
    print(json.dumps(obj, indent=indent, ensure_ascii=ensure_ascii))


def split_irregular_list_of_lists(lst):
    strs, lists = [], []

    for item in lst:
        (lists, strs)[isinstance(item, str)].append(item)

    return strs, lists


def sort_list_of_lists(lst, *inner_idx):
    return sorted(lst, key=itemgetter(*inner_idx))
