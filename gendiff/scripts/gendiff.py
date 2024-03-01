#!/usr/bin/env python3
from gendiff.packages.open_parsed_files import open_files
from gendiff.packages.generate_diff import generate_diff


def main():
    file1, file2 = open_files()
    return print(generate_diff(file1, file2))


if __name__ == '__main__':
    main()
