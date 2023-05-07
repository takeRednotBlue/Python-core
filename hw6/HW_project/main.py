"""
<<<<<<< HEAD
1. Скрипт приймає один аргумент при запуску це шлях до папки для сортування.
2. Також за бажанням можна прописати другим аргументом "backup", що вкаже скрипту
перед сортування заархівувати папку яку буде сортовано на помістити цей архів в середину.
3. Результати роботи скрипту виводяться в термінал, а також створююється два текстові файли 
один з яким містить туж інформацію що і виведено до терміналу, а також лог* сортування.
Другий містить в собі лог* нормалізації.
* Мається на увазі список шляхів до сортування/нормалізації та після.
"""

import sys
from tools import *
from pathlib import Path

def main(path, backup=False):
    path = Path(path)
    if backup == True: 
        create_backup_copy(path)

    # Main logic. Results of the functions assign to variables for future reporting
    
    files_num_init = files_amount(path)
    normalized_log, normalized_files = normalize(path)
    sort_log, unpacked_archs_count = sort_dir(path)
    removed_dirs = remove_empty_dirs(path)
    
    # Shows results of script in terminal

    dirs_info(path)
    print(f'''
{'Amount of sorted files:':<30} {files_num_init}
{'Normalized files:':<30} {normalized_files}
{'Unpacked archives:':<30} {unpacked_archs_count}
{'Removed empty directories:':<30} {removed_dirs}
''')

    # Creates two file. First one contains results of the script work and sorting log. 
    # Second contains log of normalized files.

    make_report(path, backup)
    with open(path / 'report.txt', 'a', encoding="utf-8") as rep:
        rep.write(
f'''
{'Amount of sorted files:':<30} {files_num_init}
{'Normalized files:':<30} {normalized_files}
{'Unpacked archives:':<30} {unpacked_archs_count}
{'Removed empty directories:':<30} {removed_dirs}
'''
        )
        rep.write("\nSort log:\n")
        for pair in sort_log:
            rep.write(f"{pair[0]} --> {pair[1]}\n")
        
    with open(path / 'normalized_log.txt', 'w', encoding="utf-8") as rep:
        rep.write(f"\nScript normalized {normalized_files} files.\n\n")
        rep.write("Normalize log:\n\n")
        for pair in normalized_log:
            rep.write(f"{pair[0]} --> {pair[1]}\n")



if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[2] == 'backup':
        backup_archive = True
    else:
        backup_archive = False
    
    try:
        path = rf"{sys.argv[1]}"
        try:
            main(path, backup_archive)
=======

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
>>>>>>> cbbea46da5faa5421a71f2bd5182dbd3b9844bee
        except FileNotFoundError as e:
            print(f"Invalid path argument: {e}")
    except IndexError as err:
        print(f"At least 1 argument should be passed: {err}")
    
    

<<<<<<< HEAD
=======
# a = normalize("D:\Download")
# for _ in a:
#     print(f"'{_}' file had similar stem.")
>>>>>>> cbbea46da5faa5421a71f2bd5182dbd3b9844bee
