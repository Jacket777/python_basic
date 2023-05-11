"""
2 解压可迭代对象赋值给多个变量
问题
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才 能从这个可迭代对象中解压出N个元素出来？
解决方案
Python的星号表达式可以用来解决这个问题
讨论
扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的。
通常，这些可迭代对象的元素结构有确定的规则（比如第1个元素后面都是电话号码），
星号表达式让开发人员可以很容易的利用这些规则来解压出元素来。
"""
from functools import reduce


def add(x, y):
    return x + y


def drop_first_last(grades):
    first, *middle, last = grades
    return reduce(add, middle) / len(middle)


def sample_01():
    grades = [60, 78, 85, 98, 100]
    avg = drop_first_last(grades)
    print(avg)


def sample_02():
    record = ('Dave', 'dave@163.com', '0541-58128632', '0513-56235698')
    name, email, *phone_numbers = record
    print(phone_numbers)


def sample_03():
    sales_record = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    *trailing_qtr, current_qtr = sales_record
    trailing_avg = sum(trailing_qtr) / len(trailing_qtr)
    print(trailing_avg)


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


def sample_04():
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4)
    ]
    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


def sample_05():
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    result = line.split(":")
    uname, *fields, homedir, sh = line.split(":")
    print(result)


def sample_06():
    """废弃不要的元素"""
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name, year)


def sample_07():
    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    print(head)
    print(tail)


def sum01(items):
    """递归实现累加"""
    head, *tail = items
    return head + sum01(tail) if tail else head


def sample_08():
    items = [1, 10, 7, 4, 5, 9]
    print(sum01(items))


if __name__ == '__main__':
    sample_08()
