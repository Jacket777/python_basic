"""
5 实现一个优先级队列
问题
怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次pop操作总是返回优先级 高的那个元素
解决方案
下面的类利用 heapq 模块实现了一个简单的优先级队列
"""
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item{!r}'.format(self.name)


def sample_01():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q.pop())
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    sample_01()