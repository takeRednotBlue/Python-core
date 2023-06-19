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
from commands_parser import commands_parser
from handlers import *

max = Record(Name('Max'), Phone('0933434459'))
valera = Record(Name('Valera'), Phone('0933434459'))
anton = Record(Name('Anton'), Phone('0933434459'))
vlad = Record(Name('Vlad'), Phone('0933434459'))
yura = Record(Name('Yura'), Phone('0933434459'))
sasha = Record(Name('Sasha'), Phone('0933434459'))
bogdan = Record(Name('Bogdan'), Phone('0933434459'), Birthday("26.06.1996"))
valentun = Record(Name('Valentun'), Phone('0933434459'))
tolya = Record(Name('Tolya'), Phone('0933434459'))

ab = AddressBook('ab.bin')
ab.add_record(max)
ab.add_record(valera)
ab.add_record(vlad)
ab.add_record(yura)
ab.add_record(sasha)
ab.add_record(bogdan)
ab.add_record(valentun)
ab.add_record(tolya)

COMMANDS = {
    'hello': greet,
    'add': add_contact,
    'remove': remove_contact,
    'change': change_number,
    'phone': show_contact_numbers,
    'show all': show_whole_contacts_book,
    'help': get_help,
    'birthday': birthday_handler,
}

END_COMMANS = ['exit', 'good bye', 'close']


def main():

    # Handles address_book book file
    # contacts_book_file = Path().home() / 'address_book.json'          
    contacts_book_file = Path(__file__).parent / 'address_book.bin'          
    if contacts_book_file.exists():
        address_book = AddressBook(contacts_book_file).read_from_file()
    else:
        address_book = AddressBook(contacts_book_file)

    # address_book = ab
    is_working = True

    print('Hello, I\'m your personal bot-assistant.')

    while is_working:
        user_input = input('>>> ')
        command, arguments = commands_parser(user_input)
        if command in COMMANDS:
            command_handler = COMMANDS[command]
            command_handler(arguments, address_book)
        elif command in END_COMMANS:
            exit_bot()
            address_book.save_to_file()
            is_working = False
        else:
            print('Command not found. Use "help" for available commands.')


if __name__ == '__main__':
    main()

