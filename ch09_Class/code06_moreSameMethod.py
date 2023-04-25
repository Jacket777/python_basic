"""
测试方法没有重载,多个同名方法，只有最后一个有效
"""


class Person:
    def say_hi(self):
        print("hello")

    def say_hi(self, name):
        print("{0},hello".format(name))


if __name__ == '__main__':
    p1 = Person()
    # p1.say_hi() #会报错
    p1.say_hi("Jack")
