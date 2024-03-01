from gendiff.packages.parser import parse_data
import yaml
import json


def open_files():
    args = parse_data()
    if args.first_file.endswith('.json'):
        file1 = json.load(open(args.first_file))
    elif args.first_file.endswith('.yaml')\
            or args.first_file.endswith('.yml'):
        file1 = yaml.load(open(args.first_file), Loader=yaml.FullLoader)

    if args.second_file.endswith('.json'):
        file2 = json.load(open(args.second_file))
    elif args.second_file.endswith('.yaml')\
            or args.second_file.endswith('.yml'):
        file2 = yaml.load(open(args.second_file), Loader=yaml.FullLoader)
    return file1, file2
