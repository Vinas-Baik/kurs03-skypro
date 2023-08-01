import os
import json

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
    return os.getcwd() + '\\' + name_file
    # return os.path.join(*name_file.replace('\\','/').split('/'))

def load_json_file(name_file):
    """
    Загрузка JSON словаря с файла
    name_file:  имя файла c JSON словарем
    :return: список JSON
    """
    json_list = None  # словарь
    # формируем полный путь до файла
    name_file1 = full_path_name_file(name_file)

    # name_file1 = 'C:\\Users\\user\\Мой диск (svn1409@gmail.com)\\Обучение\\skypro\\Проекты\\kurs03-skypro\\utils\\test.json'

    try:
        if os.path.exists(name_file1):
            with open(name_file, 'r', encoding='UTF-8') as file:
                json_list = json.load(file)
        else:                                       # если файла нет, то ошибка
            # print(text_error('Файл ' + name_file + ' не существует, проверьте наличие файла по указанному пути'))
            json_list = None

    except json.JSONDecodeError:                    # если ошибка чтения JSON словаря, то выводим ошибку
        # print(text_error('Файл ' + name_file + ' не является JSON файлом'))
        json_list = None

    return json_list
