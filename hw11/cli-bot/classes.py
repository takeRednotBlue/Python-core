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
import re


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
    
    def iterator(self, number=5):
        sorted_data = sorted(self.data.items())
        index = 0
        while index < len(sorted_data):
            yield sorted_data[index:index+number]
            index += number
    

class Record:
    def __init__(self, name, phone=None, birthday=None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone):
        if phone not in self.phones:
            self.phones.append(phone)
        else:
            raise PhoneAlreadyExistsError

    def change_phone(self, phone, new_phone):      
        if phone in self.phones:
            phone_pos = self.phones.index(phone)
            self.phones.insert(phone_pos, new_phone)
            self.phones.remove(phone)
        else:
            raise PhoneNotFoundError
        
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            raise PhoneNotFoundError

    def get_phones(self):
       phones_list = [phone.value for phone in self.phones]
       return phones_list
    
    def days_to_birthday(self):
        if self.birthday != None:
            today = datetime.now().date()
            difference = self.birthday.value.replace(year=today.year) - today
            if difference.days < 0:
                difference = self.birthday.value.replace(year=today.year+1) - today
            return difference.days
        else:
            raise ValueError('Contact\'s birthday hasn\'t set yet.')
    

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
    def value(self, phone):
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
    def value(self, name):
        if len(name) >= 3 and name[0].isalpha():
            self._value = name
        else:
            raise ValueError('Invalid name. Name must start from letter and has at least 3 symbols.')      

    def get_name(self):
        return self.value

    
class Birthday(Field):
    def __init__(self, value):
        super().__init__(value)
    
    @Field.value.setter
    def value(self, date):
        birthday = self.date_converter(date)
        approx_age = datetime.now().year - birthday.year
        if 1 <= approx_age <= 120:
            self._value = birthday
        else:
            raise ValueError('Invalid date format.')

    def date_converter(self, date):
        '''
        Available formats: '12.03.2023', '12/14/2023', '12.03.23', '12/03/23', '2023-03-12'
        '''
        date_mapping = {
                r'\d{2}\.\d{2}\.\d{4}': '%d.%m.%Y',
                r'\d{2}/\d{2}/\d{4}': '%d/%m/%Y',
                r'\d{2}\.\d{2}\.\d{2}': '%d.%m.%y',
                r'\d{2}/\d{2}/\d{2}': '%d/%m/%y',
                r'\d{4}-\d{2}-\d{2}': '%Y-%m-%d',
        }
        
        for pattern, format in date_mapping.items():
            if re.match(pattern, date):
                try:
                    date_obj = datetime.strptime(date, format).date()
                    return date_obj
                except ValueError:
                    print('Invalid date format.')
        else:
             raise ValueError('Invalid date format.')
        
    def get_birthday(self):
        return str(self.value)
    
    def __str__(self):
        return self.value.strftime('%d.%m.%Y')
    
    def __eq__(self, other):
        if other == None:
            return False
        return str(self.value) == str(other.value)
    
    def __len__(self):
        pass
        
    

if __name__ == "__main__":
    # name = Name('Bill')
    # name2 = Name('1John')
    phone = Phone('0234567890')
    phone2 = Phone('0932567890')
    phone3 = Phone('0932567891')
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
    # print(name)
    # print(name2)
    # print(phone)

    # record = Record('Maxym', birthday='10.08.1996')

    # print(record.days_to_birthday())

    # to_birthday = datetime(year=2023, month=6, day=17).date() - datetime.now().date()
    # print(to_birthday.days)

    assert Birthday("10.03.2023")
    print('All Ok)')



    
