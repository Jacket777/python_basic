"""
多重继承
"""


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal):
    pass


class Bat(Mammal):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


class Runnable(object):
    def run(self):
        print('Running')


class Flyable(object):
    def fly(self):
        print('flying')


class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass
