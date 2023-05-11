"""
1.13 通过某个关键字排序一个字典列表
问题
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
解决方案
通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构
原理：sorted() 内置函数
"""

from operator import itemgetter

def sample_01():
    rows = [{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
            {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    row_by_uid = sorted(rows, key=itemgetter('uid'))
    row_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_fname)
    print(row_by_uid)
    print(row_by_lfname)
    print("max---min")
    min_uid = min(rows, key=itemgetter('uid'))
    print(min_uid)
    max_uid = max(rows, key=itemgetter('uid'))
    print(max_uid)
    print("------lambda-------")
    sort_by_fname = sorted(rows, key=lambda r: r['fname'])
    sort_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
    print(sort_by_fname)
    print(sort_by_lfname)
    


if __name__ == '__main__':
    sample_01()