from gendiff.parsers import diff_json
from gendiff.parsers import diff_yaml
def generate_diff(path_file1, path_file2):

    if  (path_file1.find('.json',-5) != -1) and  (path_file2.find('.json',-5)  != -1):
        return (diff_json.generate_diff_json(path_file1, path_file2))
    if  path_file1.find('.yaml',-5) != -1 and  path_file2.find('.yaml',-5)  != -1:
        return(diff_yaml.generate_diff_yaml(path_file1, path_file2))
    if  path_file1.find('.yml',-4) != -1 and  path_file2.find('.yml',-4)  != -1:
         return (diff_yaml.generate_diff_yaml(path_file1, path_file2))
