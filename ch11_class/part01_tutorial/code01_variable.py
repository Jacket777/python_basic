# code02 类变量与实例变量 以及属性覆盖

class Dog:
    kind = 'canine'  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量
        self.tricks = []  # 实例变量

    def add_trick(self, trick):
        self.tricks.append(trick)


def use_dog():
    dog01 = Dog('Fido')
    dog02 = Dog('Buddy')
    print(dog01.kind, dog01.name)
    print(dog02.kind, dog02.name)
    dog01.add_trick('roll over')
    dog02.add_trick('play dead')
    print(dog01.tricks)
    print(dog02.tricks)


class Warehouse:
    purpose = 'storage'
    region = 'west'


# 属性覆盖
def use_warehouse():
    w1 = Warehouse()
    print(w1.purpose, w1.region)
    w2 = Warehouse()
    w2.region = 'east'
    print(w2.purpose, w2.region)


if __name__ == '__main__':
    # use_dog()
    use_warehouse()





