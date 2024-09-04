from gendiff.packages.abstr_ling_tree import search_for_differences
from gendiff.packages.formatters import stylish
from gendiff.packages.set_parsed_arguments import set_arguments


def generate_diff(file1, file2, formatter=stylish):
    file1, file2, formatter = set_arguments(file1, file2, formatter)
    return formatter.draw_changes(search_for_differences(file1, file2)).strip()
