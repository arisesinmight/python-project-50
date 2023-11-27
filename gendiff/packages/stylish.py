def format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def removed_line(key, value):
    return f"  - {key}: {format(value)}\n"


def added_line(key, value):
    return f"  + {key}: {format(value)}\n"


def changed_line(key, old_value, new_value):
    return f"  - {key}: {format(old_value)}\n\
  + {key}: {format(new_value)}\n"


def not_changed_line(key, value):
    return f"    {key}: {format(value)}\n"
