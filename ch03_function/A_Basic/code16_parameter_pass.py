# 函数参数传递分类--可变与不可变

# 传递可变对象
a = [10, 20]
print(id(a))
print(a)
print("*******")


def test01(m):
    print(id(m))
    m.append(300)
    print(id(m))


# 传递不可变对象的引用
b = 100


def f1(n):
    print("n:", id(n))
    n = n + 200
    print("n:", id(n))
    print(n)


if __name__ == '__main__':
    print("传递可变对象")
    test01(a)
    print(a)
    print("传递不可变对象")
    f1(b)
    print("b", id(b))
