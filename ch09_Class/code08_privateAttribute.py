"""
测试私有属性
"""


class Employee:
    __company = "su"

    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有属性

    def __work(self):
        print("work hard")
        print("age: {0}".format(self.__age))
        print("=======", Employee.__company)


if __name__ == '__main__':
    e = Employee("高琪", 18)

    print(e.name)
    # print(e.age)
    print(e._Employee__age)
    # print(dir(e))
    e._Employee__work()
    print(Employee._Employee__company)
