import argparse
from gendiff.gendiff  import generate_diff

def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.', \
                                     prog='gendiff', epilog="set format of output")
    parser.add_argument('-f', '--format')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()

    # parser.print_help()

    dict_1 = json.load(open(args.first_file))
    dict_2 = json.load(open(args.second_file))
    generate_diff(path_file1, path_file2)

if __name__ == '__main__':
    main()