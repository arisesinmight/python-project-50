from gendiff.packages.generate_diff import generate_diff
from tests.fixtures.result_plain import result
import json
import yaml
import pytest


@pytest.mark.parametrize(
    "input_file1, input_file2",
    [
        (json.load(open('files/file1.json')), json.load(open('files/file2.json'))),
        (yaml.load(open('files/file1.yaml'), Loader=yaml.FullLoader),
         yaml.load(open('files/file2.yaml'), Loader=yaml.FullLoader))
    ]
)

def test_gendiff(input_file1, input_file2):
    assert generate_diff(input_file1, input_file2) == result
