"""
event
"""
import threading
from threading import Thread, Event
import time

def countdown(n, started_evt):
    print("countdown starting")
    started_evt.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)


class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        """Run the timer and notify waiting threads after each interval"""
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
        pass





if __name__ == '__main__':
    started_evt = Event()
    print("Launching countdown")
    t = Thread(target=countdown, args=(10, started_evt))
    t.start()
    started_evt.wait()
    print('countdown is running')
