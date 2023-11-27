from gendiff.packages import stylish


def generate_diff(file1, file2):
    diff = ''
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    all_keys = sorted(set(keys1 + keys2))
    for key in all_keys:
        if key in file1 and key not in file2:
            diff += stylish.removed_line(key, file1[key])
        elif key in file2 and key not in file1:
            diff += stylish.added_line(key, file2[key])
        elif file1[key] != file2[key]:
            diff += stylish.changed_line(key, file1[key], file2[key])
        elif file1[key] == file2[key]:
            diff += stylish.not_changed_line(key, file1[key])
    return '{\n' + diff + '}'
