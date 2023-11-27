from gendiff.packages.generate_diff import generate_diff
from tests.fixtures.result_plain import plain_result
from tests.fixtures.result_nested import nested_dict_result
import json
import yaml
import pytest


@pytest.mark.parametrize(
    "input_file1,input_file2,expected_result",
    [
        (json.load(open('tests/fixtures/files/file1.json')),
         json.load(open('tests/fixtures/files/file2.json')),
         plain_result),
        (yaml.load(open('tests/fixtures/files/file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/file2.yaml'), Loader=yaml.FullLoader),
         plain_result),
        (json.load(open('tests/fixtures/files/nested_file1.json')),
         json.load(open('tests/fixtures/files/nested_file2.json')),
         nested_dict_result),
        (yaml.load(open('tests/fixtures/files/nested_file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('tests/fixtures/files/nested_file2.yaml'), Loader=yaml.FullLoader),
         nested_dict_result)
    ]
)
def test_gendiff(input_file1, input_file2, expected_result):
    assert generate_diff(input_file1, input_file2) == expected_result
