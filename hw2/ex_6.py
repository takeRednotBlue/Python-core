"""
6. нехай користувач введе два числа - a i b, при цьому a має бути менше b. Виведіть середнє арифметичне чисел з 
відрізку [a;b], але тільки тих, що діляться націло на 3. 
Підказка: зверніть увагу, що відрізок [a;b] включає в себе і a, i b. Щоб знайти середнє арифметичне чисел, Ви маєте 
їхню суму поділити на їхню кількість.
"""

print("Enter 2 numbers where first greater than second.")

is_working = True

while is_working:
    a = input("Enter smaler number: ")
    b = input("Enter greater number: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print(f"'{a}' and '{b}' are not numbers. Try again.")
    else:
        if a < b:
            break
        elif a == b:
            print(f"{a} is equal to {b}. Try again.")
        else:
            print(f"{a} is greater than {b}. Try again.")

count = 0
sum = 0
l = []


for i in range(a, b + 1):
    if not i % 3:
        sum += i
        count += 1
        l.append(i)
if count > 0:
    aver = sum / count
else:
    print("The is no numbers which match the requriments.")

print(f"Avarage sum of required number is {aver}.")
print(f"There is {count} numbers in the given list1: {l}")
