"""
元组的使用
"""


# TODO 1 元组的定义与使用
def tuple_use():
    eggs = ('hello', 42, 0.5)  # 元组的定义
    print(eggs[0])
    newEggs = eggs[1:3]  # 元组的切分
    for i in range(len(newEggs)):
        print(str(newEggs[i]) + ',', end='')
    print()
    # eggs[1] = 99 报错， 元组初始化后不能修改


# TODO 2  类型转换 1. list ---> tuple
def list_to_tuple():
    spam = ['cat', 'dog', 5]
    print('spam type is ' + str(type(spam)))
    spam2 = tuple(spam)
    print('spam2 type is ' + str(type(spam2)))


# TODO 3  类型转换 2. tuple ---> list
def tuple_to_list():
    a = ('cat', 'dog', 5)
    print(a)
    print('a type is ' + str(type(a)))
    b = list(a)
    print(b)
    print('b type is ' + str(type(b)))


if __name__ == '__main__':
    tuple_to_list()
