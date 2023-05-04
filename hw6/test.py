'''
Прочитати перші N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''

import sys

NUM_LINES = 4

if len(sys.argv) != 2:
    print("Please pass only 2 args!")
    quit()

# try:
#     with open(sys.argv[1]) as file:
#         counter = 0
#         line = file.readline()
#         while counter < NUM_LINES and line != '':
#             counter += 1
#             print(line.strip("\n"))
#             line = file.readline()
# except FileNotFoundError as err:
#     print(f"Помилка доступу до файлу: {err}")

"""
Вивести в консоль остання чотири рядки файлу.
"""

# try:
#     my_lines = []
#     with open(sys.argv[1]) as file:
#         for line in file:
#             my_lines.append(line)
#             if len(my_lines) > NUM_LINES:
#                 my_lines.pop(0)
#     print("".join(my_lines))
# except FileNotFoundError as err:
#     print(f"Помилка доступу до файлу: {err}")

'''
Читаємо файл за допомогою pathlib
'''

from pathlib import Path
folder = Path(".")
file = folder / 'ibm.drawio.svg'

print(file.name.split(".")[1]) # If file has more than one format
print(file.suffixes) # Return list of file's suffixes