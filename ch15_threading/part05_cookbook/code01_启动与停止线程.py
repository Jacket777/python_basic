# Code to execute in an independent thread
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print("T-minus: {}".format(n))
        n -= 1
        time.sleep(10)



if __name__ == '__main__':
    # 1. create a thread
    t = Thread(target=countdown, args=(10,))
    # t = Thread(target=countdown, args=(10,), daemon=True) # 将当前线程设置为后台线程，后台线程会在主线终止时自动销毁
    # 2 start a thread
    t.start()
    # 3 thread state
    # while True:
    #     if t.is_alive():
    #         print("Still running\n")
    #         time.sleep(3)
    #     else:
    #         print('Completed\n')
    #         break
    #t.join()



