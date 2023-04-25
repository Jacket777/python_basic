"""
内部装饰器
"""

class A:
    @classmethod
    def method(cls):
        print("hello world A")
        pass


class B:
    def method(cls):
        print("hello world B")
        pass
    method = classmethod(method) # 等效 类A的写法



if __name__ == '__main__':
    A.method()
    B.method()





