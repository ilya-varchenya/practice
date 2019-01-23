import re


def get_list_of_numbers_from_string(str_item):
    return re.findall(r'\b\d+\b', str_item)
