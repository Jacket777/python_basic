"""
测试继承类的基本使用
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("no age")

    pass


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显示的调用父类的方法，不然解释器不会去调用
        self.score = score

    pass


if __name__ == '__main__':
    s = Student("Jack", 18, 60)
    s.say_age()
    print(s.name)
    print(dir(s))
    print(s._Person__age)
    # Student-->Person-->Object
    # print(Student.mro()) #查看继承
    # print(s.age)
