def format(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    return value


def generate_diff(file1, file2):
    diff = ''
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    all_keys = sorted(set(keys1 + keys2))
    for key in all_keys:
        if key in file1 and key not in file2:
            diff += f"  - {key}: {format(file1[key])}\n"
        elif key in file2 and key not in file1:
            diff += f"  + {key}: {format(file2[key])}\n"
        elif file1[key] != file2[key]:
            diff += f"  - {key}: {format(file1[key])}\n\
  + {key}: {format(file2[key])}\n"
        elif file1[key] == file2[key]:
            diff += f"    {key}: {format(file1[key])}\n"
    return '{\n' + diff + '}'


if __name__ == '__main__':
    generate_diff()
