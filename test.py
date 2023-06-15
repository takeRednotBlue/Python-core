from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    # def make_sound(self):
    #     print("Woof!")

    def voice(self):
        print('Woof!')
    pass

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()

# dog.make_sound()