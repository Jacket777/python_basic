# 测试返回值得基本用法
def add(a, b):
    print("计算两个数的和：{0},{1},{2}".format(a, b, (a + b)))
    return a + b


def test02():
    print("akjlkdk")
    return
    print("ttttt")


def test03(x, y, z):
    return [x * 10, y * 10, z * 10]


c = add(30, 40)
print(c)
d = test02()
print(d)
print(test03(1, 2, 3))
