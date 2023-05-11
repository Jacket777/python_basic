"继承threading.Thread类创建线程"
import threading
import time

def fun01(delay):
    print("thread {0} begin run fun01".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("thread {0} end  run fun01".format(threading.current_thread().getName()))

def fun02(delay):
    print("thread {0} begin run fun02".format(threading.current_thread().getName()))
    time.sleep(delay)
    print("thread {0} end  run fun02".format(threading.current_thread().getName()))



class MyThread(threading.Thread):
    def __init__(self,funcName,threadName,funArgs):
        super().__init__(target=funcName,name=threadName,args=funArgs)

    def run(self):
        self._target(*self._args)


if __name__ == '__main__':
    print("begin to run")
    t1 = MyThread(fun01,'thread-1',(2,))
    t2 = MyThread(fun02,'thread-2',(4,))
    t1.start()
    t2.start()

