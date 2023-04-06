"""
1. Напишіть алгоритм, який приймає введене користувачем число (як int) і, за допомогою операторів % (остача від
ділення), / (ділення) і // (цілочисельне ділення) збережіть і виведіть на екран значення змінної (стрічку), яка 
виглядає, як введене число, але задом наперед
Підказка: число % 10 поверне вам останню цифру цього числа, число // 10 вертає вам число без останньої цифри. 
Використовуйте цикл while. Проходячись по циклу, щоразу діставайте останню цифру і додавайте її як стрічку до змінної 
результату.
"""

result = ""
digit = 0
enter_number = True
while enter_number:
    num = input("Enter your number: ") # Enter 3 digit numbe
    try:
        num = int(num)
        break
    except ValueError as err:
        print(f"{err}. '{num}' is not a number. Try again.")
    
while True:
    if len(str(num)) == 1:
        result += str(num)
        break
    digit = num % 10
    result += str(digit)
    num //= 10

print(result)

