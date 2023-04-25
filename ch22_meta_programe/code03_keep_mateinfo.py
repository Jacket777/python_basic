"""
装饰器中保留函数的元信息
"""

import time
from functools import wraps
from inspect import signature


"""
函数装饰器--接收一个函数作为参数并返回一个新函数
"""
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
def count_down(n):
    """
    Count down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1






if __name__ == '__main__':
    count_down(1000000)
    print(f'func name: {count_down.__name__}')
    print(f'func doc: {count_down.__doc__}')
    print(f'func annotations:  {count_down.__annotations__}')
    print(f'wrapped:{count_down.__wrapped__(10000)}')
    print(f'signature: {signature(count_down)}')  # 参数签名信息





