# 01 基础运算


def basicIntCalc():
    a = 5 + 9
    print(type(a), a)
    b = 22 - 6
    print(type(b), b)
    c = 12 * 14
    print(type(c), c)
    d = 22 / 7
    print(type(d), d)
    a = 3 // 2
    print(type(a), a)
    e = 2 ** 4
    print("指数操作", e)
    f = 25 % 7
    print(f)
    g = 1 + 2 * 3
    print(g)
    h = (1 + 2) * 3
    print(h)
    print("整型长度无限制")
    a = 22 ** 100
    print(a)


def floatCalc():
    a = 8.8 ** -5.4
    print(a)
    a = 2.3e02
    print(a)
    print(3.)
    print(3.0)
    print(.5)
    print(0.5)
    # 溢出
    # a = 500.0**10000
    # print(a) 不会打印
    a = 1 - 2 / 3
    print(a)


# 特殊类型--复数类型
def complexCalc():
    a = 1j
    b = a * a
    print(a)
    print(b)
    c = 3 + a
    print(c)


# String use
def useStr():
    a = 'Alice ' + 'Bob'
    print(a)
    b = "Hello " * 5
    print(b)


if __name__ == '__main__':
    # basicIntCalc()
    # floatCalc()
    # complexCalc()
    useStr()
