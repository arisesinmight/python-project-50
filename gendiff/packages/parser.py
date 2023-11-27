import argparse
import yaml
import json


def parse_data():
    parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')
    args = parser.parse_args()
    if str(args.first_file)[-5:] == ".json":
        file1 = json.load(open(args.first_file))
        file2 = json.load(open(args.second_file))
    elif str(args.first_file)[-5:] == ".yaml"\
            or str(args.first_file)[-4:] == ".yml":
        file1 = yaml.load(open(args.first_file), Loader=yaml.FullLoader)
        file2 = yaml.load(open(args.second_file), Loader=yaml.FullLoader)
    return file1, file2
