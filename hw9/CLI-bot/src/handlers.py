

from src.decorators import input_error



def greet(*args):
    print('How can I help you?')

@input_error
def add_contact(args: list, contacts_book: dict):
    name, phone = args[0], args[1]
    if name in contacts_book:
        raise ValueError
    else:
        contacts_book[name] = phone
        print(f'Contact "{name}" with phone number {phone} was successfully added.')

@input_error
def remove_contact(args: list, contacts_book: dict):
    name = args[0]
    phone = contacts_book.pop(name)
    print(f'Contact "{name}" was successfully removed.')
    
    
@input_error
def change_number(args: list, contacts_book: dict):
    name, phone = args[0], args[1]
    if name in contacts_book:
        contacts_book[name] = phone
        print(f'"{name}" phone number was successfully changed to {phone}.')
    else:
        raise KeyError

@input_error
def show_contact_number(args: list, contacts_book: dict):
    name = args[0]
    phone = contacts_book[name] 
    print(f'"{name}" phone number is {phone}.')
  

def show_whole_contacts_book(args: list, contacts_book: dict):
    count = 1
    print('='*44)
    print('|{:^5}|{:^20}|{:^15}|'.format('N', 'Name', 'Phone number'))
    print('='*44)
    
    if contacts_book:
        for name, phone in contacts_book.items():
            print('|{:>4} |{:^20}|{:^15}|'.format(count, name, phone))
            count += 1
    else:
        print('|{0:>4} |{1:^20}|{0:^15}|'.format('', 'No entries'))

    print('='*44)
    
def exit_bot():
    print('I\'ll miss you so much!')
   

def get_help(args: list, contacts_book: dict):
    print(
    """exImportant! Divide command and arguments only by using white spaces in the other case it can lead to data coruption or 
errors.

Available commands:
    - hello                     Greet user
    - add <name> <phone>        Add a new contact
    - change <name> <phone>     Change the phone number of an existing contact
    - remove <name>             Remove contact
    - phone <name>              Get the phone number
    - show all                  Display contacts book
    - help                      Show this help message
    - good bye, close, exit     End the bot
    """
    )