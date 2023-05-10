"""
类的专有方法
1. __str__ 与 __repr__
2. __iter__ 与 __next__
3. __getitem__
4. __getattr__
"""

class Student(object):
    """
    str与repr函数演示
    """
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'student name: {self.name}'

    __repr__ = __str__

    def __getattr__(self, attr):
        if attr == 'score':
            return 95

    def __call__(self):
        print(f'call 方法调用')
        print(f'name: {self.name}')


class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化化两个计数器

    def __iter__(self):
        print(f"调用了iter方法 a: {self.a}, b:{self.b}")

        return self  #实例本身就是迭代器对象，所以返回自己

    def __next__(self):
        print(f"调用了next方法 a: {self.a}, b:{self.b}")
        self.a , self.b = self.b, self.a + self.b
        if self.a > 10: # 退出循环条件
            raise StopIteration
        return self.a

class Fib2(object):
    def __init__(self):
        self.a, self.b = 0,1 # 初始化两个计数器

    def __getitem__(self, item):
        print("调用了getitem方法")
        for x in range(item):
            print(f"x: {x}, a: {self.a}, b:{self.b}")
            self.a, self.b = self.b, self.a + self.b
        return self.b






if __name__ == '__main__':
    print(Student('jack'))
    # # Fib()
    # for n in Fib():
    #     print(n)
    # fib = Fib2()
    # print(fib[10])
    stu = Student('jack')
    print(stu.score)
    stu() # 调用的是call方法
    #判断一个对象是否被调用
    print(f'callable(stu): {callable(stu)}')
    print(f'callable(max): {callable(max)}')
    print(f'callable([1,2,3]): {callable([1,2,3])}')
    print(f'callable(None): {callable(None)}')
    print(f"callable('a'): {callable('a')}")

