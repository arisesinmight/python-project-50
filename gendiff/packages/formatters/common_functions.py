def format_bools(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    return value
