# 测试多分支选择结构

def test01():
    score = int(input("请输入分数: "))
    grade = ""
    if score < 60:
        grade = "不及格"
    elif score < 80:
        grade = "及格"
    elif score < 90:
        grade = "良好"
    else:
        grade = "优秀"

    print("分数是:{0},等级:{1}".format(score, grade))


def test02():
    score = int(input("请输入分数: "))
    grade = ""
    if score < 60:
        grade = "不及格"
    if 60 <= score < 80:
        grade = "及格"
    if 80 <= score < 90:
        grade = "良好"
    if 90 <= score < 100:
        grade = "优秀"

    print("分数是:{0},等级:{1}".format(score, grade))


# 测试选择结构的嵌套
def test03():
    score = int(input("请输入一个在0-100之间的数字: "))
    grade = ""
    if score > 100 or score < 0:
        score = int(input("输入错误！请重新输入一个在0-100之间的数字"))
    else:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        elif score >= 60:
            grade = 'D'
        else:
            grade = 'E'
        print("分数为:{0},等级为:{1}".format(score, grade))


def test04():
    score = int(input("请输入一个在0-100之间的数字: "))
    degree = "ABCDE"
    num = 0
    if score > 100 or score < 0:
        print("请输入一个在0-100之间的数字: ")
    else:
        num = score // 10
        if num < 6:
            num = 5
        print("分数是:{0},等级是:{1}".format(score, degree[9 - num]))


if __name__ == '__main__':
    test01()
