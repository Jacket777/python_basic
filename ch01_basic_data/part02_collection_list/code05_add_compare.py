import time


def test01():
    time01 = time.time()  # 起始时间
    a = ''
    for i in range(1000000):
        a += "sxt"
    time02 = time.time()  # 结束时间
    print("run time 01==>" + str(time02 - time01))


def test02():
    time01 = time.time()
    li = []
    for i in range(1000000):
        li.append("sxt")
    a = "".join(li)

    time02 = time.time()
    print("run time 02==>" + str(time02 - time01))


if __name__ == '__main__':
	test01()







