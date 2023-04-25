"""
函数装饰器
"""

import time
from functools import wraps


"""
函数装饰器--接收一个函数作为参数并返回一个新函数
"""
def time_use(func):
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
    while n > 0:
        n -= 1






def count_down2(n):
    while n > 0:
        n -= 1

"""
装饰器第二种用法
"""
count_down2 = time_use(count_down2)


if __name__ == '__main__':
    count_down(1000000)
    count_down2(1000000)


