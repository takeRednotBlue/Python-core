"""

Порядок написання бота:
    1. Створити функції обробки команд.
    2. На основі фукцій створити декоратор обробки помилок.
    3. Записувати контакти у файл .json та зчитувати дані з нього:
        - зчитувати дані при запуску бота та зберігати в словник.
        - при закінченні роботи програми словник (зі змінами чи без) перезаписувати у файл
    4. Прописати логіку бота включаючи у функції main()

Умови

    Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.
    Бот завершує свою роботу, якщо зустрічає слова: "good bye", "close", "exit".
    Бот не чутливий до регістру введених команд.
    Бот приймає команди:
        "hello", відповідає у консоль "How can I help you?"
        "add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. Замість ... користувач вводить ім'я та номер 
        телефону, обов'язково через пробіл.
        "change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... користувач вводить ім'я та 
        номер телефону, обов'язково через пробіл.
        "phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... користувач вводить ім'я 
        контакту, чий номер потрібно показати.
        "show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
        "good bye", "close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
    Всі помилки введення користувача повинні оброблятися за допомогою декоратора input_error. Цей декоратор відповідає за повернення 
    користувачеві повідомлень типу "Enter user name", "Give me name and phone please" тощо. Декоратор input_error повинен обробляти винятки, що 
    виникають у функціях-handler (KeyError, ValueError, IndexError) та повертати відповідну відповідь користувачеві.
    Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
    Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.

    Commands:
    - hello - start bot
    - add - add contact (name, phone) in dict
    - change - change phone of existing number
    - phone - phone of the given contact
    - show all - show all contacts
    - good bye, close, exit - end bot
    - help - output commands list with their descriptions

    Помилки що можуть виникати при роботі з хеннлерами.
        1. Відсутня команда.
        2. 
"""


import argparse



contacts = {}

def input_error(func):
    # try:
    #     result
    pass

def commands_parser(input: str) -> tuple:
    # hello *args(ignore)
    # add <name> <phone> *args(ignore)
    # change <name> <phone> *args(ignore)
    # phone <name> *args(ignore)
    # show all *args(ignore)
    # good bye|close|exit *args(ignore)
    # help *args(ignore)
    words_list = input.split()
    if words_list[0] == 'show' or words_list[0] == 'good':
        command = ' '.join(words_list[:2])
        arguments = words_list[2:]
    else:
        command = words_list[0]
        arguments = words_list[1:]
    
    return command, arguments

def greet(*args):
    print('How can I help you!')

def add_contact(args: list):
    name, phone = args[0], args[1]
    if args[0] in contacts:
        print('Contact {name} already exists.')
    else:
        contacts[name] = phone
        print(f'Contact "{name}" with phone number {phone} was successfully added.')
    

def change_number(args: list):
    name, phone = args[0], args[1]
    if name in contacts:
        contacts[name] = phone
        print(f'"{name}" phone number was successfully changed to {phone}.')
    else:
        print(f'Contact "{name}" does\'t exist. Try to create new with \'add\' command.')

def show_contact_number(args: list):
    name = args[0]
    if name in contacts:
        phone = contacts[name] 
        print(f'"{name}" phone number is {phone}.')
    else:
        print(f'"{name}" contact doesn\'t exist.')   

def show_whole_contacts_book(*args):
    count = 1
    print('='*44)
    print('|{:^5}|{:^20}|{:^15}|'.format('N', 'Name', 'Phone number'))
    print('='*44)
    for name, phone in contacts.items():
        print('|{:>4} |{:^20}|{:^15}|'.format(count, name, phone))
        count += 1
    print('='*44)
    
def exit_bot():
    print('I\'ll miss you so much!')
    # global is_working
    # is_working = False

def help():
    pass

COMMANDS = {
    'hello': greet,
    'add': add_contact,
    'change': change_number,
    'phone': show_contact_number,
    'show all': show_whole_contacts_book,
    # 'good bye': exit_bot, 
    # 'close': exit_bot,
    # 'exit': exit_bot,
    'help': None,
}

def main():
    is_working = True

    print('Hello, I\'m your personal bot-assistant.')
    while is_working:
        user_input = input('>>> ')
        command, arguments = commands_parser(user_input)
        if command in COMMANDS:
            command_handler = COMMANDS[command]
            command_handler(arguments)
        elif command == 'exit':
            exit_bot()
            is_working = False


if __name__ == '__main__':
    main()

