from classes import *
from error_handlers import input_error


def greet(*_, **__):
    print('How can I help you?')

@input_error
def add_contact(args: list, address_book: AddressBook) -> None:
    if len(args) > 2:
        name, phone, birthday = Name(args[0]), Phone(args[1]), Birthday(args[2])
    name, phone = Name(args[0]), Phone(args[1])
    
    if name.value in address_book:
        # normalize phone before checking in record list because of normalization under the hood of Phone class
        if phone not in address_book[name.value].phones:
            address_book[name.value].add_phone(phone)
            print(f'Phone \'{phone}\' was successfully added to the contact \'{name}\'.')
        else:
            raise PhoneAlreadyExistsError
    else:
        if len(args) > 2:
            record = Record(name, phone, birthday)
        record = Record(name, phone)
        address_book.add_record(record)
        print(f'Contact was successfully added.')

@input_error
def birthday_handler(args: list, address_book: AddressBook) -> None:
    if len(args) >= 2:
        name, birthday = args[0], Birthday(args[1])
        if address_book[name].birthday != None:
            user_input = input(f'Do you wanna chage birthday date for \'{name}\'? (y/N)')
            if user_input == 'y':
                address_book[name].birthday = birthday
                print('Birthday date was successfully changed.')
        else:
            address_book[name].birthday = birthday
            print('Birthday date was successfully set.')
    else:
        name = args[0]
        days_to_birthday = address_book[name].days_to_birthday()
        print(f'{days_to_birthday} days to \'{name}\' birthday.')

@input_error
def remove_contact(args: list, address_book: AddressBook) -> None:
    name = args[0]
    # takes phone as second argument to remove it from contact
    if len(args) >= 2:
        phone = Phone(args[1])
        address_book[name].remove_phone(phone)
        print(f'Phone number \'{phone}\' was successfully removed.')
    else:
        address_book.remove_record(name)
        print(f'Contact \'{name}\' was successfully removed.')
    
    
@input_error
def change_number(args: list, address_book: AddressBook) -> None:
    name, phone, new_phone = args[0], Phone(args[1]), Phone(args[2])
    address_book[name].change_phone(phone, new_phone)
    print(f'Phone number \'{phone}\' was successfully changed to \'{new_phone}\'.')
    

@input_error
def show_contact_numbers(args: list, address_book: AddressBook) -> None:
    name = args[0]
    phones = address_book[name].get_phones()
    phones_str = ', '.join(phones)
    if not phones:
        print(f'\'{name}\' doesn\'t have phone numbers.')
    elif len(phones) == 1:
        print(f'\'{name}\' phone number: \'{phones_str}\'.')
    else:
        print(f'\'{name}\' phone numbers: \'{phones_str}\'.')
  

def show_whole_contacts_book(_, address_book: AddressBook) -> None:
    count = 1
    print('='*59)
    print('|{:^5}|{:^20}|{:^30}|'.format('N', 'Name', 'Phone numbers'))
    print('='*59)
    
    if address_book:
        for page in address_book.iterator():
            for name, record in page:
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
                print('='*59)

                count += 1
            if len(page) == 5:   
                # user_check = input('Press enter to see the next page.')
                user_input = input('Do you wanna see next page? (Y/n) ')
                if user_input == 'n':
                    break
    else:
        print('|{0:>4} |{1:^20}|{0:^30}|'.format('', 'No entries'))

    
def exit_bot():
    print('I\'ll miss you so much!')
   

def get_help(*_, **__) -> None:
    print(
    """Important! Divide command and arguments only by using white spaces in the other case it can lead to errors 
or data coruption. Don't terminate bot with CTRL+C combination because all unsaved changes will be lost.

Available commands:
    - hello                                 Greet user
    - add <name> <phone>                    Add a new contact
    - birthday <date>(opt)                  Shows how many days to birthday or set birthday date 
    - change <name> <phone> <new_phone>     Change the phone number of an existing contact
    - remove <name> <phone>(opt)            Remove contact or phone number if phone was given
    - phone <name>                          Get the phone numbers
    - show all                              Display contacts book
    - help                                  Show this help message
    - good bye, close, exit                 End the bot
    """
    )