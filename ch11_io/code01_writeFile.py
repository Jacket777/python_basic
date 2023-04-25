

# 测试写入文件
def test01():
    f = open(r"a.txt", "w")
    f.write("abcd\ntest\n134")
    f.close()

# 测试写入中文文件
def test02():
    f = open(r"b.txt", "w", encoding="utf-8")
    f.write("中国\n江苏\n南京")
    f.close()

# 测试writelines写入数据
def test03():
    f = open(r"bb.txt", "w", encoding="utf-8")
    s = ["高七\n", "高三\n", "高四\n"]
    f.writelines(s)
    f.close()

def test04():
    # 测试结合异常机制确保关闭文件对象
    try:
        f = open(r"my01.txt", "a")
        str = "abcd"
        f.write(str)
    except BaseException as e:
        print(e)
    finally:
        f.close()

# 测试上下文管理器 with语句
def test05():
    a = ["高七\n", "高三\n", "高四\n"]
    with open(r"d.txt", "w") as f:
        f.writelines(a)

# 测试二进制文件的读写
def test06():

    with open("test.jpg", "rb") as f:
        with open("test_copy.jpg", "wb") as w:
            for line in f.readlines():
                w.writelines(line)
    print("图片拷贝完成")

def test07():
    # a = ["I love you\n","Jack\n","Programmer\n"]
    # b = enumerate(a)
    # print(a)
    # print(list(b))
    with open("b.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() + " #" + str(index + 1) + "\n" for index, line in enumerate(lines)]

    with open("b.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


def test08():
    # a = ["I love you\n","Jack\n","Programmer\n"]
    # b = enumerate(a)
    # print(a)
    # print(list(b))
    with open("b.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [line.rstrip() + " #" + str(index + 1) + "\n" for index, line in enumerate(lines)]

    with open("b.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)


if __name__ == '__main__':
    test01()