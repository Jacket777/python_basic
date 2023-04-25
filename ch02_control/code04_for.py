#测试for循环
def test01():
    for x in (10, 20, 30):
        print(x * 3)
    for x in "abcdef":
        print(x)


def test02():
    d = {"name": "高清", "age": 10, "job": "programmer"}
    for x in d:
        print(x)
    for x in d.keys():
        print(x)
    for x in d.values():
        print(x)
    for x in d.items():
        print(x)

    for x in range(10):
        print(x)


def test03():
    sum_all = 0
    sum_odd = 0  # 100以内计数和
    sum_even = 0  # 100以内偶数和
    for x in range(101):
        sum_all += x
        if x % 2 == 1:
            sum_odd += x
        else:
            sum_even += x
    print("1-100累加和{0},奇数和{1},偶数和{2}".format(sum_all, sum_odd, sum_even))





#测试嵌套循环

def test04():
    for x in range(5):
        for y in range(5):
            print(x, end="\t")
        print()



#打印九九乘法表
def test05():
    for m in range(1, 10):
        for n in range(1, m + 1):
            print("{0}*{1}={2}".format(m, n, m * n), end="\t")
        print()



#使用列表和字典存储表格的数据
def test06():
    r1 = dict(name="高小一", age=18, salary=30000, city="北京")
    r2 = dict(name="高小二", age=28, salary=20000, city="上海")
    r3 = dict(name="高小三", age=38, salary=10000, city="广州")
    tb = [r1, r2, r3]

    for x in tb:
        if (x.get("salary") > 15000):
            print(x)




#循环代码优化测试
import time

def test07():
    start = time.time()
    for i in range(1000):
        result = []
        for m in range(1000):
            result.append(i * 1000 + m * 100)

    end = time.time()
    print("耗时: {0}".format((end - start)))



def test08():
    start = time.time()
    for i in range(1000):
        result = []
        c = i * 1000
        for m in range(1000):
            result.append(c + m * 100)

    end = time.time()
    print("耗时: {0}".format((end - start)))



#测试zip并行迭代
def test09():
    names = ("Jack01", "Jack02", "Jack03", "Jack04")
    ages = (18, 16, 20, 25)
    jobs = ("Teacher", "Programmer", "Employer")

    for name, age, job in zip(names, ages, jobs):
        print("{0}-{1}-{2}".format(name, age, job))



#测试循环中的else
def test10():
    salarySum = 0  # 总薪资
    salarys = []  # 存放薪资的列表

    for i in range(4):
        s = input("请输入员工的薪资(按Q或q结束)")
        if s.upper() == 'Q':
            print("录入完成，退出")
            break
        if float(s) < 0:
            continue
        salarys.append(float(s))
        salarySum += float(s)
    else:
        print("你已经全部录入4名员工的薪资")

    print("录入薪资", salarys)
    print("平均薪资{0}".format(salarySum / 4))

