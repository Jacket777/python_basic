"""
线程队列
"""
import threading
import queue
from  time import sleep


class MyThread(threading.Thread):
    def __init__(self,threadID,name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print(f"开启线程: {self.name}")
        process_data(self.name,self.q)
        print(f"退出线程: {self.name}")

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print(f"{threadName} process {data}")
        else:
            queueLock.release()
        sleep(1)
def main():
    global exitFlag
    exitFlag = 0
    threadList = ["Thread-1","Thread-2","Thread-3"]
    nameList = ["One","Two","Three","Four","Five"]
    threads = []
    threadID = 1
    # 创建新线程
    for tName in threadList:
        thread = MyThread(threadID,tName,workQueue)
        thread.start()
        threads.append(thread)
        threadID +=1
    # 填充队列
    queueLock.acquire()
    for word in nameList:
        workQueue.put(word)
    queueLock.release()
    # 等待队列清空
    while not workQueue.empty():
        pass
    # 通知线程是否退出的时候了
    exitFlag = 1

    #  等待所有线程完成
    for t in threads:
        t.join()
    print("退出主线程")

if __name__ == '__main__':
    queueLock = threading.Lock()
    workQueue = queue.Queue(10)
    main()
