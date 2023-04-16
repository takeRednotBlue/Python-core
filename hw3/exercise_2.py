"""
2. Напишіть функцію, що приймає два числа і вертає перше число в степені другого (без використання вбудованого 
функціоналу, але можна використовувати множення)
2*. Напишіть ту ж функцію, але використовуючи рекурсію.
"""

def exponentiation(num, power):
    result = num
    while power > 1:
        result *= num
        power -= 1
    return result

def recursive_exp(num, power):
    if power == 1:
        return num
    return num * recursive_exp(num, power - 1)


power = 12
print(exponentiation(2, power))
print(2**power)
print(recursive_exp(2, power))
