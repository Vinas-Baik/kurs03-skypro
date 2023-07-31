import sys

import pytest

import utils.utils as my_utils



def test_load_json_file():
    assert my_utils.load_json_file('data.json') == None
    assert my_utils.load_json_file('test.json') == [{'id': 667307132}]
    assert my_utils.load_json_file('test-err.json') == None


def test_check_line_entry():
    # пока не смог найти возможность реализации проверки pytest вводимых с клавиатуры данных

    # assert my_utils.check_line_entry('Введите А или Б', 'aб') in 'aб'
    pass

def test_text_error():
    assert my_utils.text_error() == '\033[31m>> ОШИБКА -  << \033[39m'
    assert my_utils.text_error('НЕТ ТАКОГО ФАЙЛА') == '\033[31m>> ОШИБКА - НЕТ ТАКОГО ФАЙЛА << \033[39m'


def test_full_path_name_file():
    temp_st = my_utils.full_path_name_file('data.json')
    assert my_utils.full_path_name_file('data.json') == temp_st
    temp_st = my_utils.full_path_name_file('test-err.json')
    assert my_utils.full_path_name_file('test-err.json') == temp_st

