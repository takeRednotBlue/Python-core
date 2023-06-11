from classes import *
from error_handlers import input_error


def greet(*args, **kwargs):
    print('How can I help you?')

@input_error
def add_contact(args: list, address_book: AddressBook) -> None:
    name, phone = args[0], args[1]
    record = Record(Name(name), Phone(phone))
    if name in address_book:
        raise ValueError
    else:
        address_book.add_record(record)
        print(f'Contact "{name}" with phone number {phone} was successfully added.')

@input_error
def remove_contact(args: list, address_book: AddressBook) -> None:
    name = args[0]
    address_book.remove_record(name)
    print(f'Contact "{name}" was successfully removed.')
    
    
@input_error
def change_number(args: list, address_book: AddressBook) -> None:
    name, phone, new_phone = args[0], args[1], args[2]
    if name in address_book:
        address_book.get(name).change_phone(phone, new_phone)
        print(f'"{name}" phone number {phone} was successfully changed to {new_phone}.')
    else:
        raise KeyError

@input_error
def show_contact_numbers(args: list, address_book: AddressBook) -> None:
    name = args[0]
    phones = address_book[name].get_phones()
    print(f'"{name}" phone numbers are {phones}.')
  

def show_whole_contacts_book(args: list, address_book: AddressBook) -> None:
    count = 1
    print('='*59)
    print('|{:^5}|{:^20}|{:^30}|'.format('N', 'Name', 'Phone numbers'))
    print('='*59)
    
    if address_book:
        for name, record in address_book.items():
            phones = record.get_phones()
            print('|{:>4} |{:^20}|{:^30}|'.format(count, name, ', '.join(phones)))
            count += 1
    else:
        print('|{0:>4} |{1:^20}|{0:^30}|'.format('', 'No entries'))

    print('='*59)
    
def exit_bot():
    print('I\'ll miss you so much!')
   

def get_help(*args, **kwargs) -> None:
    print(
    """Important! Divide command and arguments only by using white spaces in the other case it can lead to errors 
or data coruption. Don't terminate bot with CTRL+C combination because all unsaved changes will be lost.

Available commands:
    - hello                                 Greet user
    - add <name> <phone>                    Add a new contact
    - change <name> <phone> <new_phone>     Change the phone number of an existing contact
    - remove <name>                         Remove contact
    - phone <name>                          Get the phone number
    - show all                              Display contacts book
    - help                                  Show this help message
    - good bye, close, exit                 End the bot
    """
    )