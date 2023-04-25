"""
查看对象所有属性和object进行对比
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_age(self):
        print(self.name, " 的年龄", self.age)


if __name__ == '__main__':
    obj = object()
    print(dir(obj))

    s2 = Person("Jack", 18)
    print(dir(s2))
