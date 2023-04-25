"""
测试异常调用机制
"""


# coding=utf-8

def a():
    num = 1 / 0


def b():
    a()


def c():
    b()


def f01():
    print("step 0")
    try:
        print("step 01")
        a = 3 / 0
        print("step 02")
    except BaseException as e:
        print("发生异常，0不能做除数")
        print(e)
        print((type(e)))

    print("end !!!!")


if __name__ == '__main__':
    c()
