def format_bools(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def build_indentation(depth, prim_indentation="    "):
    def cut_symbol_used_space(space_string):
        return space_string[0:-2]
    return cut_symbol_used_space(prim_indentation * depth)


def make_removed(key, value, depth):
    return f"{build_indentation(depth)}- {key}: {format_bools(value)}\n"


def make_added(key, value, depth):
    return f'{build_indentation(depth)}+ {key}: {format_bools(value)}\n'


def make_changed_value(key, old_value, new_value, depth):
    return make_removed(key, old_value, depth) + make_added(key, new_value, depth)


def make_not_changed(key, value, depth):
    return f'{build_indentation(depth)}  {key}: {format_bools(value)}\n'


def make_nested(key, depth):
    return f'{build_indentation(depth)}  {key}:'


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
            stringed_diff += make_nested(key, depth) + draw_changes(
                    diff_dict[key]['value'], depth=depth+1
                )

    return '{\n' + stringed_diff + '}'
