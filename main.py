
import os
import shutil
from datetime import datetime

file_name = "input.txt"
folder_name = "output"


"""
    Проверяет, существует ли файл в текущей директории и создает папку вывода, если она не существует.

    Args:
        file_name (str): Имя входного файла.
        folder_name (str): Имя папки вывода.

    Returns:
        None

    Raises:
        FileNotFoundError: Если файл не существует.
        NotADirectoryError: Если папка вывода существует, но не является директорией.
"""
def check_file_exists(file_name, folder_name):

    if os.path.exists(file_name):
        print(f"Файл {file_name} существует в текущей директории.")
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Папка {folder_name} была успешно создана.")
        else:
            print(f"Папка {folder_name} уже существует в текущей директории.")
        scan_files_and_create(file_name)
    else:
        print(f"ОШИБКА: Файл {file_name} не существует в текущей директории.")




"""
    Сканирует входной файл и создает новую папку вывода с количеством токенов и текущей датой в качестве имени папки.
    Копирует содержимое входного файла в новый файл с именем "tokens.txt" в папке вывода.

    Args:
        file_name (str): Имя входного файла.

    Returns:
        None

    Raises:
        FileNotFoundError: Если файл не существует.
"""
def scan_files_and_create(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    print(f"Файл {file_name} был успешно сканирован.")

    # Достаём токены и узнаем сколько их
    last_parts = [line.split(':')[-1].strip() for line in lines]
    last_parts_combined = '\n'.join(last_parts)
    count = len(last_parts)
    print(f"Количество токенов: {count}")

    # Создаём папку с кол-во токенов и текущей датой
    new_folder_name = f"{count} TOKENS {
        datetime.now().strftime('[%d-%m-%Y] [%H-%M-%S]')}"
    folder_path = os.path.join(folder_name, new_folder_name)
    os.makedirs(folder_path)

    # Создаём файл с токенами
    new_file_name = os.path.join(folder_path, "tokens.txt")
    with open(new_file_name, 'w') as file:
        file.writelines(last_parts_combined)
    print(f"Файл {new_file_name} был успешно создан.")

    # Копируем содержимого input.txt в log_pass.txt
    new_file_name = os.path.join(folder_path, "log_pass.txt")
    shutil.copy(file_name, new_file_name)
    print(f"Файл {new_file_name} был успешно создан.")
    with open('input.txt', 'w') as file:
        file.write('')
    print("Содержимое файла input.txt было успешно удалено.")

    print("Работа успешно выполнена")


check_file_exists(file_name, folder_name)
input("Нажмите enter что бы закрыть...")
