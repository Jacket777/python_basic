#测试continue语句

def test01():
    empNum = 0  # 员工人数
    salarySum = 0  # 总薪资
    salarys = []  # 存放薪资的列表

    while True:
        s = input("请输入员工的薪资(按Q或q结束)")
        if s.upper() == 'Q':
            print("录入完成，退出")
            break
        if float(s) < 0:
            continue
        empNum += 1
        salarys.append(float(s))
        salarySum += float(s)

    print("员工数{0}".format(empNum))
    print("录入薪资", salarys)
    print("平均薪资{0}".format(salarySum / empNum))


if __name__ == '__main__':
    test01()