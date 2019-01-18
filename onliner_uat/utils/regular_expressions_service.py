import re


def get_number_from_string(string_val):
    return re.findall(r'\b\d+\b', string_val)
