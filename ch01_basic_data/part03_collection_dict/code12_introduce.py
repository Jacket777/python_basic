# 测试推导式

# 列表推导式
def test01():
    y = [x * 2 for x in range(1, 50) if x % 5 == 0]
    print(y)


def test02():
    y = []
    for x in range(1, 50):
        if x % 5 == 0: y.append(x * 2)
    print(y)


def test03():
    cells = [(row, col) for row in range(1, 10) for col in range(1, 10)]
    print(cells)


# 字典推导式
def test04():
    my_text = "i love you,i love sxt,i love gaoqi"
    char_count = {c: my_text.count(c) for c in my_text}
    print(char_count)


# 普通循环实现计数


# 集合推导式
def test05():
    b = {x for x in range(1, 100) if x % 9 == 0}
    print(b)


# 生成器迭代器
def test06():
    gnt = (x for x in range(1, 100) if x % 9 == 0)
    print(gnt)
    print(tuple(gnt))
    print(tuple(gnt))


if __name__ == '__main__':
	test01()
