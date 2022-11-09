from gendiff import generate_diff


def test_generate_diff():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file2.json'
    diff = open('./tests/fixtures/output_diff')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result


def test_generate_diff_no_diff():
    path_file1 = './tests/fixtures/file1.json'
    path_file2 = './tests/fixtures/file1.json'
    diff = open('./tests/fixtures/output_diff2')
    result = diff.read()
    assert generate_diff(path_file1, path_file2) == result

