import argparse



def parse_data():
    parser = argparse.ArgumentParser(description='Compares \
two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format')
    return parser.parse_args()




    return file1, file2
