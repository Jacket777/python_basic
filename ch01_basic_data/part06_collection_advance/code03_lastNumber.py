"""
3 保留后N个元素
问题
在迭代操作或者其他操作的时候，怎样只保留后有限几个元素的历史记录？
解决方案
保留有限历史记录正是 collections.deque 大显身手的时候。
"""

from collections import deque


def sample_01():
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.append(4)
    print(q)
    q.append(5)
    print(q)


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            """生成器与迭代器"""
            yield li, previous_lines
            # print(previous_lines)
        previous_lines.append(li)


def sample_02():
    """重要代码"""
    with open(r'somefile.txt') as f:
        for line, previous in search(f, 'python', 5):
            for pline in previous:
                print(pline, end='')
            print(line, end='')
            print('-'*30)


def sample_03():
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)
    q.appendleft(4)
    print(q)
    q.pop()
    print(q)
    q.popleft()
    print(q)


if __name__ == '__main__':
    sample_03()