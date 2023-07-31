import os
import json
import requests


def load_json_url(url_name):
    """
    Загрузка JSON словаря с Интернета
    :param url_name: ссылка на JSON словарь в Интернете
    :return: загруженный JSON словарь или None (если страница не доступна)
    """
    result = requests.get(url_name, verify=False)
    # print(result.status_code)
    if result.status_code != 200:
        print(text_error('Ссылка ' + url_name + ' не существует, проверьте правильность'))
        return None
    return result.json()


def text_error(text=''):
    """
    Формирование сообщения об ошибку с выделением красным цветом
    вызов функции без параметра выдает просто сообщение ОШИБКА
    """
    return '\033[31m' + '>> ОШИБКА - ' + text + ' << ' + '\033[39m'
    # return text

def full_path_name_file(name_file):
    """
    формируем полный путь до файла
    :param name_file: имя файла с указанием подпапки
    :return: полный пусть в UNIX системы
    """
    # return os.getcwd() + '/' + name_file
    return os.path.join(*name_file.replace('\\','/').split('/'))

def load_json_file(name_file):
    """
    Загрузка JSON словаря с файла
    name_file:  имя файла c JSON словарем
    :return: список JSON
    """
    json_list = None  # словарь
    # формируем полный путь до файла
    name_file = full_path_name_file(name_file)
    # print(name_file)

    try:
        if os.path.exists(name_file):
            with open(name_file, 'r', encoding='UTF-8') as file:
                json_list = json.load(file)
        else:                                       # если файла нет, то ошибка
            print(text_error('Файл ' + name_file + ' не существует, проверьте наличие файла по указанному пути'))
    except json.JSONDecodeError:                    # если ошибка чтения JSON словаря, то выводим ошибку
        print(text_error('Файл ' + name_file + ' не является JSON файлом'))

    return json_list


def check_line_entry(text='', allowed_сhars='', error_string=''):
    """
    Функция проверяет введенную пользователем строку на пустой ввод и разрешенные символы
    :param text: строка для пользователя
    :param allowed_сhars: разрешенные символы, если список пустой, то разрешены любые символы
    :param error_string: строка с ошибкой, если строка содержит запрещенные символы
    :return: возвращаем введенную строку от пользователя
    """
    allowed_сhars = allowed_сhars.strip()
    while True:
        input_string = input(f'{text}: ').strip().lower()
        if input_string == '':
            print(text_error('Пустой ввод'))
        elif allowed_сhars == '':
            break
        else:
            is_chars_allowed = True
            for i_s in input_string:
                if i_s not in allowed_сhars:
                    is_chars_allowed = False
                    break
            if is_chars_allowed:
                break
            else:
                print(text_error(error_string))

    return input_string
