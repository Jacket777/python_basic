# 测试while循环


def test01():
    num = 0
    while num <= 100:
        print(num, end="\t")
        num += 1


# 计算1-100累加和
def test02():
    num = 0
    sum_all = 0
    while num <= 100:
        sum_all = sum_all + num
        num += 1
    print("1-100所有数的累加和: ", sum_all)


# 测试break
def test03():
    while True:
        a = input("请输入一个字符（输入Q或q时退出）: ")
        if a == "q" or a == "Q":
            print("循环结束，退出")
            break
        else:
            print(a)


if __name__ == '__main__':
    test01()
