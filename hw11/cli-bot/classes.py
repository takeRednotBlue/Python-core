"""
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


class PhoneNotFoundError(Exception):
    pass

class PhoneAlreadyExistsError(Exception):
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
    def __init__(self, name, phone=None):
        self.name = Name(name)
        self.phones = []
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        phone = Phone(phone)
        if phone.get_phone() not in self.get_phones():
            self.phones.append(phone)
        else:
            raise PhoneAlreadyExistsError

    def change_phone(self, phone, new_phone):
        phone = Phone(phone)
        new_phone = Phone(new_phone)
        changed = False

        for item in self.phones:
            if phone.get_phone() == item.get_phone():
                item_pos = self.phones.index(item)
                self.phones.insert(item_pos, new_phone)
                self.phones.remove(item)
                changed = True

        if not changed:
            raise PhoneNotFoundError
        
    def remove_phone(self, phone):
        phone = Phone(phone)
        removed = False

        for item in self.phones:
            if phone.get_phone() == item.get_phone():
                self.phones.remove(item)
                removed = True

        if not removed:
            raise PhoneNotFoundError

    def get_phones(self):
       phones_list = [phone.get_phone() for phone in self.phones]
       return phones_list
    

class Field:
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        self._normalize_phone()

    def _normalize_phone(self):
        if len(self.value) == 12:
            self.value = '+' + self.value
        elif len(self.value) == 10:
            self.value = '+38' + self.value
        else:
            return f'Note: format of the phone \'{self.value}\' doesn\'t comply to the nation phone numbers conventions.'
  
    def get_phone(self):
        return self.value

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def get_name(self):
        return self.value


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
