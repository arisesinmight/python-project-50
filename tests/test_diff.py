from gendiff.packages.generate_diff import generate_diff
import json
from tests.fixtures.result_json import result


def test_gendiff():
    file1 = json.load(open('files/file1.json'))
    file2 = json.load(open('files/file2.json'))
    assert generate_diff(file1, file2) == result
