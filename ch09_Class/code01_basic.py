class Student:  # 类名一般首字母大写多个单词采用驼峰原则
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_score(self):  # self必须位于第一个参数
        print("{0}的分数：{1}".format(self.name, self.score))


class Man:
    pass


def test01():
    s1 = Student("高七", 18)  # 通过类名进行调用构造函数
    s1.say_score()
    s1.age = 32
    s1.salary = 3000
    # del s1 删除对象，从属对象的属性都被删除
    print(s1.salary)


def test02():
    s2 = Student("Jack", 100)
    s2.say_score()
    Student.say_score(s2)
    print(dir(s2))
    print(s2.__dict__)
    print(isinstance(s2, Student))
    print(isinstance(s2, Man))


def test03():
    stu2 = Student
    s2 = stu2("Jack", 100)
    s1 = Student("Jack", 100)

    s1.say_score()
    s2.say_score()


if __name__ == '__main__':
    test03()
