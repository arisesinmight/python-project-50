from gendiff.packages.generate_diff import generate_diff
from tests.fixtures.result_plain import plain_nested_result
from tests.fixtures.result_stylish import stylish_plain_result, stylish_nested_result
from tests.fixtures.result_json import json_nested_result
from tests.fixtures.hex_result_plain import hex_plain_result
from tests.fixtures.hex_result_stylish import hex_stylish_result
import pytest


@pytest.mark.parametrize(
    "input_file1, input_file2, expected_result, formatter",
    [
        ('tests/fixtures/files/file1.json',
         'tests/fixtures/files/file2.json',
         stylish_plain_result,
         'stylish'),
        ('tests/fixtures/files/file1.yaml',
         'tests/fixtures/files/file2.yaml',
         stylish_plain_result,
         'stylish'),

        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         stylish_nested_result,
         'stylish'),
        ('tests/fixtures/files/hex_file1.json',
         'tests/fixtures/files/hex_file2.json',
         hex_stylish_result,
         'stylish'),

        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         stylish_nested_result,
         'stylish'),
        ('tests/fixtures/files/hex_file1.yml',
         'tests/fixtures/files/hex_file2.yml',
         hex_stylish_result,
         'stylish'),

        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         plain_nested_result,
         'plain'),
        ('tests/fixtures/files/hex_file1.json',
         'tests/fixtures/files/hex_file2.json',
         hex_plain_result,
         'plain'),

        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         plain_nested_result,
         'plain'),
        ('tests/fixtures/files/hex_file1.yml',
         'tests/fixtures/files/hex_file2.yml',
         hex_plain_result,
         'plain'),


        ('tests/fixtures/files/nested_file1.json',
         'tests/fixtures/files/nested_file2.json',
         json_nested_result,
         'json'),
        ('tests/fixtures/files/nested_file1.yaml',
         'tests/fixtures/files/nested_file2.yaml',
         json_nested_result,
         'json')

    ]
)
def test_gendiff(input_file1, input_file2, expected_result, formatter):
    assert generate_diff(input_file1, input_file2, formatter) == expected_result
