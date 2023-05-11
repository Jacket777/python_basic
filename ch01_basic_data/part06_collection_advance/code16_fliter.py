"""
1.16 过滤序列元素
问题
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
解决方案
简单的过滤序列元素的方法就是使用列表推导和fliter
"""
import math
from itertools import compress

def sample_01():
    my_list = [1, 4, -5, 10, -7, 2, 3, -1]
    larger_list = [ n for n in my_list if n > 0]
    print(larger_list)
    small_list = [ n for n in my_list if n < 0]
    print(small_list)
    pos = (n for n in my_list if n > 0)
    for x in pos:
        print(x)


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def sample_02():
    values = ['1', '2', '-3', '-', '4', 'N/A', '5']
    ivals = list(filter(is_int, values))
    print(ivals)


def sample_03():
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    result = [math.sqrt(n) for n in mylist if n > 0]
    print(result)
    clip_pos = [ n if n > 0 else 0 for n in mylist ]
    print(clip_pos)
    clip_neg = [ n if n < 0 else 0 for n in mylist ]
    print(clip_neg)


def sample_04():
    addresses = ['5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK'    '5645 N RAVENSWOOD', '1060 W ADDISON',
                 '4801 N BROADWAY', '1039 W GRANVILLE']
    counts = [0, 3, 10, 4, 1, 7, 6, 1]
    more5 = [n > 5 for n in counts]
    print(more5)
    result = list(compress(addresses, more5))
    print(result)



if __name__ == '__main__':
    sample_04()







if __name__ == '__main__':
    sample_02()

