#!/usr/bin/env python3
import argparse
from gendiff.packages.gendiff import generate_diff
import json


def main():
    parser = argparse.ArgumentParser(description='Compares\
    two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')
    args = parser.parse_args()
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    return print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
