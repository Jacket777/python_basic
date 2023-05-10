"""
多态实例
"""
class Animal(object):
    def run(self):
        print("animal is running....")


class Dog(Animal):
    def run(self):
        # 覆盖了父类的方法
        print("Dog is running....")


class Cat(Animal):
    def run(self):
        print("Cat is running....")


def test01():
    a = list()
    b = Animal()
    c = Dog()
    print(f'a 是否为list类型对象： {isinstance(a, list)}')
    print(f'b 是否为Animal类型对象： {isinstance(b, Animal)}')
    print(f'b 是否为Dog类型对象： {isinstance(b, Dog)}')
    print(f'c 是否为Animal类型对象： {isinstance(c, Animal)}')
    print(f'c 是否为Dog类型对象： {isinstance(c,Dog)}')




def run_two_times(animal):
    animal.run()
    animal.run()


class Bird(Animal):
    def run(self):
        print(f'Bird is flying in the sky.....')


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    test01()
    run_two_times(dog)
    run_two_times(Bird())