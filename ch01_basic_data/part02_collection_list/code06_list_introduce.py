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
