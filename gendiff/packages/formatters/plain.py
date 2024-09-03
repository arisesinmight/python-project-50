def format_value(value):
    if type(value) is dict:
        return '[complex value]'
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    elif value == 0:
        return "0"
    return f"'{value}'"


def set_string(path, changes, value=0, old_value=0, new_value=0):

    if changes == "removed":
        changed = "removed"

    elif changes == "added":
        changed = f'added with value: {format_value(value)}'

    elif changes == "changed":
        changed = f'updated. From \
{format_value(old_value)} to \
{format_value(new_value)}'

    else:
        return ''
    return f'Property {path} was {changed}\n'


def draw_changes(diff_dict, path=[]):
    stringed_diff = ""
    keys = sorted(diff_dict.keys())

    for key in keys:
        path.append(key)
        stringed_path = f"'{'.'.join(path)}'"

        if diff_dict[key]["type"] == "changed":
            stringed_diff += set_string(
                stringed_path,
                diff_dict[key]["type"],
                old_value=diff_dict[key]["old_value"],
                new_value=diff_dict[key]["new_value"]
            )
            path.remove(key)

        elif diff_dict[key]["type"] != "nested":
            stringed_diff += set_string(
                stringed_path,
                diff_dict[key]["type"],
                value=diff_dict[key]["value"],
            )
            path.remove(key)

        elif diff_dict[key]["type"] == "nested":
            stringed_diff += draw_changes(diff_dict[key]["value"], path=path)
            path.remove(key)

    return stringed_diff
