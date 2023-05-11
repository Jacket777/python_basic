# code02: 类中方法调用与继承

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def add_twice(self, x):
        self.add(x)
        self.add(x)


# 1. 类实例方法的调用
def method_invoke():
    bag = Bag()
    bag.add(10)
    bag.add_twice(23)
    print(bag.data)


if __name__ == '__main__':
    method_invoke()


