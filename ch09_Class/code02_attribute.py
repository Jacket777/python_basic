# 测试类属性
class Student:
    company = "sxt"  # 类属性
    count = 0  # 类属性

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count = Student.count + 1

    def say_score(self):
        print("我的公司是: ", Student.company)
        print("{0}的分数：{1}".format(self.name, self.score))


if __name__ == '__main__':
    s1 = Student("Jack", 100)
    s1.say_score()
    s2 = Student("Jack", 100)
    s3 = Student("Jack", 100)
    print('一共创建{0}个Student对象'.format(Student.count))
