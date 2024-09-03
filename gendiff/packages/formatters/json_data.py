import json


def draw_changes(diff_dict):
    return json.dumps(diff_dict, indent=2, sort_keys=True)
