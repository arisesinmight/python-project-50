import json

import yaml
from gendiff.packages.formatters import json_data, plain, stylish


def set_arguments(first_file, second_file, formatter):
    if first_file.endswith('.json'):
        file1 = json.load(open(first_file))
    elif first_file.endswith('.yaml')\
            or first_file.endswith('.yml'):
        file1 = yaml.load(open(first_file), Loader=yaml.FullLoader)

    if second_file.endswith('.json'):
        file2 = json.load(open(second_file))
    elif second_file.endswith('.yaml')\
            or second_file.endswith('.yml'):
        file2 = yaml.load(open(second_file), Loader=yaml.FullLoader)

    if formatter == 'plain':
        _formatter = plain
    elif formatter == 'json':
        _formatter = json_data
    else:
        _formatter = stylish

    return file1, file2, _formatter
