from gendiff.packages.generate_diff import generate_diff
from tests.fixtures.result_plain import plain_nested_result
from tests.fixtures.result_stylish import stylish_plain_result, stylish_nested_result
from tests.fixtures.result_json import json_nested_result
from tests.fixtures.hex_result_plain import hex_plain_result
from tests.fixtures.hex_result_stylish import hex_stylish_result
from gendiff.packages.formatters import stylish, plain, json_data
import json
import yaml
import pytest


@pytest.mark.parametrize(
    "input_file1, input_file2, expected_result, formatter",
    [
        (json.load(open('tests/fixtures/files/file1.json')),
         json.load(open('tests/fixtures/files/file2.json')),
         stylish_plain_result,
         stylish),
        (yaml.load(open('tests/fixtures/files/file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/file2.yaml'), Loader=yaml.FullLoader),
         stylish_plain_result,
         stylish),

        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         stylish_nested_result,
         stylish),
        (json.load(open('tests/fixtures/files/hex_file1.json')),
         json.load(open('tests/fixtures/files/hex_file2.json')),
         hex_stylish_result,
         stylish),

        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         stylish_nested_result,
         stylish),
        (yaml.load(open('tests/fixtures/files/hex_file1.yml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/hex_file2.yml'), Loader=yaml.FullLoader),
         hex_stylish_result,
         stylish),

        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         plain_nested_result,
         plain),
        (json.load(open('tests/fixtures/files/hex_file1.json')),
         json.load(open('tests/fixtures/files/hex_file2.json')),
         hex_plain_result,
         plain),

        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         plain_nested_result,
         plain),
        (yaml.load(open('tests/fixtures/files/hex_file1.yml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/hex_file2.yml'), Loader=yaml.FullLoader),
         hex_plain_result,
         plain),


        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         json_nested_result,
         json_data),
        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         json_nested_result,
         json_data)

    ]
)
def test_gendiff(input_file1, input_file2, expected_result, formatter):
    assert generate_diff(input_file1, input_file2, formatter) == expected_result
