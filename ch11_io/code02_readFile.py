#测试文件取取
def test01():
    with open(r"b.txt", "r", encoding="utf-8") as f:
        str = f.read(1)
        print(str)

# 测试readline
def test02():
    with open("b.txt", "r", encoding="utf-8") as f:
        for a in f:
            print(a, end="")


def test03():
    # a = ["I love you\n","Jack\n","Programmer\n"]
    # b = enumerate(a)
    # print(a)
    # print(list(b))
    with open("b.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() + " #" + str(index + 1) + "\n" for index, line in enumerate(lines)]

    with open("b.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


# 测试tell seek readline
def test04():
    with open("b.txt", "r", encoding="utf-8") as f:
        print("文件名是: {0}".format(f.name))
        print(f.tell())
        print("读取的内容是:{0}".format(f.readline()))
        f.seek(3)
        print(f.tell())
        print("读取的内容是:{0}".format(f.readline()))


def test05():
    # 测试readline
    with open("b.txt", "r", encoding="utf-8") as f:
        for a in f:
            print(a, end="")