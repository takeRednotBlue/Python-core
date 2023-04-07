"""
7. У змаганні з програмування беруть участь синя та червона команди програмістів. Команда, що переможе, отримує 
торт! Єдина складність полягає в тому, що в обох командах різна кількість учасників, але організаторам треба на початку 
розрізати торт таким чином, щоб, незалежно від того, яка команда виграє, кожен учасник отримав би цілу кількість 
шматочків торта, але при цьому щоб шматочків не було забагато (бо будуть занадто дрібними і буде незручно їсти). 
Наприклад, якщо в синій команді 2 людей, а в червоній - 8, торт треба розрізати на 8 шматочків. Якщо в синій команді 4 
людини, а в червоній - 6, торт треба розрізати на 12 шматочків. Якщо в синій команді 5 людей, а в червоній - 6, торт 
треба розрізати на 30 шматочків. Нехай користувач введе кількість учасників для обох команд і доможіть організаторам 
знайти необхідну кількість шматочків торта. 
Підказка: пошукайте в Інтернеті, що таке НСК (найменше спільне кратне) і подумайте, як би в реальному житті без 
програмування Ви би вирішили таку проблему. Використовуйте if/else/while/break


"""

is_working = True

# function which returns least common  multiple 
def lcm(a, b):
    # gcd - greatest common divisor 
    gcd = a if a < b else b 
    global is_working
    while is_working:
        if not a % gcd and not b % gcd:
            break
        gcd -= 1
    # lmc formula is |ab|/gcd(a, b)
    return abs(a * b) / gcd


while is_working:
    red_team_members = input("Enter red team members number: ")
    blue_team_members = input("Enter blue team members number: ")
    try:
        red_team_members = int(red_team_members)
        blue_team_members = int(blue_team_members)
    except ValueError:
        print("One of the number or both are not an integer. Try again.")
    else:
        break
    
amount_of_pieces = lcm(red_team_members, blue_team_members)

print(f"You should divide cake into {amount_of_pieces} pieces.")



    

