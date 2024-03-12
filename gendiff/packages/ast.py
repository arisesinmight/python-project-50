def search_for_differences(dict1, dict2, depth=1):
    diff_dict = {}

    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2

    nested_dicts1 = set(filter(lambda x: type(x) is dict, keys1))
    nested_dicts2 = set(filter(lambda x: type(x) is dict, keys2))
    children = nested_dicts1 & nested_dicts2

    plain_stable_keys = (keys1 & keys2) - children

    for key in added_keys:
        diff_dict[key] = {
            'type': 'added',
            'value': dict2[key],
            'depth': depth
        }

    for key in removed_keys:
        diff_dict[key] = {
            'type': 'removed',
            'value': dict1[key],
            'depth': depth
        }

    for key in plain_stable_keys:
        if dict1[key] == dict2[key]:
            diff_dict[key] = {
                'type': 'not_changed',
                'value': dict1[key],
                'depth': depth
            }
        if dict1[key] != dict2[key]:
            diff_dict[key] = {
                'type': 'changed',
                'old_value': dict1[key],
                'new_value': dict2[key],
                'depth': depth
            }

    for key in children:
        diff_dict[key] = {
            'type': 'children',
            'value': search_for_differences(
                dict1[key], dict2[key], depth=depth + 1
            ),
            'depth': depth}

    return diff_dict
