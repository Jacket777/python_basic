"""
继承实例
"""

"""
基类
"""
class Animal(object):
    def run(self):
        print("Animal is running")

    def __run(self):
        # 子类无法继承父类私有方法
        print('I am a private method')

    def jump(self):
        print("animal is jumping....")





class Dog(Animal):
    def eat(self):
        print('Eating....')


class Cat(Animal):
    pass


if __name__ == '__main__':
    dog = Dog()
    dog.run()
    dog.jump()
    # dog.__run() 强行调用报错
    dog.eat()
    cat = Cat()
    cat.run()
    cat.jump()
