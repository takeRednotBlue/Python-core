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
    {'name': 'Gary Wright', 'greating_date': datetime(2023, 5, 28)},
    {'name': 'Christopher Stephens', 'greating_date': datetime(2023, 5, 18)},
    {'name': 'Regina Martinez', 'greating_date': datetime(2023, 5, 27)},
    {'name': 'Julie Carroll', 'greating_date': datetime(2023, 5, 24)},
    {'name': 'Justin Anderson', 'greating_date': datetime(2023, 5, 21)},
    {'name': 'Kayla Johnson', 'greating_date': datetime(2023, 5, 28)},
    {'name': 'Stephanie Hill', 'greating_date': datetime(2023, 5, 31)},
    {'name': 'Zachary Young', 'greating_date': datetime(2023, 5, 30)},
    {'name': 'David Rowe', 'greating_date': datetime(2023, 5, 29)},
    {'name': 'Ruben Carlson', 'greating_date': datetime(2023, 5, 24)},
    {'name': 'Jason Pennington', 'greating_date': datetime(2023, 5, 25)},
    {'name': 'Betty Hill', 'greating_date': datetime(2023, 5, 30)},
    {'name': 'Lisa Payne', 'greating_date': datetime(2023, 5, 23)},
    {'name': 'Kathleen Allison', 'greating_date': datetime(2023, 5, 22)},
    {'name': 'Cheryl Shepard', 'greating_date': datetime(2023, 5, 25)},
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
    for day, names in birhday_dict.items():
        print("{:<10}: {}".format(day, ", ".join(names)))

def main():
    birthdays_per_week = get_birthdays_per_week(users)
    print_birthdays_per_week(birthdays_per_week)
    

if __name__ == '__main__':
    main()











