"""

1. Має бути окрема функція для обробки папок яка викликається рекурсивно (можна використати glob? 
або краще iterdir())
2. Функція має повертати список файлів в кожній категорії, перелік всіх розширень з папки, перелік всіх відомих розширень.
3. Потрібно додати функції, які будуть відповідати за обробку кожного типу файлу.
4. Переіменувати папки/файли через функцію normalize() (транслітерація, всі інші символи "_") 
Приймає радок та повертає рядок, великі залишаються великими. 
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
from datetime import datetime
from tools import *

def main(path, backup=False):
    path = Path(path)
    if backup == True: 
        create_backup_copy(path)

    '''Main logic. Results of the sript work assign to variables
    for future reporting'''
    
    files_num_init, dirs_num_init, suffixes_init = dir_info(path)
    normalized_log, normalized_files = normalize(path)
    sort_log, unpacked_archs_count = sort_dir(path)
    removed_dirs = remove_empty_dirs(path)
    # files_num_final, dirs_num_final, suffixes_final = dir_info(path)
    
    dirs_info(path)
    make_report(path, backup)
    print(f'''
{'Amount of sorted files:':<30} {files_num_init}
{'Normalized files:':<30} {normalized_files}
{'Unpacked archives:':<30} {unpacked_archs_count}
{'Removed empty directories:':<30} {removed_dirs}
{"Directory's file suffixes:":<30} 
{', '.join(map(repr, suffixes_init))}
''')


    with open(path / 'report.txt', 'a', encoding="utf-8") as rep:
        rep.write(
f'''
{'Amount of sorted files:':<30} {files_num_init}
{'Normalized files:':<30} {normalized_files}
{'Unpacked archives:':<30} {unpacked_archs_count}
{'Removed empty directories:':<30} {removed_dirs}
{"Directory's file suffixes:"} 
{', '.join(map(repr, suffixes_init))}
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
        except FileNotFoundError as e:
            print(f"Invalid path argument: {e}")
    except IndexError as err:
        print(f"At least 1 argument should be passed: {err}")
    
    

