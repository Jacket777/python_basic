
"""
 线程中带参数
"""
import threading

if __name__ == '__main__':
    thread01 = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep': '&'})
    thread01.start()



