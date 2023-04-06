"""
5. Дозвольте користувачу вводити цілі числа по черзі. Якщо введене число менше 10, пропустіть його і нічого не робіть. 
Якщо воно більше 100, зупиніть введення чисел і програму. В інших випадках виводьте число на екран. Підказка: 
використовуйте if/elif/else/break/continue 
"""

is_working = True

while is_working:
    num = input("Enter integer number: ")
    try:
        num = int(num)
    except ValueError:
        print(f"{num} invalid number. Try again.")
        continue

    if num < 10:
        continue
    elif num > 100:
        break
    
    print(f"Your number {num}")

