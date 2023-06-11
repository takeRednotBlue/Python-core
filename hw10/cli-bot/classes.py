"""
d 
    - add contact
    - remove contact
    - change contact
    - find contact (by one or more creteria)


    В цій домашній роботі ви повинні реалізувати такі класи:

    Клас AddressBook, який наслідується від UserDict, та ми потім додамо логіку пошуку за записами до цього класу.
    Клас Record, який відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name.
    Клас Field, який буде батьківським для всіх полів, у ньому потім реалізуємо логіку, загальну для всіх полів.
    Клас Name, обов'язкове поле з ім'ям.
    Клас Phone, необов'язкове поле з телефоном та таких один запис (Record) може містити кілька.

Критерії приймання

    Реалізовано всі класи із завдання.
    Записи Record в AddressBook зберігаються як значення у словнику. Як ключі використовується значення Record.name.value.
    Record зберігає об'єкт Name в окремому атрибуті.
    Record зберігає список об'єктів Phone в окремому атрибуті.
    Record реалізує методи для додавання/видалення/редагування об'єктів Phone.
    AddressBook реалізує метод add_record, який додає Record у self.data.
"""

from collections import UserDict

class DataNotFoundError(Exception):
    pass

class PhoneNotFoundError(Exception):
    pass

class ContactNotFoundError(Exception):
    pass

class AlreadyExistsError(Exception):
    pass

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record):
        self.data.update({
            record.name.value: record,
        })
    
    def remove_record(self, name):
        self.data.pop(name)


       

class Record:
    def __init__(self, name, phone):
        self.name = name
        self.phones = []
        self.email = None
        self.add_phone(phone)

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            print(f'{phone} already exists.')

    def change_phone(self, phone, new_phone):
        changed = False
        for phone_obj in self.phones:
            if phone_obj.get_phone() == phone:
                phone_index = self.phones.index(phone_obj)
                new_phone = Phone(new_phone)
                self.phones.insert(phone_index, new_phone)
                self.phones.remove(phone_obj)
                changed = True
        if not changed:
            raise PhoneNotFoundError
        

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print(f'{phone} doesn\'t exist for {self.name} contact.')

    def get_phones(self):
       phones_list = [phone.get_phone() for phone in self.phones]
       return phones_list
    

class Field:
    pass

class Phone(Field):
    def __init__(self, value):
        self.value = value
    
    def get_phone(self):
        return self.value

class Name(Field):
    def __init__(self, value):
        self.value = value

    def get_name(self):
        return self.value

# print(dir(Field))

if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
    print(phone)