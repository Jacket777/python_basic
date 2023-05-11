"线程共享全局变量存在问题"
import time
from threading import *

num = 0


def test01():
    global num
    for i in range(100000):
        num += 1
    print("test1 out: num: ", num)


def test02():
    global num
    for i in range(100000):
        num += 1
    print("test2 out: num: ", num)


if __name__ == '__main__':
    t1 = Thread(target=test01)
    t2 = Thread(target=test02)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
