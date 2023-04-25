# 测试返回值得基本用法
def add(a, b):
    """返回两个值得和"""
    print("计算两个数的和：{0}+{1}={2}".format(a, b, (a + b)))
    return a + b


def test02():
    """无任何返回值，返回值为None"""
    print("akjlkdk")
    return
    print("ttttt")


def test03(x, y, z):
    """返回列表"""
    return [x * 10, y * 10, z * 10]


if __name__ == '__main__':
    result = add(30, 40)
    print(result)
    real_result = test02()
    print(real_result)
    result03 = test03(1, 2, 3)
    print(result03)
    print(type(result03))

