"""
继承threa 类使用
"""
import threading
from time import sleep
from datetime import datetime

loops = [4, 2]  # 设定休眠时间
date_time_format = '%y-%M-%d %H:%M:%S'


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        """

        :param func: 线程需要的执行方法
        :param args: 方法参数
        :param name: 线程名称
        """
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def __call__(self):
        print("--call-----")
        print(f'starting {self.name} at:{date_time_str(datetime.now())}\n')
        self.res = self.func(*self.args)
        print(f'{self.name} finished at:{date_time_str(datetime.now())}\n')


def loop(n_loop, n_sec):
    print(f'线程({n_loop}) 开始执行:{date_time_str(datetime.now())}, 先休眠({n_sec})秒\n')
    sleep(n_sec)
    print(f'线程({n_loop}) 休眠结束，结束于:{date_time_str(datetime.now())}\n')


def main():
    print(f'---所有线程开始执行：{date_time_str(datetime.now())}')
    threads = []  # 线程列表
    n_loops = range(len(loops))
    # 定义线程
    for i in n_loops:
        t = threading.Thread(
            target=MyThread(loop, (i, loops[i]), loop.__name__))
        threads.append(t)
    print("线程定义完毕")
    # 启动线程
    for i in n_loops:
        threads[i].start()
    # 等待所有线程结束
    for i in n_loops:
        threads[i].join()
    print(f'---所有线程结束于：{date_time_str(datetime.now())}')


if __name__ == '__main__':
    main()
