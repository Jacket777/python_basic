"""
star and stop thread
"""
import multiprocessing
import time
from threading import Thread

def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


def sample_01():
    t = Thread(target=countdown, args=(3,))
    t.start()
    time.sleep(2)
    if t.is_alive():
        print("Still running")
    else:
        print('completed')
    print("the end of function")


def sample_02():
    t = Thread(target=countdown, args=(3,))
    t.start()
    time.sleep(2)
    if t.is_alive():
        print("Still running")
    else:
        print('completed')
    print("=====>>主体方法进入休眠===========")
    time.sleep(50)
    if t.is_alive():
        print("Still running")
    else:
        print("completed")


def sample_03():
    t = Thread(target=countdown, args=(10,), daemon=True)
    t.start()


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(5)


def sample_04():
    c = CountdownTask()
    t = Thread(target=c.run, args=(10,))
    t.start()
    print("send signal termination")
    c.terminate()
    print("after send signal termination")
    t.join()




class IOTask:
    """socket"""
    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)


class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print("T-minus", self.n)
            self.n -= 1
            time.sleep(5)


def sample_05():
    c = CountdownThread(5)
    # c.start()
    p = multiprocessing.Process(target=c.run)
    p.start()
    # time.sleep(100)




if __name__ == '__main__':
    c = CountdownThread(5)
    # c.start()
    p = multiprocessing.Process(target=c.run)
    p.start()


