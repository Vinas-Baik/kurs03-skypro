import utils.utils as my_utils
import utils.myclass as my_class

FILE_JSON = 'data\operations.json'

operation_list = []

def main():

    # Делаем красиво и просим имя пользователя
    print('\n{0:^60}\n'.format('-=== \033[32m ДОБРЫЙ ДЕНЬ \033[39m ===-'))

    user_player = my_utils.check_line_entry('Введи свое имя')

    print(f'Привет \033[32m{user_player.title()}\033[39m')

    json_list = my_utils.load_json_file(FILE_JSON)

    for t_json in json_list:
        # print(t_json)
        if t_json == {}:
            continue
        if 'from' in t_json:
            operation_list.append(my_class.MyOperation(t_json['id'], t_json['date'], t_json['state'],
                                                       t_json['operationAmount'], t_json['description'],
                                                       t_json['from'], t_json['to']))
        else:
            operation_list.append(my_class.MyOperation( t_json['id'], t_json['date'], t_json['state'],
                                                        t_json['operationAmount'], t_json['description'],
                                                        None, t_json['to']))

    # for t_oper in operation_list:
    #     print(t_oper)

    count_EXECUTED = 0

    operation_list.sort(key='date')

    # for temp_oper in operation_list:



main()

