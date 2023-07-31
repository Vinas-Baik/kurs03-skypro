from datetime import datetime


class MyOperation():

    def __init__(self, id_operation: int, date_operation: str, state_operation: str,
                 operationAmount: dict, description_operation: str, from_operation: str, to_operation: str):
        self.id_operation = id_operation
        self.date_operation = datetime.strptime(date_operation, '%Y-%m-%dT%H:%M:%S.%f')
        self.state_operation = state_operation.upper()
        self.operationAmount = operationAmount
        self.description_operation = description_operation
        self.from_operation = from_operation
        self.to_operation = to_operation

    def __repr__(self):
        return f"MyOperation({self.id_operation}, '{self.date_operation}', '{self.state_operation}',\n" \
               f"'{self.operationAmount}',\n'{self.description_operation}', '{self.from_operation}', " \
               f"'{self.to_operation}')"

    def __str__(self):
        from_text = self.from_operation.split()
        to_text = self.to_operation.split()

        return f"{self.date_operation.strftime('%d.%m.%Y')} {self.description_operation}\n" \
               f"{from_text[0]} {from_text[1][:4]} {from_text[1][4:6]}** **** {from_text[1][-4:]} -> " \
               f"{to_text[0]} **{to_text[1][-4:]}\n" \
               f"{self.operationAmount['amount']} {self.operationAmount['currency']['name']}\n"


# проверяем создание класса
# temp_oper = MyOperation(441945886, "2022-08-26T10:50:58.294041", "EXECUTED",
#                         {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
#                         "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589")
#
# print(temp_oper)
#
# print(temp_oper.__repr__())

