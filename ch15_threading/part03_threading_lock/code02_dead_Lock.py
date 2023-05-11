"dead lock"
from threading import Thread,Lock
import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()

class MyThread01(Thread):
    def run(self):
        if mutexA.acquire():
            print(self.name,'execute')
            time.sleep(1)
            if mutexB.acquire():
                print(self.name,"execute")
                mutexB.release()
            mutexA.release()

class MyThread02(Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name,'execute')
            time.sleep(1)
            if mutexA.acquire():
                print(self.name,"execute")
                mutexA.release()
            mutexB.release()

if __name__ == '__main__':
    t1 = MyThread01()
    t2 = MyThread02()
    t1.start()
    t2.start()