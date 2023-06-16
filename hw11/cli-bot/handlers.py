from classes import *
from error_handlers import input_error


def greet(*_, **__):
    print('How can I help you?')

@input_error
def add_contact(args: list, address_book: AddressBook) -> None:
    name, phone, birthday = args[0], args[1], args[2]
    if name in address_book:
        # normalize phone before checking in record list because of normalization under the hood of Phone class
        if Phone(phone).get_phone() not in address_book[name].get_phones():
            address_book[name].add_phone(phone)
            print(f'Phone \'{phone}\' was successfully added to the contact \'{name}\'.')
        else:
            raise PhoneAlreadyExistsError
    else:
        record = Record(name, phone, birthday)
        address_book.add_record(record)
        print(f'Contact \'{name}\' with phone number \'{phone}\' was successfully added.')

@input_error
def remove_contact(args: list, address_book: AddressBook) -> None:
    name = args[0]
    # can take phone as second argument to remove it from contact
    if args [1]:
        phone = args[1]
        address_book[name].remove_phone(phone)
        print(f'Phone number \'{phone}\' from contact \'{name}\' was successfully removed.')
    else:
        address_book.remove_record(name)
        print(f'Contact \'{name}\' was successfully removed.')
    
    
@input_error
def change_number(args: list, address_book: AddressBook) -> None:
    name, phone, new_phone = args[0], args[1], args[2]
    address_book[name].change_phone(phone, new_phone)
    print(f'\'{name}\' phone number \'{phone}\' was successfully changed to \'{new_phone}\'.')
    

@input_error
def show_contact_numbers(args: list, address_book: AddressBook) -> None:
    name = args[0]
    phones = address_book[name].get_phones()
    phones_str = ', '.join(phones)
    print(f'\'{name}\' phone numbers are \'{phones_str}\'.')
  

def show_whole_contacts_book(_, address_book: AddressBook) -> None:
    count = 1
    print('='*59)
    print('|{:^5}|{:^20}|{:^30}|'.format('N', 'Name', 'Phone numbers'))
    print('='*59)
    
    if address_book:
        for name, record in address_book.items():
            phones = record.get_phones()
            # handle contact's multiple phones
            if len(phones) == 1: 
                print('|{:>4} |{:^20}|{:^30}|'.format(count, name, phones[0]))
            elif  len(phones) > 1:
                print('|{:>4} |{:^20}|{:^30}|'.format(count, name, phones[0]))
                for phone in phones[1:]:
                    print('|{0:>4} |{0:^20}|{1:^30}|'.format('', phone))
            else:
                print('|{:>4} |{:^20}|{:^30}|'.format(count, name, 'No phones'))

            count += 1
    else:
        print('|{0:>4} |{1:^20}|{0:^30}|'.format('', 'No entries'))

    print('='*59)
    
def exit_bot():
    print('I\'ll miss you so much!')
   

def get_help(*_, **__) -> None:
    print(
    """Important! Divide command and arguments only by using white spaces in the other case it can lead to errors 
or data coruption. Don't terminate bot with CTRL+C combination because all unsaved changes will be lost.

Available commands:
    - hello                                 Greet user
    - add <name> <phone>                    Add a new contact
    - change <name> <phone> <new_phone>     Change the phone number of an existing contact
    - remove <name> <phone>(opt)            Remove contact or phone number if phone was given
    - phone <name>                          Get the phone numbers
    - show all                              Display contacts book
    - help                                  Show this help message
    - good bye, close, exit                 End the bot
    """
    )