import re
from datetime import datetime




def date_transformation(date: str):

        date_mapping = {
                r'\d{2}\.\d{2}\.\d{4}': '%d.%m.%Y',
                r'\d{2}/\d{2}/\d{4}': '%d/%m/%Y',
                r'\d{2}\.\d{2}\.\d{2}': '%d.%m.%y',
                r'\d{2}/\d{2}/\d{2}': '%d/%m/%y',
                r'\d{4}-\d{2}-\d{2}': '%Y-%m-%d',
        }

        for pattern, format in date_mapping.items():
            if re.match(pattern, date):
                birthday = datetime.strptime(date, format)
                return birthday
        else:
             raise ValueError('Invalid data format.')
"""12.03.2023
    12.03.20
    12-03-2023
    2023-03-12
    12/03/2023
    
    """

test1 = date_transformation('12.03.2023')
test2 = date_transformation('12/14/2023')
test3 = date_transformation('12.03.23')
test4 = date_transformation('12/03/23')
test5 = date_transformation('2023-03-12')

assert type(test1) == datetime
assert type(test2) == datetime
assert type(test3) == datetime
assert type(test4) == datetime
assert type(test5) == datetime


print('Everything is OK!')

