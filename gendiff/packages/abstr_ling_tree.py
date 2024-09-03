def search_for_differences(dict1, dict2):
    diff_dict = {}
    if type(dict1) is dict and type(dict2) is dict:
        keys1 = dict1.keys()
        keys2 = dict2.keys()
    else:
        return diff_dict

    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    nested_dicts1 = set(filter(lambda x: isinstance(dict1[x], dict), keys1))
    nested_dicts2 = set(filter(lambda x: isinstance(dict2[x], dict), keys2))
    nested = nested_dicts1 & nested_dicts2
    plain_stable_keys = (keys1 & keys2) - nested

    for key in added_keys:
        diff_dict[key] = {
            'type': 'added',
            'value': dict2[key]
        }

    for key in removed_keys:
        diff_dict[key] = {
            'type': 'removed',
            'value': dict1[key],
        }

    for key in plain_stable_keys:
        if dict1[key] == dict2[key]:
            diff_dict[key] = {
                'type': 'not_changed',
                'value': dict1[key],
            }
        if dict1[key] != dict2[key]:
            diff_dict[key] = {
                "type": "changed",
                "old_value": dict1[key],
                "new_value": dict2[key]
            }
    for key in nested:
        diff_dict[key] = {
            'type': 'nested',
            'value': search_for_differences(dict1[key], dict2[key])
        }
    return diff_dict
