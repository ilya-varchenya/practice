import re


def get_list_of_numbers_from_string(string_val):
    return re.findall(r'\b\d+\b', string_val)
