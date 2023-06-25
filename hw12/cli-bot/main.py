from pathlib import Path
from commands_parser import commands_parser
from handlers import *

# max = Record(Name('Max'), Phone('0933434459'))
# valera = Record(Name('Valera'), Phone('0933434459'))
# anton = Record(Name('Anton'), Phone('0933434459'))
# vlad = Record(Name('Vlad'), Phone('0933434459'))
# yura = Record(Name('Yura'), Phone('0933434459'))
# sasha = Record(Name('Sasha'), Phone('0933434459'))
# bogdan = Record(Name('Bogdan'), Phone('0933434459'), Birthday("26.06.1996"))
# valentun = Record(Name('Valentun'), Phone('0933434459'))
# tolya = Record(Name('Tolya'), Phone('0933434459'))

# ab = AddressBook('ab.bin')

# ab.add_record(max)
# ab.add_record(valera)
# ab.add_record(vlad)
# ab.add_record(yura)
# ab.add_record(sasha)
# ab.add_record(bogdan)
# ab.add_record(valentun)
# ab.add_record(tolya)

COMMANDS = {
    'hello': greet,
    'add': add_contact,
    'remove': remove_contact,
    'change': change_number,
    'phone': show_contact_numbers,
    'show all': show_whole_contacts_book,
    'help': get_help,
    'birthday': birthday_handler,
    'find': find_contacts,
    'clear': clear_book,
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

