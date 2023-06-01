
from time import time_ns, sleep


def operation_speed_measure(func):
    def wrapper(*args, **kwargs):
        start = time_ns()
        result = func(*args, **kwargs)
        end = time_ns()
        speed = end - start
        # print('It took {speed} nanoseconds to perform operation.')
        return result, speed
    return wrapper


def factorial_with_cache():
    cache = {}
    @operation_speed_measure
    def calc(n):
        if n < 0:
            raise ValueError("Number must not be negative")

        result = 1 
        for val in range(1, n +1 ):
            if val in cache:
                result = cache[val]
            else:
                result = val * cache.get(val-1, 1)
                cache[val] = result
                # print(f'{val} was not in cache - {result}')
        return result
    return calc

factorial = factorial_with_cache()
factorial2 = factorial_with_cache()

# print('Output - time {1} ns'.format(*factorial(100000)))
# print('='*30)
# # # factorial(10)
# print('Output - time {1} ns'.format(*factorial(50000)))
# # factorial(7)
# print('='*30)
# print('Output - time {1} ns'.format(*factorial2(50000)))
# print('='*30)
# print('Output {} - time {} ns'.format(*factorial(6)))


