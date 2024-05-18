def format_bools(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def make_removed(key, value, depth):
    indentation = "  " * depth
    return f"{indentation}- {key}: {format_bools(value)}\n"


def make_added(key, value, depth):
    indentation = "  " * depth
    return f'{indentation}+ {key}: {format_bools(value)}\n'


def make_changed_value(key, old_value, new_value, depth):
    return make_removed(key, old_value, depth) + make_added(key, new_value, depth)


def make_not_changed(key, value, depth):
    indentation = "  " * depth
    return f'{indentation}  {key}: {format_bools(value)}\n'


def make_nested(key, depth):
    indentation = "  " * depth
    return f'{indentation}  {key}:'


def make_children(key, depth):
    indentation = "  " * depth
    return f'{indentation}  {key}: {draw_changes(key, depth)}\n'


def draw_changes(diff_dict, depth=1):
    stringed_diff = ''
    keys = sorted(diff_dict.keys())

    for key in keys:
        if diff_dict[key]['type'] == 'not_changed':
            stringed_diff += make_not_changed(
                key, diff_dict[key]['value'], depth
            )

        if diff_dict[key]['type'] == 'added':
            stringed_diff += make_added(
                key,
                diff_dict[key]['value'],
                depth
            )

        if diff_dict[key]['type'] == 'removed':
            stringed_diff += make_removed(
                key,
                diff_dict[key]['value'],
                depth
            )

        if diff_dict[key]['type'] == 'changed':
            stringed_diff += make_changed_value(
                key,
                diff_dict[key]['old_value'],
                diff_dict[key]['new_value'],
                depth
            )

        if diff_dict[key]['type'] == 'nested':
            stringed_diff += make_nested(
                make_children(
                    diff_dict[key]['value'], depth=depth+1
                ), depth
            )

    return '{\n' + stringed_diff + '}'
