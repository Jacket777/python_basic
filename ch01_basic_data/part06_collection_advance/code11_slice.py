"""
1.11 命名切片
问题
你的程序已经出现一大堆已无法直视的硬编码切片下标，然后你想清理下代码。
解决方案
假定你有一段代码要从一个记录字符串中几个固定位置提取出特定的数据字段(比如文件 或类似格式)：
"""


def sample_01():
    record = "....................100 .......513.25 .........."
    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)


def sample_02():
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)  # 创建一个切片对象
    print("------------")
    print(items[a])
    print("-------------")
    print(items[2:4])
    print("---替换-------")
    items[a] = [10, 11]
    print(items)
    print("---删除-------")
    del items[a]
    print(items)


def sample_03():
    s = slice(5, 10, 2)
    print(s.start)  # 切片的对象的三个属性
    print(s.stop)
    print(s.step)


"""
调用切片的 indices(size) 方法将它映射到一个确定大小的序列上， 
这个方法返回一个三元组 (start, stop, step) ，所有值都会被合适的缩小以满足边界限制， 
从而使用的时候避免出现 IndexError 异常
"""
def sample_04():
    a = slice(5, 50, 2)
    s = 'HelloWorld'
    b = a.indices(len(s))
    *d, = b  # 仍然可以使用
    print(d)
    # e = *a.indices(len(s))  不能这么用, 只能这么用
    for i in range(*a.indices(len(s))):
        print(s[i])
    pass





if __name__ == '__main__':
    sample_04()


