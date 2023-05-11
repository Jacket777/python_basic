"""
1 解压序列赋值给多个变量
问题
现在有一个包含N个元素的元组或者是序列，怎样将它里面的值解压后同时赋值给N个变 量？
解决方案
任何的序列(或者是可迭代对象)可以通过一个简单的赋值语句解压并赋值给多个变量。 唯 一的前提就是变量的数量必须跟序列元素的数量是一样的
如果变量个数和序列元素的个数不匹配，会产生一个异常
实际上，这种解压赋值可以用在任何可迭代对象上面，而不仅仅是列表或者元组。 包括 字符串，文件对象，迭代器和生成器
"""


def sample_01():
    p = (4, 5)
    x, y = p
    print(x, y)
    data = ['ACME', 50, 91.1, (2020, 12, 21)]
    name, share, price, date = data
    print(name, share, price, date)
    s = 'Hello'
    a, b, c, d, e = s
    print(a, b, c, d, e)


def sample_02():
    data2 = ['ACME', 50, 91.1, (2020, 12, 21)]
    """下划线可以作为占位变量名进行占位"""
    _, share2, price2, _ = data2
    print(share2, price2)


if __name__ == '__main__':
    sample_01()

