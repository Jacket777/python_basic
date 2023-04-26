# 匿名函数
# lambda表达式 创建匿名函数
# lambda [arg1, [, arg2,...argn]]: expression
f = lambda a, b, c, d: a * b * c * d


def test01(a, b, c, d):
    print("======")
    return a * b * c * d


g = [lambda a: a * 2, lambda b: b * 3]

h = [test01, test01]  # 函数也是对象

if __name__ == '__main__':
    print(f(2, 3, 4, 5))
    print(g[0](6))  # 给第一个函数中传递参数值为6
    print(g[1](3))  # 给第一个函数中传递参数值为6
    print(g[0](6) + g[1](3))
    print(h[0](3, 4, 5, 6))
