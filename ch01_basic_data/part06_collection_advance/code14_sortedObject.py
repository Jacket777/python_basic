"""
1.14 排序不支持原生比较的对象
问题
你想排序类型相同的对象，但是他们不支持原生的比较操作。
解决方案
内置的 sorted() 函数有一个关键字参数 key ，可以传入一个 callable 对象给它， 这个 callable 对象对每个传入的对象返回一个值，
这个值会被 sorted 用来排序这些对象。
"""
from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_by_lambda():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))


def sort_by_operator():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=attrgetter('user_id')))
    print(min(users, key=attrgetter('user_id')))
    print(max(users, key=attrgetter('user_id')))




if __name__ == '__main__':
    # sort_by_operator()
    sort_by_lambda()