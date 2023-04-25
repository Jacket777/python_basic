"""
测试tracback模块使用
"""

import traceback


def test01():
    try:
        print("step1")
        c = 1 / 0
    except:
        traceback.print_exc()


# 将异常日志输出到指定文件中######
def test02():
    try:
        print("step1")
        c = 1 / 0
    except:
        with open("d:/a.txt", "a") as f:
            traceback.print_exc(file=f)


if __name__ == '__main__':
    print(test01())
