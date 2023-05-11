"互斥锁"
import time
from threading import Thread, Lock

num = 0
mutex = Lock()


def test01():
    global num
    mutex.acquire()
    for i in range(100000):
        num += 1
    mutex.release()
    print("test01 out num: ", num)


def test02():
    global num
    mutex.acquire()
    for i in range(100000):
        num += 1
    mutex.release()
    print("test02 out num: ", num)


if __name__ == '__main__':
    t1 = Thread(target=test01)
    t2 = Thread(target=test02)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
