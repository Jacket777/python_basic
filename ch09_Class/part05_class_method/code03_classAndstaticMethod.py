# 测试类方法,静态方法
class Student:
    company = "sxt"

    def __init__(self, name, score):
        self.name = name
        self.score = score

    @classmethod
    def printCompany(cls):
        print(cls.company)
        # print(self.name) #类方法和静态方法中不能调用实例变量和实例方法


class Student2:
    company = "sxt"

    @staticmethod
    def add(a, b):
        print("{0}+{1}={2}".format(a, b, (a + b)))


if __name__ == '__main__':
    Student.printCompany()
    Student2.add(2, 3)
