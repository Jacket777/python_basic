'''
使用单独进程执行
'''

import time
import multiprocessing

class CountDownTask:
    def __init__(self,n):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(5)



c = CountDownTask(5)
p = multiprocessing.Process(target=c.run())
p.start()