def format_bools(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def removed_key(key, value, type, depth):
    indentation =
    return f"  - {key}: {format_bools(value)}\n"


def added_key(key, value):
    return f"  + {key}: {format_bools(value)}\n"


def changed_value(key, old_value, new_value, depth):
    indentation = "  " * depth
    return f"{indentation} -{key}: {format_bools(old_value)}\n\
{indentation}{type}{key}: {format(new_value)}\n"


def no_changes(key, value):
    return f"    {key}: {format_bools(value)}\n"


def draw_changes(dict_entry): # key, 'value'=ast[key], type, depth

    if dict_entry['type'] = "added":


