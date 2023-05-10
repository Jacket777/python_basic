"""
测试has-a关系，使用组合
"""


class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("计算123456")
        print("cpu对象:", self)


class Screen:
    def show(self):
        print("显示：123456")
        print("screen对象:", self)


if __name__ == '__main__':
    m = MobilePhone(CPU(), Screen())
    m.cpu.calculate()
    m.screen.show()
