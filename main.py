import utils.utils as my_utils
import utils.myclass as my_class

FILE_JSON = 'data\operations.json'

operation_list = []

def main():
    #
    #   НАЧАЛО ПРОГРАММЫ
    #

    # Делаем красиво и просим имя пользователя
    print('\n{0:^60}\n'.format('-=== \033[32m ДОБРЫЙ ДЕНЬ \033[39m ===-'))

    user_player = input('Введи свое имя: ').strip()

    print(f'Привет \033[32m{user_player.title()}\033[39m')

    json_list = my_utils.load_json_file(FILE_JSON)
    date_list = {}

    for t_json in json_list:
        # print(t_json)
        if t_json == {}:
            continue
        date_list[t_json['date']] = t_json['id']
        if 'from' in t_json:
            operation_list.append(my_class.MyOperation(t_json['id'], t_json['date'], t_json['state'],
                                                       t_json['operationAmount'], t_json['description'],
                                                       t_json['from'], t_json['to']))
        else:
            operation_list.append(my_class.MyOperation( t_json['id'], t_json['date'], t_json['state'],
                                                        t_json['operationAmount'], t_json['description'],
                                                        None, t_json['to']))

    # for t_oper in operation_list:
    #     print(t_oper.print_one_str())

    # print("до сортировки")
    # for t_key, t_value in date_list.items():
    #     print(f'{t_key}: {t_value}')

    sorted_date_list = dict(sorted(date_list.items(), reverse=True))

    # print("после сортировки")
    #
    # for t_key, t_value in sorted_date_list.items():
    #     print(f'{t_key}: {t_value}')

    count_executed = 0

    for t_key, t_value in sorted_date_list.items():

        for t_oper in operation_list:
            if (t_value == t_oper.id_operation) and (t_oper.state_operation.upper() == 'EXECUTED'):
                # print(t_oper.print_one_str())   # вывод в одну строку
                print(t_oper)
                count_executed += 1
                break

        if count_executed == 5:
            break

    #
    #   КОНЕЦ ПРОГРАММЫ
    #


main()

