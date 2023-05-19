"""
1. get_birthdays_per_week виводить іменинників у форматі:
    Monday: Bill, Jill
    Friday: Kim, Jan
2. Користувачів, у яких день народження був на вихідних, потрібно привітати в понеділок.
3. Для тестування зручно створити тестовий список users та заповнити його самостійно.
4. Функція виводить користувачів з днями народження на тиждень вперед від поточного дня.
Тиждень починається з понеділка.

"""

from datetime import datetime, timedelta
from collections import defaultdict

SEVEN_DAYS = 7
WEEK_START = 'Monday'

users = [
    {'name': 'Zachary Myers DDS', 'birthday': datetime(1999, 5, 28)},
    {'name': 'Tyler Morales', 'birthday': datetime(1983, 5, 25)},
    {'name': 'Stephanie Carter', 'birthday': datetime(1999, 5, 19)},
    {'name': 'Robin Gilbert', 'birthday': datetime(1969, 5, 24)},
    {'name': 'Jeffrey Hahn', 'birthday': datetime(1983, 5, 19)},
    {'name': 'Richard Mclean', 'birthday': datetime(1984, 5, 25)},
    {'name': 'Max Chang', 'birthday': datetime(1972, 5, 20)},
    {'name': 'Alan Sandoval', 'birthday': datetime(1997, 5, 22)},
    {'name': 'Chad Brown', 'birthday': datetime(1979, 5, 22)},
    {'name': 'Tina Faulkner', 'birthday': datetime(2000, 5, 30)},
    {'name': 'Michael Stanley', 'birthday': datetime(1998, 5, 25)},
    {'name': 'April Kaiser', 'birthday': datetime(2002, 5, 22)},
    {'name': 'Maria Phillips', 'birthday': datetime(1993, 5, 23)},
    {'name': 'Jeremy Gomez', 'birthday': datetime(1981, 5, 28)},
    {'name': 'Nicole Martin', 'birthday': datetime(1976, 5, 27)},
]

def get_birthdays_per_week(users: list) -> dict:
    date_offset = timedelta(days=1)
    current_date = datetime.now()
    greating_date = current_date
    greating_dict = defaultdict(list)
    
    # Handles case when the current day is Monday and we have to  
    # greet people who had birthdays on previous weekends
    if current_date.weekday() == 0:
        greating_date -= date_offset * 2.0
    
    for _ in range(SEVEN_DAYS):
        for person in users:
            for key, value in person.items():
                if key == 'birthday':
                    birthday = value
                    has_birthday = birthday.day == greating_date.day \
                                    and greating_date.month == greating_date.month
                    
                    if has_birthday:
                        if greating_date.weekday() != 5 and greating_date.weekday() != 6:
                            greating_dict[greating_date.strftime("%A")].append(person['name'])
                        # Handles case when Saturday is the last day of the SEVEN_DAYS interval and it's 
                        # birthdays included in Monday greetings of the current week
                        elif current_date.weekday() == 6 and greating_date.weekday() == 5:
                            continue
                        else:
                            greating_dict["Monday"].append(person['name'])
        
        greating_date += date_offset

    return greating_dict

def print_birthdays_per_week(birhday_dict: dict):
    for weekday, names in birhday_dict.items():
        print("{:<10}: {}".format(weekday, ", ".join(names)))

def main():
    birthdays_per_week = get_birthdays_per_week(users)
    print_birthdays_per_week(birthdays_per_week)
    

if __name__ == '__main__':
    main()











