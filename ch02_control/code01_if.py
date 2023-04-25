'''
IF 使用
条件判断不能用赋值语句
'''


def testIf():
    a = input("请输入一个小于10的数字: ")
    if int(a) < 10:
        print(a)


def testIF01():
    b = []
    if not b:
        print("空的列表是false")


def testIF02():
    c = "False"  # 非空字符串也是True
    if c:
        print("c")


def testIF03():
    d = 10
    if d:
        print("d")

    if 3 < d < 11:
        print("3<d<11")


if __name__ == '__main__':
    testIf()
