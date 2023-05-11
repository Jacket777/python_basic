# code06 : 单继承

class Anima:
    type = 'Animal'

    def eat(self):
        print("eat somthing")


class Dog(Anima):
    kind = 'Japan'

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        super().eat()
        print(food)


if __name__ == '__main__':
    dog01 = Dog('Tom')
    print(dog01.type, dog01.name)
    dog01.eat('beef')
