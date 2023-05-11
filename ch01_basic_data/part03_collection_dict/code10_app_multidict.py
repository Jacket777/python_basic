"""
1.6 字典中的键映射多个值
问题
怎样实现一个键对应多个值的字典(也叫 multidict )？
解决方案
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要将这多个值放到另外的容器中，
"""
from collections import defaultdict


# 1.解决方案：将值放在列表, 或集合中
def test01():
    dict01 = {'a': [1, 2, 3], 'b': [4, 5]}  # 值为列表
    dict02 = {'a': {1, 2, 3}, 'b': {4, 5}}  # 值为集合
    for k, v in dict01.items():
        print(k, v)
    for k, v in dict02.items():
        print(k, v)


# TODO 2. 使用defaultdict
def test02():
    dict01 = defaultdict(list)  # 值为列表
    dict01['a'].append(1)
    dict01['a'].append(2)
    dict01['b'].append(4)
    dict02 = defaultdict(set)  # 值为集合
    dict02['a'].add(1)
    dict02['b'].add(2)
    dict02['a'].add(4)
    for k, v in dict01.items():
        print(k, v)
    for k, v in dict02.items():
        print(k, v)


# TODO 3. 普通字典实现方式
def test03():
    d = {}
    d.setdefault('a', []).append(1)
    d['a'].append(15)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print(d)


if __name__ == '__main__':
    test03()
