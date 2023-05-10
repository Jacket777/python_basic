# 03 类型转换与数学模块使用
import math


# 数学模块使用
def math_fun():
    a = math.pow(10, 2)
    print(a)
    result = math.sqrt(5)
    print(result)
    print(math.sqrt(2) * math.tan(22))
    print(math.log(25 + 5))
    print(math.sqrt(4) * math.sqrt(10 * 10))
    print(math.tanh.__doc__)
    print(bin.__doc__)
    print(bin(25))


# 类型转换场景
def type_change():
    a = float(3)
    print(type(a))
    a = float('3.2')
    print(type(a))
    a = float('3')
    print(type(a))

    b = str(85)
    print(b, type(b))
    b = str(-9.78)
    print(b, type(b))

    c = int(8.64)
    print(c)
    c = round(8.64)
    print(c)
    c = round(8.5)
    print(c)

    d = int('5')
    print(d)
    d = float('5.1')
    print(d)


# math模块为浮点运算提供了对底层c函数库的访问
def math_float():
    result = math.cos(math.pi / 4.0)
    print(result)
    log_result = math.log(1024, 2)
    print(log_result)


if __name__ == '__main__':
    # math_fun()
    # type_change()
    math_float()

