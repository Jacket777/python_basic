"线程共享全局变量"
import time
from threading import *

num = 10
def test01():
    global num
    for i in range(3):
        num += 1
    print("test1 out: num: ",num)


def test02():
    global num
    print("test2 out: num: ",num)

if __name__ == '__main__':
    t1 = Thread(target=test01)
    t2 = Thread(target=test02)
    t1.start()
    t1.join()
    t2.start()
    t2.join()