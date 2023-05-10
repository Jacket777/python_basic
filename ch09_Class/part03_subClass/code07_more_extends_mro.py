"""
测试mro()多重继承
"""


class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say AAAA")


class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBBB")


class C(A, B):
    def cc(self):
        print("cc")


if __name__ == '__main__':
    c = C()

    print(C.mro())  # 打印类的层次结构
    c.say()  # 解释器寻找方法，是从左到右方式寻找，会执行B中的方法
