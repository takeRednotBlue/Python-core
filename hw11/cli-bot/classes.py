"""
Завдання

У цьому домашньому завданні ми:

    Додамо поле для дня народження Birthday. Це поле не обов'язкове, але може бути тільки одне.
    Додамо функціонал роботи з Birthday у клас Record, а саме функцію days_to_birthday, яка повертає кількість днів до наступного дня народження.
    Додамо функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
    Додамо пагінацію (посторінкове виведення) для AddressBook для ситуацій, коли книга дуже велика і потрібно показати вміст частинами, а не все 
    одразу. Реалізуємо це через створення ітератора за записами.

Критерії приймання:

    AddressBook реалізує метод iterator, який повертає генератор за записами AddressBook і за одну ітерацію повертає представлення для N записів.
    Клас Record приймає ще один додатковий (опціональний) аргумент класу Birthday
    Клас Record реалізує метод days_to_birthday, який повертає кількість днів до наступного дня народження контакту, якщо день народження заданий.
    setter та getter логіку для атрибутів value спадкоємців Field.
    Перевірку на коректність веденого номера телефону setter для value класу Phone.
    Перевірку на коректність веденого дня народження setter для value класу Birthday.
"""

from collections import UserDict
from datetime import datetime


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
    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = birthday
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
        # removed = False

        # for item in self.phones:
        #     if phone.get_phone() == item.get_phone():
        #         self.phones.remove(item)
        #         removed = True

        # if not removed:
        #     raise PhoneNotFoundError
            
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise PhoneNotFoundError

    def get_phones(self):
       phones_list = [phone.get_phone() for phone in self.phones]
       return phones_list
    
    def days_to_birthday(self):
        pass
    

class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    def __eq__(self, other):
        return self.value == other.value
            
    def __str__(self):
        return str(self.value)
    
    def __len__(self):
        return len(self.value)
    


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    def value(self, phone: str):
        if phone.isnumeric():
            if len(phone) == 12 and phone.startswith('380'):
                self._value = '+' + phone
            elif len(phone) == 10 and phone.startswith('0'):
                self._value = '+38' + phone
            elif len(phone) == 13 and phone.startswith('+380'):
                self._value = phone
            else:
                raise ValueError(f'Phone\'s format \'{phone}\' must comply to the national phone numbers conventions.')
        else:
            raise ValueError(f'Phone\'s format \'{phone}\' must comply to the national phone numbers conventions.')
  
    def get_phone(self):
        return self.value
    
    

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    @Field.value.setter
    def value(self, name: str):
        if len(name) >= 3 and name[0].isalpha():
            self._value = name
        else:
            raise ValueError('Invalid name. Name must start from letter and has length at least 3.')      

    def get_name(self):
        return self.value

    
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
    
    @Field.value.setter
    def value(self):
        pass
    

if __name__ == "__main__":
    name = Name('Bill')
    name2 = Name('1John')
    # phone = Phone('0234567890')
    # phone2 = Phone('234567890')
    # rec = Record(name, phone)
    # ab = AddressBook()
    # ab.add_record(rec)
    # assert isinstance(ab['Bill'], Record)
    # assert isinstance(ab['Bill'].name, Name)
    # assert isinstance(ab['Bill'].phones, list)
    # assert isinstance(ab['Bill'].phones[0], Phone)
    # assert ab['Bill'].phones[0].value == '1234567890'
    # assert phone == phone2
    # print(phone)
    # print(phone2)
    print(name)
    print(name2)
    print('All Ok)')
    # print(phone)

    

