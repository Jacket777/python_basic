# 测试函数的定义和调用

def test01():
    print("*" * 10)
    print("@" * 10)



if __name__ == '__main__':
    test01()
    print("id: " +id(test01))
    print("type: " + type(test01))
    print(test01)


