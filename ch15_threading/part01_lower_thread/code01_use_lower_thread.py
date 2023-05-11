"使用_thread模块创建线程"
import _thread
import time

def fun01():
    print("begin run fun01")
    time.sleep(4)
    print("fun01 end")

def fun02():
    print("begin run fun02")
    time.sleep(4)
    print("fun02 end")


if __name__ == '__main__':
    print("begin to run")
    _thread.start_new(fun01,())
    _thread.start_new(fun02,())
    time.sleep(6)

