import re


def find_dates_in_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return re.findall(r'\b(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(\d{4})\b',
                          file.read())
