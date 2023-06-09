"""
4 查找大或小的N个元素
问题
怎样从一个集合中获得大或者小的N个元素列表？
解决方案
heapq模块有两个函数： nlargest() 和 nsmallest() 可以完美解决这个问题。
"""

import heapq

def sample_01():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))   # Prints [42, 37, 23
    print(heapq.nsmallest(3, nums))  # Prints [-4, 1, 2]




def sample_02():
    portfolio = [{'name': 'IBM', 'shares': 100, 'price': 91.1}, {'name': 'AAPL', 'shares': 50, 'price': 543.22},
                 {'name': 'FB', 'shares': 200, 'price': 21.09}, {'name': 'HPQ', 'shares': 35, 'price': 31.75},
                 {'name': 'YHOO', 'shares': 45, 'price': 16.35}, {'name': 'ACME', 'shares': 75, 'price': 115.65}]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)


def sample_03():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    """堆排序"""
    heapq.heapify(nums)
    print(nums)
    """出堆操作"""
    min_value = heapq.heappop(nums)
    print(min_value)
    print(nums)
    min_value = heapq.heappop(nums)
    print(min_value)
    min_value = heapq.heappop(nums)
    print(min_value)


if __name__ == '__main__':
    sample_03()
