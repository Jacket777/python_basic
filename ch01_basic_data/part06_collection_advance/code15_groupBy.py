"""
1.15 通过某个字段将记录分组
问题
你有一个字典或者实例的序列，然后你想根据某个特定的字段比如 date 来分组迭代访 问。
解决方案
itertools.groupby() 函数对于这样的数据分组操作非常实用。
"""
from operator import itemgetter
from itertools import groupby
from collections import defaultdict



def sample_01():
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]
    rows.sort(key=itemgetter('date'))
    for date, items, in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


def sample_02():
    rows_by_date = defaultdict(list)
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]
    for row in rows:
        rows_by_date[row['date']].append(row)
    for r in rows_by_date['07/01/2012']:
        print(r)



if __name__ == '__main__':
    sample_02()




