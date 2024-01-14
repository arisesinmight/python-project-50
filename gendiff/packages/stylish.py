def format_bools(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def removed_key(key, value):
    return f"  - {key}: {format_bools(value)}\n"


def added_key(key, value):
    return f"  + {key}: {format_bools(value)}\n"


def changed_value(key, old_value, new_value):
    return f"  - {key}: {format_bools(old_value)}\n\
  + {key}: {format(new_value)}\n"


def no_changes(key, value):
    return f"    {key}: {format_bools(value)}\n"


def built_changes(key, file1, file2):
    if key in file1 and key not in file2:
        return removed_key(key, file1[key])
    elif key in file2 and key not in file1:
        return added_key(key, file2[key])
    elif file1[key] != file2[key]:
        return changed_value(key, file1[key], file2[key])
    elif file1[key] == file2[key]:
        return no_changes(key, file1[key])
