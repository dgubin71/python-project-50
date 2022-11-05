import argparse


def main():
    parser = argparse.ArgumentParser(description = 'Compares two configuration files and shows a difference.',\
                                     prog = 'gendiff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.print_help()

if __name__ == '__main__':
    main()