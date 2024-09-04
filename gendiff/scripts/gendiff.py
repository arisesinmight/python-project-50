#!/usr/bin/env python3
from gendiff.packages.generate_diff import generate_diff
from gendiff.packages.parser import parse_data


def main():
    args = parse_data()
    return print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
