import pytest

import utils.myclass as myclass


def test_myclass():
    # тестирование проверки вывода __str__
    assert myclass.MyOperation(441945886, "2022-08-26T10:50:58.294041", "EXECUTED",
                               {"amount": "31957.58", "currency": {"name": "руб.","code": "RUB"}},
                               "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589").__str__() == \
           "26.08.2022 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.\n"

    assert myclass.MyOperation(667307132, "2022-07-13T18:51:29.313309", "EXECUTED",
                               {"amount": "97853.86", "currency": {"name": "руб.","code": "RUB"}},
                               "Перевод с карты на счет", "Maestro 1308795367077170", "Счет 96527012349577388612").__str__() == \
           "13.07.2022 Перевод с карты на счет\nMaestro 1308 79** **** 7170 -> Счет **8612\n97853.86 руб.\n"

    assert myclass.MyOperation(667307132, "2022-07-13T18:51:29.313309", "EXECUTED",
                               {"amount": "97853.86", "currency": {"name": "руб.","code": "RUB"}},
                               "Перевод с карты на счет", None, "Счет 96527012349577388612").__str__() == \
           "13.07.2022 Перевод с карты на счет\n-> Счет **8612\n97853.86 руб.\n"

    # тестирование проверки вывода __repr__

    test_my_oper = myclass.MyOperation(667307132, "2022-07-13T18:51:29.313309", "EXECUTED",
                                       {"amount": "97853.86", "currency": {"name": "руб.","code": "RUB"}},
                                       "Перевод с карты на счет", "Maestro 1308795367077170", "Счет 96527012349577388612")
    result_test_repr = repr(test_my_oper)

    assert test_my_oper.__repr__() == result_test_repr

