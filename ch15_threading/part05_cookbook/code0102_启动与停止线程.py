
import time
from threading import Thread


class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)


c = CountDownTask()
t = Thread(target=c.run, args=(10,))
t.start()
c.terminate()  # Signal termination
t.join()   # Wait for actual termination (if needed)
print("=====end=====")

