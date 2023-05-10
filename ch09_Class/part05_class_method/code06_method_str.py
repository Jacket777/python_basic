"""
测试重写object的__str()__方法
类似于Java的 toString方法
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "名字是{0}".format(self.name)


if __name__ == '__main__':
    p = Person("Jack")
    print(p)
