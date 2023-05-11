
"""
code01 使用threading 实例
"""
import threading, time


def takANap():
    time.sleep(15)
    print('Wake up!')


if __name__ == '__main__':
    print("Start of program.")
    thread01 = threading.Thread(target=takANap())
    thread01.start()
    print("End of program.")

