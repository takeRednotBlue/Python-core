"""

Порядок написання бота:
    1. Створити функції обробки команд.
        - Перевірка коректності введеного номеру.
        - Виведення номерів в єдиному форматі
        - Відображати контакти в алфавітному порядку
    2. На основі фукцій створити декоратор обробки помилок.
    3. Записувати контакти у файл .json та зчитувати дані з нього:
        - зчитувати дані при запуску бота та зберігати в словник.
        - при закінченні роботи програми словник (зі змінами чи без) перезаписувати у файл
    4. Прописати логіку бота включаючи у функції main()

    Commands:
    - hello - Greating user
    - add - add contact (name, phone) to the contacts dict
    - change - change phone of existing number
    - remove - removes contact from the contacts book
    - phone - phone of the given contact
    - show all - show all contacts
    - good bye, close, exit - end bot
    - help - output commands list with their descriptions

  """


import json
from pathlib import Path
from src.command_parser import commands_parser
from src.handlers import *


COMMANDS = {
    'hello': greet,
    'add': add_contact,
    'remove': remove_contact,
    'change': change_number,
    'phone': show_contact_number,
    'show all': show_whole_contacts_book,
    'help': get_help,
}

END_COMMANS = ['exit', 'good bye', 'close']


def main():

    # Handles contacts_book book file
    contacts_book_file = Path().home() / 'contacts_book.json'          
    if contacts_book_file.exists():
        with open(contacts_book_file, 'r') as file:
            contacts_book = json.load(file)
    else:
        contacts_book_file.touch()
        contacts_book = {}

    is_working = True

    print('Hello, I\'m your personal bot-assistant.')

    while is_working:
        user_input = input('>>> ')
        command, arguments = commands_parser(user_input)
        if command in COMMANDS:
            command_handler = COMMANDS[command]
            command_handler(arguments, contacts_book)
        elif command in END_COMMANS:
            exit_bot()
            with open(contacts_book_file, 'w') as file:
                json.dump(contacts_book, file, sort_keys=True)
            is_working = False
        else:
            print('Command not found. Use "help" command to look at available commands.')


if __name__ == '__main__':
    main()

