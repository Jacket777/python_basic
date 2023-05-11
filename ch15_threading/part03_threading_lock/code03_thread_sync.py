"线程同步应用"
import time
from threading import Thread,Lock
import threading

lock01 = Lock()
lock02 = Lock()
lock03 = Lock()

lock02.acquire()
lock03.acquire()

class Task01(Thread):
    def run(self):
        while True:
            if lock01.acquire():
                print("....task01.....")
                time.sleep(1)
                lock02.release()



class Task02(Thread):
    def run(self):
        while True:
            if lock02.acquire():
                print("....task02.....")
                time.sleep(1)
                lock03.release()


class Task03(Thread):
    def run(self):
        while True:
            if lock03.acquire():
                print("....task02.....")
                time.sleep(1)
                lock01.release()


if __name__ == '__main__':
    t1 = Task01()
    t2 = Task02()
    t3 = Task03()
    t1.start()
    t2.start()
    t3.start()