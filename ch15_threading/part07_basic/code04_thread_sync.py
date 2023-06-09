"""
线程同步
"""
import threading
from time import sleep
from datetime import datetime

date_time_format = '%y-%M-%d %H:%M:%S'

class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print(f"开启锁： {self.name}")
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name,self.counter,3)
        threadLock.release()

def date_time_str(date_time):
        return datetime.strftime(date_time,date_time_format)

def print_time(threadName,delay,counter):
    while counter:
        sleep(delay)
        print(f"{threadName}: {date_time_str(datetime.now())}")
        counter-=1



def main():
    thread1 = MyThread(1,"Thread-1",1)
    thread2 = MyThread(2,"Thread-2",2)

    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)

    for t in threads:
        t.join()
    print("退出主线程")

if __name__ == '__main__':
    threadLock =threading.Lock()
    threads = []
    main()

