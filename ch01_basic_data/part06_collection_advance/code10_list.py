"""
1.10 删除序列相同元素并保持顺序
问题
怎样在一个序列上面保持元素顺序的同时消除重复的值？
解决方案
如果序列上的值都是 hashable 类型，那么可以很简单的利用集合或者生成器来解决这个 问题。
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    print(seen)


def dedupe2(items, key=None):
    """内置函数key"""
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def sample_01():
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    result = list(dedupe(a))
    print(result)


def sample_02():
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    print(a)
    b = list(dedupe2(a, key=lambda d: (d['x'], d['y'])))
    print(b)
    c = list(dedupe2(a, key=lambda d: d['x']))
    print(c)





if __name__ == '__main__':
    sample_02()

