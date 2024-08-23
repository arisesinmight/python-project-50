from gendiff.packages.formatters.common_functions import format_bools


def set_string(path, changes, *values):
    if changes == "not_changed":
        return

    if changes == "removed":
        changed = "removed"

    if changes == "added":
        changed = f'added with value: {format_bools(values)}'

    if changes == "changed":
        changed = f'updated. From {format_bools(values[0])} to {format_bools(values[1])}'

    return f'Property {path} was {changed}\n'


def draw_changes(diff_dict, key_path=''):
    stringed_diff = ""
    keys = sorted(diff_dict.keys())

    for key in keys:
        key_path += str(key)
        if not isinstance(key, dict):
            stringed_diff += set_string(
                key_path,
                diff_dict[key]["type"],
                diff_dict[key]["value"],
                diff_dict[key]["old_value"],
                diff_dict[key]["new_value"]
            )
        else:
            stringed_diff += draw_changes(diff_dict[key], key_path=key_path + f'.{key}')
    return stringed_diff

