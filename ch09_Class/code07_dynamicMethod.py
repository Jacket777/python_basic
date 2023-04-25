"""
测试方法的动态性
"""


class Person:
    def work(self):
        print("work hard")


def play_game(s):
    print("{0}在玩游戏".format(s))


def work2(s):
    print("work hard======")


if __name__ == '__main__':
    Person.play = play_game;
    p = Person()
    p.work()
    p.play()

    Person.work = work2
    p.work()
