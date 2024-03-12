def format_bools(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def removed(key, value, depth):
    indentation = "  " * depth
    return f"{indentation}- {key}: {format_bools(value)}\n"


def added(key, value, depth):
    indentation = "  " * depth
    return f'{indentation}+ {key}: {format_bools(value)}\n'


def changed_value(key, old_value, new_value, depth):
    return removed(key, old_value, depth) + added(key, new_value, depth)


def not_changed(key, value, depth):
    indentation = "  " * depth
    return f'{indentation}  {key}: {format_bools(value)}\n'


def draw_changes(diff_dict):
    stringed_diff = ''
    keys = sorted(diff_dict.keys())

    for key in keys:
        if diff_dict[key]['type'] == 'not_changed':
            stringed_diff += not_changed(
                key, diff_dict[key]['value'], diff_dict[key]['depth']
            )

        if diff_dict[key]['type'] == 'added':
            stringed_diff += added(
                key,
                diff_dict[key]['value'],
                diff_dict[key]['depth']
            )

        if diff_dict[key]['type'] == 'removed':
            stringed_diff += removed(
                key,
                diff_dict[key]['value'],
                diff_dict[key]['depth']
            )

        if diff_dict[key]['type'] == 'changed':
            stringed_diff += changed_value(
                key,
                diff_dict[key]['old_value'],
                diff_dict[key]['new_value'],
                diff_dict[key]['depth']
            )

        if diff_dict[key]['type'] == 'children':
            stringed_diff += draw_changes(diff_dict[key])

    return '{\n' + stringed_diff + '}'
