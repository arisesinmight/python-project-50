from gendiff.packages.abstr_ling_tree import search_for_differences


def generate_diff(file1, file2, formatter):
    return formatter.draw_changes(search_for_differences(file1, file2)).strip()
