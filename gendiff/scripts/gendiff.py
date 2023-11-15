#!/usr/bin/env python3
from gendiff.packages.parser import args
from gendiff.packages.generate_diff import generate_diff
import json


def main():
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    return print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
