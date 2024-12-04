from gendiff.packages.generate_diff import generate_diff
import pytest

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

@pytest.mark.parametrize(
    "input_file1, input_file2, expected_result, formatter",
    [
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         read('tests/fixtures/result_stylish_plain.txt'),
         'stylish'),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         read('tests/fixtures/result_stylish_plain.txt'),
         'stylish'),

        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         read('tests/fixtures/result_stylish_nested.txt'),
         'stylish'),
        ('tests/fixtures/files/hex_file1.json',
         'tests/fixtures/files/hex_file2.json',
         read('tests/fixtures/hex_result_stylish.txt'),
         'stylish'),

        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         read('tests/fixtures/result_stylish_nested.txt'),
         'stylish'),
        ('tests/fixtures/files/hex_file1.yml',
         'tests/fixtures/files/hex_file2.yml',
         read('tests/fixtures/hex_result_stylish.txt'),
         'stylish'),

        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         read('tests/fixtures/result_plain.txt'),
         'plain'),
        ('tests/fixtures/files/hex_file1.json',
         'tests/fixtures/files/hex_file2.json',
         read('tests/fixtures/hex_result_plain.txt'),
         'plain'),

        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         read('tests/fixtures/result_plain.txt'),
         'plain'),
        ('tests/fixtures/files/hex_file1.yml',
         'tests/fixtures/files/hex_file2.yml',
         read('tests/fixtures/hex_result_plain.txt'),
         'plain'),


        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         read('tests/fixtures/result_json.txt'),
         'json'),
        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         read('tests/fixtures/result_json.txt'),
         'json')

    ]
)
def test_gendiff(input_file1, input_file2, expected_result, formatter):
    assert generate_diff(input_file1, input_file2, formatter) == expected_result
