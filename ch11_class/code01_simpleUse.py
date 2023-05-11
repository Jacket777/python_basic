# class define
class MyClass:
    i = 12345
    counter = 0

    def f(self):
        return 'hello world'

x = MyClass()
print(x.f())

x.counter =1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter


class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0,-4.5)
print(str(x.r),str(x.i))

class Dog:
    kind = 'canine'
    #tricks = []

    def __init__(self,name):
        self.name = name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)
d.add_trick('rolly over')
e.add_trick('play dead')
print(d.tricks)


class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose,w2.region)


def f1(self,x, y):
    return min(x,y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c1 = C()
result = c1.f(3,4)
print(str(result))
print(c1.g())
print(c1.h())


print("===========================")
class Bag:
    def __init__(self):
        self.data = []

    def add(self,x):
        self.data.append(x)

    def addtwice(self,x):
        self.add(x)
        self.add(x)

bag = Bag()
bag.add(3)
bag.addtwice(6)
print(bag.data)

print("=========Inherit==================")
class Mapping:
    def __init__(self,iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self,iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update

class MappingSubclass(Mapping):
    def update(self,keys,values):
        for item in zip(keys,values):
            self.items_list.append(item)


print("=========pass==================")
class Employee:
    pass
john = Employee()
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 100


