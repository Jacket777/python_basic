"为线程传递参数"
import threading
import time

def fun1(threadName,delay):
    print("thread {0} begin run fun1".format(threadName))
    time.sleep(delay)
    print("thread {0} begin run fun1 end".format(threadName))


def fun2(threadName,delay):
    print("thread {0} begin run fun2".format(threadName))
    time.sleep(delay)
    print("thread {0} begin run fun2 end".format(threadName))

if __name__ == '__main__':
    print("begin to run")
    t1 = threading.Thread(target=fun1,args = ("thread -1",  4))
    t2 = threading.Thread(target=fun2,args = ("thread -2", 2))
    t1.start()
    t2.start()
