"为线程传递参数"
import _thread
import time


def fun1(threadName, delay):
    print("thread {0} begin run fun1".format(threadName))
    time.sleep(delay)
    print("thread {0} begin run fun1 end".format(threadName))


def fun2(threadName, delay):
    print("thread {0} begin run fun2".format(threadName))
    time.sleep(delay)
    print("thread {0} begin run fun2 end".format(threadName))


if __name__ == '__main__':
    print("begin to run")
    _thread.start_new(fun1, ("thread -1", 4))
    _thread.start_new(fun2, ("thread -2", 2))
    time.sleep(6)
