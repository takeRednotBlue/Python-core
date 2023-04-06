"""
4. Напишіть програму "fizzbuzz". Логіка програми-гри наступна: Користувач вводить ціле число. Якщо воно ділиться націло 
на 3, програма має вивести "fizz". Якщо воно ділиться націло на 5, програма має вивести "buzz". Якщо воно ділиться 
націло і на 3, і на 5, програма має вивести "fizzbuzz". В інших випадках виведіть якесь повідомлення за замовчуванням. 
Підказка: використовуйте if/elif/else
"""

num = int(input("Enter your number: "))
if not num % 3 and not num % 5:
    print("fizzbuzz")
elif not num % 3:
    print("fizz")
elif not num % 5:
    print("buzz")
else:
    print("Bad luck, sorry")