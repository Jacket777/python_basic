"""
类的构造方法
Note: 一个类中可以定义多个构造方法，但以最后一个方法为真正实例化方法
"""


class MyClass(object):
    i = 123

    def __init__(self, name):
        self.name = name

    def f(self):
        return 'hello, ' + self.name


class DefaultInit(object):
    def __init__(self):
        print('类实例化时执行，我是init方法')

    def show(self):
        print('我是类中定义的方法，需要通过实例化对象调用')


class DefaultInit2(object):
    def __init__(self):
        print('我是不带参数的init方法')


class DefaultInit3(object):
    def __init__(self):
        print('我是不带参数的init方法')

    def __init__(self, param):
        print(f'我是带参数的init方法，参数值为:{param}')


class DefaultInit4(object):
    def __init__(self, param):
        print(f'我是带参数的init方法，参数值为: {param}')

    def __init__(self):
        print('我是不带参数的init方法4')


if __name__ == '__main__':
    # use_class = MyClass('xiao ming')
    # print(f'调用类的属性: {use_class.i}')
    # print(f'调用类的方法:{use_class.f()}')
    # test = DefaultInit()
    # print("实例化结束")
    # test.show()
    test2 = DefaultInit2()
    #test3 = DefaultInit3('abc')
    # test4 = DefaultInit4()
