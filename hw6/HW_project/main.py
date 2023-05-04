"""

1. Має бути окрема функція для обробки папок яка викликається рекурсивно (можна використати glob? 
або краще iterdir())
2. Функція має повертати список файлів в кожній категорії, перелік всіх розширень з папки, перелік всіх відомих розширень.
3. Потрібно додати функції, які будуть відповідати за обробку кожного типу файлу.
4. Переіменувати папки/файли через функцію normalize() (транслітерація, всі інші символи "_") Приймає радок та повертає рядок, великі залишаються великими. 
5. Видаляти порожні папки
6. Скрипт ігнорує папки з сортованими файлами.
7. Архіви розпакувати в папку з назвою архіву

Додатково:
1. Створити резервну копію файлів у вигляді архіву.


"""
import sys 
from tools import *

def main(path):
    files_amount = len([file for file in get_all_items(Path(path))])
    normalized_files = normalize(path)
    sort_dir(path)
    removed_dirs = remove_empty_dirs(path)
    files_amount_sorted = len([file for file in get_all_items(Path(path))])
    make_report(path)
    dirs_info(path)
    print(f'Amount of files before {files_amount} and after {files_amount_sorted} running the script.\nRemoved {removed_dirs} empty directories.')
    


if __name__ == '__main__':
    try:
        path = rf"{sys.argv[1]}"
        try:
            main(path)
        except FileNotFoundError as e:
            print(f"Invalid path argument: {e}")
    except IndexError as err:
        print(f"At least 1 argument should be passed: {err}")
    
    

# a = normalize("D:\Download")
# for _ in a:
#     print(f"'{_}' file had similar stem.")