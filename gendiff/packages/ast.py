def search_for_differences(dict1, dict2, depth=1):
    difference = {}
    if type(dict1) is not dict or type(dict2) is not dict:
        return difference

    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    stable_keys = keys1 & keys2
    nested_dicts1 = set(filter(lambda x: type(x) is not dict, keys1))
    nested_dicts2 = set(filter(lambda x: type(x) is not dict, keys2))
    children = nested_dicts1 & nested_dicts2

    for key in added_keys:
        difference[key] = {"type": "added", "value": dict2[key], 'depth': depth}

    for key in removed_keys:
        difference[key] = {"type": "removed", "value": dict1[key], 'depth': depth}

    for key in stable_keys:
        if dict1[key] == dict2[key]:
            difference[key] = {"type": "not_changed", "value": dict1[key], 'depth': depth}
        if dict1[key] != dict2[key]:
            difference[key] = \
                {"type": "changed", "past_value": dict1[key], "new_value": dict2[key], 'depth': depth}

    for key in children:
        difference[key] = search_for_differences(dict1[key], dict2[key], depth=depth + 1)

    return difference