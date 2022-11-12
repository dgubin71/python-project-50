from gendiff.gendiff import generate_diff


def test_generate_json_diff():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file2.json'
    diff = open('./tests/fixtures/output_diff')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_json_no_diff():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file1.json'
    diff = open('./tests/fixtures/output_diff2')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_yaml_diff():
    path_file1 = './tests/fixtures/file1.yaml'
    path_file2 = './tests/fixtures/file2.yaml'
    diff = open('./tests/fixtures/output_diff_yaml')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_yaml_no_diff():
    path_file1 = './tests/fixtures/file1.yaml'
    path_file2 = './tests/fixtures/file1.yaml'
    diff = open('./tests/fixtures/output_diff2_yaml')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_yml_diff():
    path_file1 = './tests/fixtures/file1.yml'
    path_file2 = './tests/fixtures/file2.yml'
    diff = open('./tests/fixtures/output_diff_yml')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_yml_no_diff():
    path_file1 = './tests/fixtures/file1.yml'
    path_file2 = './tests/fixtures/file1.yml'
    diff = open('./tests/fixtures/output_diff2_yml')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result
    