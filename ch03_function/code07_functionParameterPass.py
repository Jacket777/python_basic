#测试参数传递

#传递可变对象
a = [10,20]
print(id(a))
print(a)
print("*******")


def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))

test01(a)
print(a)

print("***************")
#传递不可变对象的引用
a = 100
def f1(n):
    print("n:",id(n))
    n = n +200
    print("n:", id(n))
    print(n)

f1(a)
print("a",id(a))
