"""
3. Напишіть функцію, яка може приймати різну кількість (або не приймати) секунд, хвилин, годин, днів і тижнів і буде 
вертати загальну кількість секунд. Використовуйте ключові параметри, щоб не запам'ятовувати порядок вказання аргументів.
"""
from datetime import datetime, timedelta



def amount_of_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
    sum = seconds + minutes*60 + hours*60*60 + days*24*60*60 + weeks*7*24*60*60
    return sum


print(amount_of_seconds(minutes=2, hours=1))
