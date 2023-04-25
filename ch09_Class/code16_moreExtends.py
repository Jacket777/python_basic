"""
测试多重继承
"""


class A:
    def aa(self):
        print("aa")


class B:
    def bb(self):
        print("bb")


class C(B, A):
    def cc(self):
        print("cc")


if __name__ == '__main__':
    c = C()
    c.aa()
    c.bb()
    c.aa()
