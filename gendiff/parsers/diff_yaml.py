import yaml
from gendiff.parsers import diff_reporter


def generate_diff_yaml(path_file1, path_file2):
    dict_1 = yaml.safe_load(open(path_file1))
    dict_2 = yaml.safe_load(open(path_file2))
    return (diff_reporter.diff_report_create(dict_1, dict_2))