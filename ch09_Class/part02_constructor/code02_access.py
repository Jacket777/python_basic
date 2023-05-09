"""
类的属性访问权限
默认为public
在属性名称前加两个下划线为private

"""


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def info(self):
        print(f'student:{self.name}, score:{self.score}')


"""
私有属性
"""


class College_Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def info(self):
        print(f'student:{self.name}, score:{self.score}')

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print('请输入0到100的数字')


class PrivatePublicMethod(object):
    def __init__(self):
        pass

    def __foo(self):
        print("这是私有方法")

    def foo(self):
        print("这是公有方法")
        print("公有方法中调用私有方法")
        self.__foo()
        print("公有方法中调用私有方法")


if __name__ == '__main__':
    stu = Student('Jack', 100)
    print(f'before modify score: {stu.score}')
    stu.info()
    stu.score = 0
    print(f'after modify score:{stu.score}')
    stu.info()
    stu2 = College_Student('tom', 100)
    print(f'college student tom score： {stu2.get_score()}')
    stu2.set_score(98)
    print(f'college student tom score： {stu2.get_score()}')
    test = PrivatePublicMethod()
    test.foo()
