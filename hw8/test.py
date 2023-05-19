from datetime import datetime, timedelta
import random
from faker import Faker # installed in venv

# sublist = [item[i] if i < len(item) else None for item in data.values()]

def create_user_bithday_dict():
    # Create an instance of the Faker class
    faker = Faker()

    # Define the date range for birthdays
    start_date = datetime(2023, 5, 18)
    end_date = datetime(2023, 5, 31)

    # Generate a list of 15 colleagues with random names and birthdays
    colleagues = []
    for i in range(15):
        # Generate a random name
        name = faker.name()

        # Generate a random birthday within the specified date range
        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        
        # Create a dictionary with the colleague's name and birthday
        colleague = {
            "name": name,
            "birthday": random_date
        }
        
        # Append the colleague dictionary to the list
        colleagues.append(colleague)

    # Print the list of colleagues
    for colleague in colleagues:
        print(colleague)

dt = datetime.now()
delta = timedelta(days=1)

print(delta * 2.0)