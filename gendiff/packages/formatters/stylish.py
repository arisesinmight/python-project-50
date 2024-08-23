from gendiff.packages.formatters.common_functions import format_bools


def build_indentation(place, depth, prim_indentation="    "):
    if place == "start":
        return (prim_indentation * depth)[0:-2]
    if place == "end":
        return prim_indentation * (depth - 1)


def draw_nested_value(value, depth):
    entry = ""
    keys = value.keys()

    for key in keys:
        if not isinstance(key, dict):
            entry += f'{make_not_changed(key, value[key], depth)}'
        else:
            entry += f'\n{build_indentation("end", depth)}'\
                + draw_nested_value(value[key], depth=depth + 1)
    return "{" + entry + f'\n{build_indentation("end", depth)}' + "}"


def make_removed(key, value, depth):
    if type(value) is not dict:
        string_entry = format_bools(value)
    else:
        string_entry = draw_nested_value(value, depth=depth + 1)
    return f'\n{build_indentation("start", depth)}- {key}: {string_entry}'


def make_added(key, value, depth):
    if type(value) is not dict:
        string_entry = format_bools(value)
    else:
        string_entry = draw_nested_value(value, depth=depth + 1)
    return f'\n{build_indentation("start", depth)}+ {key}: {string_entry}'


def make_not_changed(key, value, depth):
    if type(value) is not dict:
        string_entry = format_bools(value)
    else:
        string_entry = draw_nested_value(value, depth=depth + 1)
    return f'\n{build_indentation("start", depth)}  {key}: {string_entry}'


def make_changed_value(key, old_value, new_value, depth):
    return make_removed(key, old_value, depth)\
        + make_added(key, new_value, depth)


def make_nested_key(key, depth):
    return f'\n{build_indentation("start", depth)}  {key}: '


def draw_changes(diff_dict, depth=1):
    stringed_diff = ""
    keys = sorted(diff_dict.keys())

    for key in keys:
        if diff_dict[key]["type"] == "not_changed":
            stringed_diff += make_not_changed(
                key, diff_dict[key]["value"], depth
            )

        if diff_dict[key]["type"] == "added":
            stringed_diff += make_added(
                key,
                diff_dict[key]["value"],
                depth
            )

        if diff_dict[key]["type"] == "removed":
            stringed_diff += make_removed(
                key,
                diff_dict[key]["value"],
                depth
            )

        if diff_dict[key]["type"] == "changed":
            stringed_diff += make_changed_value(
                key,
                diff_dict[key]["old_value"],
                diff_dict[key]["new_value"],
                depth
            )

        if diff_dict[key]["type"] == "nested":
            stringed_diff += make_nested_key(key, depth)\
                + draw_changes(diff_dict[key]["value"], depth=depth + 1)

    return "{" + stringed_diff + "\n" + build_indentation("end", depth) + "}"
