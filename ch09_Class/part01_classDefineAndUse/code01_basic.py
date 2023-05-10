"""
类的定义与使用
"""


class MyClass(object):
    i = 123

    def f(self):
        return 'hello world'


if __name__ == '__main__':
    use_class = MyClass()
    print(f'调用类的属性:{use_class.i}')
    print(f'调用类的方法:{use_class.f()}')
