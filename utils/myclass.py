from datetime import datetime


class MyOperation():
    """MyOperation"""

    def __init__(self, id_operation: int, date_operation: str, state_operation: str,
                 operationAmount: dict, description_operation: str, from_operation: str, to_operation: str):
        self.id_operation = id_operation
        temp_date_oper = date_operation.split('T')
        self.date_operation = datetime.strptime(temp_date_oper[0], '%Y-%m-%d')
        self.state_operation = state_operation.upper()
        self.operationAmount = operationAmount['amount'] + ' ' + operationAmount['currency']['name']
        self.description_operation = description_operation
        self.from_operation = from_operation
        self.to_operation = to_operation

    def __repr__(self):
        return f"{self.__doc__}({self.id_operation},'{self.date_operation}','{self.state_operation}'," \
               f"'{self.operationAmount}','{self.description_operation}','{self.from_operation}'," \
               f"'{self.to_operation}')"

    def __str__(self):
        return f"{self.date_operation.strftime('%d.%m.%Y')} {self.description_operation}\n" \
               f"{self.print_from_operation()} -> {self.print_to_operation()}\n" \
               f"{self.operationAmount}\n"

    def print_from_operation(self):
        """
        Правильный вывод имени карты и номера счета
        значение from_operation делится по пробелам
        Если первый элемент прописан Visa, то выводятся первый и второй элемент имени карты, затем выводится счет в виде XXXX XX** *** XXXX
        :return:
        """
        from_temp_text = ''
        if self.from_operation != None:
            from_text = self.from_operation.split()
            if 'visa' in self.from_operation.lower():
                from_temp_text = f'{from_text[0]} {from_text[1]} {from_text[2][:4]} {from_text[2][4:6]}** **** {from_text[2][-4:]}'
            else:
                from_temp_text = f'{from_text[0]} {from_text[1][:4]} {from_text[1][4:6]}** **** {from_text[1][-4:]}'
        return from_temp_text

    def print_to_operation(self):
        """
        Правильный вывод имени карты и номера счета
        значение to_operation делится по пробелам
        Если первый элемент прописан Visa, то выводятся первый и второй элемент имени карты, затем выводится счет в виде **XXXX
        :return:
        """
        to_temp_text = ''
        to_text = self.to_operation.split()
        if 'visa' in self.to_operation.lower():
            to_temp_text = f'{to_text[0]} {to_text[1]} **{to_text[2][-4:]}'
        else:
            to_temp_text = f'{to_text[0]} **{to_text[1][-4:]}'
        return to_temp_text

    def print_one_str(self):
        """
        вывод ы одну строку
        :return:
        """
        return f"{self.date_operation.strftime('%d.%m.%Y')}\t{self.description_operation}\t" \
               f"{self.print_from_operation()} -> {self.print_to_operation()}\t" \
               f"{self.operationAmount}"

# проверяем создание класса
# temp_oper = MyOperation(441945886, "2022-08-26T10:50:58.294041", "EXECUTED",
#                         {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                         "Перевод организации", "VISA class 1596837868705199", "VISA gold 64686473678894779589")
#
# print(temp_oper)
#
# print(temp_oper.__repr__())
#
# print(temp_oper.print_one_str())
