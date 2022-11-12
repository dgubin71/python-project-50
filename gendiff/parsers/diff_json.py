import json
from gendiff.parsers import diff_reporter

def generate_diff_json(path_file1, path_file2):
    dict_1 = json.load(open(path_file1))
    dict_2 = json.load(open(path_file2))
    return(diff_reporter.diff_report_create(dict_1, dict_2))


