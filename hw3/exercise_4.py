"""
4. Напишіть функцію гри, що буде загадувати число від 1 до 100, а Ви маєте його вгадати. Після кожного введення 
програма Вам може підказувати, чи загадане число більше чи менше введеного. Також можна рахувати і в кінці вивести 
кількість спроб, за яку користувач вгадав число. Підказка: використовуйте бібліотеку random (а саме метод randint)
4*. Аналогічно зробіь функцію гри, де Ви загадуєте число від 1 до 100 (вводячи його), а комп'ютер має його вгадати за 
10 спроб (без Ваших підказок). 
Простіший варіант: комп'ютер не пам'ятає, які числа він називав як варіанти до того (під час однієї гри). 
Використовуйте random.randint
Складніший варіант: комп'ютер пам'ятає, що він пробував вгадати до того, і не пробує повторюватися, коли вгадує число. 
Використовуйте random.sample
"""

from random import randint, sample
def main():
    number_to_guess = randint(1, 101)
    is_working = True
    count = 0

    while is_working:
        guess = int(input("Enter your number: "))
        count += 1
        if guess > number_to_guess:
            print("Your number is greater than mine. Try again.")
        elif guess < number_to_guess:
            print("Your number is less than mine. Try again.")
        else:
            print(f"You won! The number is {guess} and you guessed it from {count} try.")
            is_working = False

def sub_main():
    user_number = int(input("Enter your number: "))
    number_of_guesses =  10
    numbers_range = [i for i in range(1, 101)]
    computer_guess = sample(numbers_range, number_of_guesses)
    for num in computer_guess:
        print(f"I guess your number is: {num}")
        confirmation = input("Is the number correct? Enter 'yes' or 'no': ")
        if confirmation == "yes" or confirmation == "y":
            print("I've never had any doubt about my superiority")
            return
        else:
            continue
    print("You won! Computer exceeded given number of guesses.")
sub_main()
        