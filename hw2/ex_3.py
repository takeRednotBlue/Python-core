"""
3. Напишіть програму, яка "кривляється" з користувача (повторює все, що користувач вводить). Програма має завершитися 
тільки тоді, коли користувач введе "stop". 
Підказка: використовуйте while та break
"""

is_working = True

while is_working:
    text = input()
    if "stop" in text:
        break
    print(text)
    