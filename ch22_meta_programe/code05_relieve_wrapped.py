"""
解除装饰器
"""

import time
from functools import wraps


def time_use(func):
    """
    Decorator that reports the execution time.
    :param func
    :return
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'func name: {func.__name__}, time use:{end - start}')
        return result

    return wrapper


def decorator_1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Call decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator_2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Call decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator_1
@decorator_2
def add(x, y):
    return x + y


if __name__ == '__main__':
    print(f'add result = {add(3, 5)}')
    print(f'wrapped add result = {add.__wrapped(3, 5)}')
