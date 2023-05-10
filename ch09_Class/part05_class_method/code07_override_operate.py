"""
测试运算符重载
"""


class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return "{0}--{1}".format(self.name, other.name)
        else:
            return "不是同类对象不是相加"

    def __mul__(self, other):
        if isinstance(other, int):
            return self.name * other
        else:
            return "不是同类对象不是相加"


if __name__ == '__main__':
    p1 = Person("Jack")
    p2 = Person("Tom")

    x = p1 + p2
    print(x)

    print(p1 * 3)
