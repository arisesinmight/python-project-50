import json


def draw_changes(diff_dict):
    json_data = json.dumps(diff_dict)
    return json_data
