"""
类专有方法
__del__ 析构函数
"""

class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("del object {0}: ".format(self.name))


if __name__ == '__main__':
    p1 = Person("p1")
    p2 = Person("p2")

    del p2
    print("end.........")
