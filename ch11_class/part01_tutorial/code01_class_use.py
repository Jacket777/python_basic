# code01: class简单使用

# 1.类定义与简单使用
class MyTest:
    """A simple example class"""
    i = 12345  # 类似于Java中静态变量

    def fun(self):
        return 'hellow world'

# 2.类对象使用
def class_use():
    print(MyTest.i)
    myTest = MyTest()
    x = MyTest.fun
    print(x(myTest))
    print(MyTest.__doc__)


# 2.类初始化
class Complex:
    def __init__(self, real_part, image_part):
        self.real_part = real_part
        self.image_part = image_part


def init_use():
    x = Complex(3.0, -4.5)
    print(x.real_part, x.image_part)


# 3. 类的数据属性类似于Java中实例变量，不需要声明【不同点】
def counter_use():
    x = MyTest()
    x.counter = 1
    while x.counter < 10:
        x.counter = x.counter * 2
    print(x.counter)
    del x.counter  # 删除该属性


# 4. 方法对象的使用
def method_object():
    x = MyTest()
    xf = x.fun
    for i in range(3):
        print(xf())


# 5. 类函数特殊用法
def min_fun(self, x, y):
    return min(x, x + y)


class C:
    f = min_fun

    def hello(self):
        return 'hello world'

    h = hello


def method_use():
    x = C()
    result = x.f(2, 3)
    print(result)
    print(x.h())


if __name__ == '__main__':
    # init_use()
    # counter_use()
    # method_object()
    method_use()



