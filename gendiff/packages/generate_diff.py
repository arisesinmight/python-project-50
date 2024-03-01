from gendiff.packages.stylish import built_changes

def generate_diff(file1, file2 ):
    diff = ''
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    all_keys = sorted(set(keys1 + keys2))
    nested_dicts = list(filter(lambda x: type(x) is dict, all_keys))
    for key in all_keys:
        if key in file1 and key in file2 \
                and type(file1[key]) is dict and type(file2[key]) is dict:
            diff += generate_diff(file1[key], file2[key])
        elif key in file1 and type(file1[key]) is dict:
            diff += str(file1[key])
        else:
            diff += built_changes(key, file1, file2)
    return diff
