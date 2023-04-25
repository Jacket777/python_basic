"""
测试方法的重写
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("my age", self.__age)

    def say_introduce(self):
        print("my name is {0}".format(self.name))


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显示的调用父类的方法，不然解释器不会去调用
        self.score = score

    def say_introduce(self):
        '''重写父类的方法'''
        print("I am student ,my name is {0}".format(self.name))


if __name__ == '__main__':
    s = Student("Jack", 18, 60)
    s.say_age()
    s.say_introduce()
