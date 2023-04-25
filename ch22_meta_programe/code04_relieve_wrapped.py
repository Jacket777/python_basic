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
        start= time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'func name: {func.__name__}, time use:{end - start}')
        return result
    return wrapper


@time_use
def add(x, y):
    return x + y





if __name__ == '__main__':
    orig_add = add.__wrapped__
    print(f'add result: {orig_add(3,5)}')

