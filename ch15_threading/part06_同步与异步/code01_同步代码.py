"""
同步代码
"""
import time


def hello():
    time.sleep(1)


def run():
    for i in range(5):
        hello()
        print("Hello world %s" % time.time())


if __name__ == '__main__':
    run()
