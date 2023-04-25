"""
测试多态
"""


class Man:
    def eat(self):
        print("hungry,eat")


class Chinese(Man):
    def eat(self):
        print("用中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print("英国人用刀叉吃饭")


class Indian(Man):
    def eat(self):
        print("印度人用手吃饭")


def manEat(m):
    if isinstance(m, Man):
        m.eat()
    else:
        print("不能吃饭")


if __name__ == '__main__':
    manEat(Chinese())
    manEat(English())
