import pytest

import utils.utils as my_utils

def test_load_json_file():
    assert my_utils.load_json_file('data.json') == None
    assert my_utils.load_json_file('tests\test.json') == []
