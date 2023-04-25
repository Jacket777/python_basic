"""
测试组合
"""


# 使用继承实现代码的复用
class A1:
    def say_a1(self):
        print("a1,a1,a1")


class B1(A1):
    pass


b1 = B1()
b1.say_a1()


# 使用组合进行代码的复用
class A2:
    def say_a2(self):
        print("a2,a2,a2")


class B2:
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    b1 = B1()
    b1.say_a1()
    a2 = A2()
    b2 = B2(a2)
    b2.a.say_a2()
