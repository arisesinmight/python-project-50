#!/usr/bin/env python3
from gendiff.packages.set_parsed_arguments import set_arguments
from gendiff.packages.generate_diff import generate_diff


def main():
    file1, file2, formatter = set_arguments()
    return print(generate_diff(file1, file2, formatter))


if __name__ == '__main__':
    main()
