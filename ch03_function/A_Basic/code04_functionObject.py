# 测试函数也是对象 函数名其实是指向函数对象的一个引用
def test01():
    """无参函数"""
    print("sx")


def test02(a, b):
    return a + b


if __name__ == '__main__':
    test01()
    print("=============")
    c = test01
    c()
    print(id(test01))
    print(id(c))
    print(id(test01) == id(c))
    print(type(c))
    print("-----------")
    other=test02
    print(id(test02))
    print(id(other))
    print(other(3,4))



