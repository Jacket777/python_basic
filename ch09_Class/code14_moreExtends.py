"""
测试查看类的继承层次结构
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


if __name__ == '__main__':
    print(C.mro())
    print("********")
    print(C.__mro__)
