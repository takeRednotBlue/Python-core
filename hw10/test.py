# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        return 'I\'m smart being and want respect.'
    
    def get_info(self):
        # self.say()
        return self.say() + f'My name is {self.nickname} and I weigh {self.weight} kilogram.' 

    def change_weight(self, weight):
        self.weight = weight

class Breed:
    def __init__(self, habitat, color):
        self.habitat = habitat
        self.color = color
    
    def say(self):
        return f'Wild is my motherland.'




class Owner:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
        
      
    def info(self):
        info_dict = {
            'name': self.name,
            'age': self.age,
            'adress': self.adress,
        }
        return info_dict
    

class Cat(Animal, Breed):
    def __init__(self, nickname, weight, breed, owner, country='Ukraine'):
        self.breed = breed
        self.owner = owner
        self.country = country
        super().__init__(nickname, weight)

    # def say(self):
    #     return "Meow"

    def get_country(self):
        return self.country

    def say(self):
        return 'Meow motherfucker!'

    def who_is_owner(self):
        return self.owner.info()

        
Maxym = Owner('Maxym', 26, 'Berdychev')
cat = Cat('Luna', 4, 'scotish', Maxym, 'USA')

# print(cat.who_is_owner())
print(cat.get_info())

# print(cat.weight)
# Animal.change_weight(cat, 5)
# print(cat.weight)

# print(Animal.say(Cat))

# print(isinstance(cat, Animal))
