"""
偏函数的使用 python 2.5 开始引入
"""
from functools import partial


def mode_partial(n, m):
    return n % m

"""
后面的参数可以写，也可以不写，但应该依次填写
"""
mode_by_100 = partial(mode_partial, 100)
mode_by = partial(mode_partial)

if __name__ == '__main__':
    print(f'自定义函数, 100对7取余结果为: {mode_partial(100, 7)}')
    print(f'调用偏函数100对7取余结果为: {mode_by_100(7)}')
    print(f'调用偏函数100对7取余结果为: {mode_by(100,7)}')