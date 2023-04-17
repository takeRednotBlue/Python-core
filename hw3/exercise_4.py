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

def starred_main():
    number_of_guesses =  10
    numbers_range = [i for i in range(1, 101)]
    computer_guess = sample(numbers_range, number_of_guesses)
    is_working = True
            
    while True:
        user_number = input("Enter your number (1-100): ")        
        try:
            user_number = int(user_number)
            if 1 <= user_number < 100:
                break
            else:
                print("Your number not in range from 1 to 100.")
        except ValueError:
            print(f"Your must enter only number in range from 1 to 100. Try again.")


    while is_working:
        for num in computer_guess:
            print(f"I guess your number is: {num}")        
            while True:                
                confirmation = input("Is the number correct? Enter 'yes' or 'no': ")
                if confirmation.lower().startswith("y") and confirmation.lower().startswith("n"):
                    break
                else:
                    print("Invalid answer. Try again.")  

            if confirmation.lower().startswith("y") and num == user_number:
                print("I've never had any doubt about my superiority")
                is_working = False
            elif confirmation.lower().startswith("n") and num == user_number:
                print("You cannot foul me, I'm not an idiot. My superiority is undisputable!")
                is_working = False
            elif confirmation.lower().startswith("y") and num != user_number:
                print("There is no need in flattery. Anyway I'm better and you know it.")
                continue

        is_working = False            
        print("You won! Computer exceeded given number of guesses.")

        
starred_main()
        