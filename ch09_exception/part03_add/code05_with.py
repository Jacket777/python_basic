#
"""
测试with 上下文管理使用，不是用来取代，只是作为补充
"""


def test01():
    with open("d:/dd.txt", "r") as f:
        content = f.readline()
        print(content)

    print("程序结束")


if __name__ == '__main__':
    print(test01())
