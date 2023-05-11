# code05 open txt
import subprocess


def open_sp():
    """使用写字板打开txt文档"""
    #subprocess.Popen(['c:/Windows/notepad.exe', 'D:/python_workspace/python_basic/ch15_threading/part01_simple/hello.txt'])
    """运行Python 脚本, 在交换式中运行下面的代码"""
    subprocess.Popen(['D:/software/python/python.exe',
                      'D:/python_workspace/python_basic/ch15_threading/part01_simple/code01_threadDemo.py'])


def open_default():
    """使用默认程序打开"""
    with open('hello2.txt', 'w') as f:
        f.write('Hello world!')
    subprocess.Popen(['start', 'hello2.txt'], shell=True)


if __name__ == '__main__':
    open_sp()
    open_default()
