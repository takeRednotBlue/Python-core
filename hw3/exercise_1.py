"""
1. Напишіть функцію, яка буде приймати число і рекурсивно виводити число і відповідну кількість зірочок, поступово зменшуючи кількість на 2 (поки 
не дійдемо до нуля). Наприклад, якщо ввести 5, отримаємо такий результат
5 *****
3 ***
1 *

1*. Напишіть ту ж функцію, але використовуючи рекурсію.
"""

def number_and_stars(number):
    while number > 0:
        print(number, "*" * number)
        number -= 2

def with_recursion(number):
    if number == 0:
        return
    if number == 1:
        return print("1 *")
    else:
        print(number, "*"*number)
    with_recursion(number - 2)


number_and_stars(5)
with_recursion(51)
