from gendiff.packages.generate_diff import generate_diff
from tests.fixtures.result_plain import plain_nested_result
from tests.fixtures.result_stylish import stylish_plain_result, stylish_nested_result
from gendiff.packages.formatters import stylish, plain
import json
import yaml
import pytest


@pytest.mark.parametrize(
    "input_file1,input_file2,expected_result",
    [
        (json.load(open('tests/fixtures/files/file1.json')),
         json.load(open('tests/fixtures/files/file2.json')),
         stylish_plain_result),
        (yaml.load(open('tests/fixtures/files/file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/file2.yaml'), Loader=yaml.FullLoader),
         stylish_plain_result),
        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         stylish_nested_result),
        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         stylish_nested_result),

        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         plain_nested_result),
        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         plain_nested_result)

    ]
)
def test_gendiff(input_file1, input_file2, expected_result):
    assert generate_diff(input_file1, input_file2, formatter=stylish) == expected_result
