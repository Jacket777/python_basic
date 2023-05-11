"""
1.6 字典中的键映射多个值
问题
怎样实现一个键对应多个值的字典(也叫 multidict )？
解决方案
一个字典就是一个键对应一个单值的映射。如果你想要一个键映射多个值，那么你就需要 将这多个值放到另外的容器中，
"""
from collections import defaultdict


def sample_01():
    d = defaultdict(list)
    """值为列表"""
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(d)
    c = defaultdict(set)
    """值为集合"""
    c['a'].add(1)
    c['a'].add(2)
    c['b'].add(4)
    print(c)
    d = {}
    """普通字典实现方式"""
    d.setdefault('a', []).append(1)
    d.setdefault('a', []).append(2)
    d.setdefault('b', []).append(4)
    print(d)




if __name__ == '__main__':
    sample_01()