from gendiff.packages import stylish
from gendiff.packages.ast import search_for_differences


def generate_diff(file1, file2, formatter=stylish):
    return formatter.draw_changes(search_for_differences(file1, file2))
