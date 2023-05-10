"""
8.8. 获取对象信息
1.type
判断各种类型--基本数据类型，函数
2.isinstance
判断对象是否属于某个类，主要用于有继承关系的类
3.dir
获取对象的全部属性和方法
"""
import types

class Dog:
    pass

def test_type():
    # 基本类型判断
    print(f'type(123):  {type(123)}')
    print(f"type('abc'):  {type('abc')}")
    # 指向函数
    print(f'type(abs):  {type(abs)}')
    # 指向类
    dog = Dog()
    print(f'type(dog):  {type(dog)}')
    # 判断两个变量的type是否相同
    print(f'type(123) == type(456):  {type(123) == type(456)}')
    print(f'type(123) == int:  {type(123) == int}')
    print(f"type('abc') == str:  {type('abc') == str}")
    print(f"type('abc') == type(123):  {type('abc') ==type(123)}")


def use_type_module():
    print(f'type(test_type) == types.FunctionType: {type(test_type) == types.FunctionType}')
    print(f'type(abs) == types.FunctionType: {type(abs) == types.BuiltinFunctionType}')
    print(f'type(lambda x:x) == types.LambdaType: {type(lambda x:x) == types.LambdaType}')
    print(f'type(x for x in range(10)) == types.GeneratorType: {type(x for x in range(10)) == types.GeneratorType}')



class Animal:
    pass

class Dog(Animal):
    pass
def test_isinstance():
    animal = Animal()
    dog = Dog()
    print(f'isinstance(dog, Dog):  {isinstance(dog, Dog)}')
    print(f'isinstance(dog, Animal):  {isinstance(dog, Animal)}')
    print(f'isinstance(dog, object):  {isinstance(dog, object)}')
    print(f'isinstance(dog, Dog) and isinstance(dog, Animal):  {isinstance(dog, Dog) and isinstance(dog, Animal)}')
    print(f'isinstance(animal, Dog):  {isinstance(animal, Dog)}')
    print(f'isinstance([1,2],(list,tuple): {isinstance([1,2],(list,tuple))}')
    print(f'isinstance((1,2),(list,tuple): {isinstance((1,2),(list,tuple))}')
    print(f'isinstance([1,2],list): {isinstance([1,2],list)}')
    print(f'isinstance((1,2),list): {isinstance((1, 2), list)}')

def test_dir():
    print(dir('abc'))



if __name__ == '__main__':
    # test_type()
    # use_type_module()
    # test_isinstance()
    test_dir()