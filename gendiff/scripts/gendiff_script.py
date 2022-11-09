import argparse
from gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.", prog="gendiff", epilog="set format of output")
    parser.add_argument('-f', '--format')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    # parser.print_help()
    path_file1 = args.first_file
    path_file2 = args.second_file
    print(generate_diff(path_file1, path_file2))


if __name__ == '__main__':
    main()
