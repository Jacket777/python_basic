"""
1.9 查找两字典的相同点
问题
怎样在两个字典中寻寻找相同点(比如相同的键、相同的值等等)？
"""


def sample_01():
    a = {'x': 1, 'y': 2, 'z': 3}
    b = {'w': 10, 'x': 11, 'y': 2}
    # Find keys in common
    result01 = a.keys() & b.keys()
    print(result01)
    # Find keys in a that are not in b
    result02 = a.keys() - b.keys()
    print(result02)
    # Find (key,value) pairs in common
    result03 = a.items() & b.items()
    print(result03)
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


if __name__ == '__main__':
    sample_01()