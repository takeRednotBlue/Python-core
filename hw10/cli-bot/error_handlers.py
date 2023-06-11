from classes import PhoneNotFoundError

# Lists of commads handlers sorted by argumets they take.
HAS_NO_ARGS = [
    "greet",
    "show_whole_contacts_book",
    "get_help"
]

HAS_NAME_AND_PHONE_ARGS = [
    "add_contact",
    "change_number",
]

HAS_ONLY_NAME_ARG = [
    'phone',
    "remove_contact",
    "show_contact_number",
]

def input_error(func):
    def wrapper(*args):
        try:
            func(*args)
        except IndexError as inderr:
            if func.__name__ in HAS_NAME_AND_PHONE_ARGS:
                print('Missing arguments. Please write name and phone number.')
            elif func.__name__ in HAS_ONLY_NAME_ARG:
                print('Missing argument. Plese wrinte contact\'s name.')
        except KeyError as keyerr:
            print(f'Cannot find such contact. Please check spelling and try again.')
        except ValueError:
            if func.__name__ == 'add_contact':
                print(f'Contact {0} already exist. If you want to change phone number use "change" command.')
        except PhoneNotFoundError:
            if func.__name__ == 'change_number':
                print('Phone was not found.')
            
    return wrapper
