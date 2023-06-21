"""
Завдання

У цьому домашньому завданні вам потрібно:

    Додати функціонал збереження адресної книги на диск та відновлення з диска. Для цього ви можете вибрати будь-який зручний для вас протокол 
    серіалізації/десеріалізації даних та реалізувати методи, які дозволять зберегти всі дані у файл і завантажити їх із файлу.

    Додати користувачеві можливість пошуку за вмістом книги контактів, щоб можна було знайти всю інформацію про одного або кількох користувачів 
    за кількома цифрами номера телефону або літерами імені тощо.

Критерії приймання:

    Застосунок не втрачає дані після виходу із застосунку та відновлює їх з файлу.
    Застосунок виводить список користувачів, у яких в імені або номері телефону є збіги із введеним рядком.
"""

from collections import UserDict
from datetime import datetime
import pickle
import re
from pathlib import Path


class PhoneNotFoundError(Exception):
    pass

class PhoneAlreadyExistsError(Exception):
    pass

class AddressBook(UserDict):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

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

    def save_to_file(self):
        with open(self.filename, 'wb') as fh:
            pickle.dump(self, fh)
    
    def read_from_file(self):
        with open(self.filename, 'rb') as fh:
            book = pickle.load(fh)
        return book

    def find(self, search_string):
        search_result = []
        for name, record in self.data.items():
            if search_string.lower() in name.lower():
                search_result.append(self.data[name])
            else:
                for phone in record.get_phones():
                    if search_string.lower() in phone.lower():
                        search_result.append(self.data[name])
                        break
        return search_result
                        
                

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
        
    
    def __repr__(self):
        attr_dict = {
            'name': self.name,
            'phones': self.phones,
            'birthday': self.birthday,
        }
        return f'RecordObject({attr_dict})'
    

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
        if other == None:
            return False
        return str(self.value) == str(other.value)
            
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        # return f'{self.__class__.__name__}Object({self.value})'
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
    
    def __bool__(self):
        if self.value == None:
            return False
        else:
            return True
       
    def __len__(self):
        pass
        
    

if __name__ == "__main__":
    max = Record(Name('Max'), Phone('0933434459'))
    valera = Record(Name('Valera'), Phone('0933434459'))
    anton = Record(Name('Anton'), Phone('0933434459'))
    vlad = Record(Name('Vlad'), Phone('0933434459'))
    yura = Record(Name('Yura'), Phone('0933434459'))
    sasha = Record(Name('Sasha'), Phone('0933434459'))
    bogdan = Record(Name('Bogdan'), Phone('0933434459'), Birthday("26.06.1996"))
    valentun = Record(Name('Valentun'), Phone('0933434459'))
    tolya = Record(Name('Tolya'), Phone('0933434459'))

    ab = AddressBook(Path(__file__).parent / 'address_book.bin')
    ab.add_record(max)
    ab.add_record(valera)
    ab.add_record(vlad)
    ab.add_record(yura)
    ab.add_record(sasha)
    ab.add_record(bogdan)
    ab.add_record(valentun)
    ab.add_record(tolya)

    # ab.save_to_file()
    # print('Saved')
    # loaded_ab = ab.read_from_file()
    # bd_days = loaded_ab['Bogdan'].days_to_birthday()
    # print(f'There is {bd_days} days to Bogdan\'s birthday.')
    print(ab)


    print('All Ok)')



    
