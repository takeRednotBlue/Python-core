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
1. Створити резервну копію файлів у вигляді архіву та запитувати про її створення при виклику скрипта.
2. Створювати файл звіту. Прописати його зміст та структуру.
3. Створити файл Readme з описом роботи скрипта.
4. Вивести необхідну інформацію на екран по завершенню роботи скрипта.
5. Оптимізувати написаний код.


"""
import sys 
from tools import *

def main(path):
    files_amount = len([file for file in get_all_items(Path(path))])

    normalized_log, normalized_files = normalize(path)
    sort_dir(path)
    removed_dirs = remove_empty_dirs(path)
    
    files_amount_sorted = len([file for file in get_all_items(Path(path))])
    
    make_report(path)
    dirs_info(path)
    print(f'Amount of files before {files_amount} and after {files_amount_sorted} running the script.\nRemoved {removed_dirs} empty directories.')
   
    with open(Path(path) / 'report.txt', 'a', encoding="utf-8") as rep:
        rep.write(f"\nScript normalized {normalized_files} files.\n")
        rep.write("\nLog of normalization:\n")
        for pair in normalized_log:
            rep.write(f"{pair[0]} --> {pair[1]}\n")
        

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