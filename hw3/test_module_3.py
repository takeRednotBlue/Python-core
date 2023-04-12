# def choose_message(name, hello=True):
#     def say_hello():
#         return f"Hello {name}"

#     def say_bye():
#         return f"Bye {name}"

#     if hello:
#         return say_hello
#     else:
#         return say_bye

# name = "Max" #input()

# hi = choose_message(name)
# print(hi())
# bye = choose_message(name, hello=False)
# print(bye())

from my_module import get_name


def check(name):
    return f"Wait a minute... {get_name(name)}, right?"


print(check("Max"))


def func(my_string):
    result = {}
    for symbol in my_string:
        if symbol not in result:
            result[symbol] = 1
        else:
            result[symbol] += 1
    return result


print(func("Hello worl!"))

sorted()
            
