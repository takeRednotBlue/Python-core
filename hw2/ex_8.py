"""
8. Нехай користувач введе якусь стрічку, яка може містити різні типи дужок - (), {}, [] (вони можуть бути вкладеними 
одні в одних). Спробуйте знайти відповідь на питання, чи кількість відкриваючих дужок дорівнює кількості закриваючих 
дужок.
Завдання з зірочкою: Крім перевірки кількості, також перевірте, чи вони відкриваються і закриваються правильно. 
Наприклад, "({[]})" це правильно, а "({[}])" - ні (тому що фігурні дужки закрилися, але квадратна дужка всередині них 
лишилася відкритою).
"""

from collections import Counter
# Hello (my{friend } just ) testing my [ progra].
test_string = input("Enter string with parentheses, brackets and braces: ")

open_list = ["(", "{", "["]
close_list = [")", "}", "]"]
stack = []
items_list = []

for char in test_string:
    if char in close_list or char in open_list:
        items_list.append(char)
    if char in open_list:
        stack.append(char)
    elif char in close_list:
        pos = close_list.index(char)
        if len(stack) > 0 and open_list[pos] == stack[len(stack) - 1]:
            stack.pop()
count = {i:items_list.count(i) for i in items_list}

if not items_list:
    print("There is no parentheses, brackets or braces.")
elif len(stack) == 0:
    print(f"Everything is closed - {''.join(items_list)}")
else:
    print(f"Somewhere is mistake - {''.join(items_list)}")


print(f"Count of parantheses {count}")
    
