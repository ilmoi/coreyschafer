# def bark(n):
#     print('bark '*n)
#
# def doublebark(n, level):
#     print(f'wow this dog is really..{level}')
#     print('barketzybark '*n)
#
# bark(3)
#
# def decorator(func):
#
#     def wrapper_decorator(*args, **kwargs):
#         print('do something BEFORE')
#         value = func(*args, **kwargs)
#         print('do something AFTER')
#         return value
#
#     return wrapper_decorator
#
# # print('-'*50)
# #
# # bark = decorator(bark)
# # bark(50)
# #
# # print('-'*50)
# #
# # doublebark = decorator(doublebark)
# # doublebark(50, 'loud')
#
# print('-'*50)
#
# @decorator
# def bark(n):
#     print('bark '*n)
#
# bark(30)

import time
import logging
from functools import wraps


def logger(func):
    logging.basicConfig(filename='{}.log'.format(func.__name__), level='DEBUG')

    @wraps(func)  # this is needed in order to preserve original function name in double wrapping
    def logger_wrapper(*args, **kwargs):
        logging.info(
            f'Our function {func.__name__} ran with arg {args} and kwargs {kwargs}'
        )
        print('logging succeeded')
        return func(*args, **kwargs)

    return logger_wrapper


def timer(func):

    @wraps(func)  # this is needed in order to preserve original function name in double wrapping
    def timer_wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'our function {func.__name__} ran in {t2-t1}')
        return result

    return timer_wrapper


# timer(logger(add_two_together))
# the lower ones on the stack get executed first
@timer
@logger
def add_two_together(x, y):
    time.sleep(1)
    return(x+y)


add_two_together(3, 1)


# if you ever wanted to add more prefixes
def prefix(prefix):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print(prefix, 'statement before function called')
            result = func(*args, **kwargs)
            print(prefix, 'statement after function called')
            return result

        return wrapper

    return decorator


@prefix('LOG:')
def addition(x, y):
    return x+y


z = addition(1, 2)
print(z)
