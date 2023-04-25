# 测试函数也是对象
def test01():
    print("sx")


test01()
print("=============")
c = test01
c()
print(id(test01))
print(id(c))
print(type(c))
