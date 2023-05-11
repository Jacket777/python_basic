"""
1.8 字典的运算
问题
怎样在数据字典中执行一些计算操作(比如求小值、大值、排序等等)？
解决方案

"""

def sample_01():
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
    """ zip() 函数创建的是一个只能访问一次的迭代器"""
    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(min_price)
    print(max_price)
    """排序"""
    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)
    """最大与最小值 ---键"""
    print(max(prices))
    print(min(prices))
    """最大与最小值 ---值"""
    print(max(prices.values()))
    print(min(prices.values()))
    """最低价股票与最高价股票"""
    min_value = min(prices, key=lambda k: prices[k])
    max_value = max(prices, key=lambda k: prices[k])
    print(min_price)
    print(max_value)
    """在执行 min() 和 max() 操作的时候，如果恰巧小或大值有重复的，那么拥有小或大键的实体会返回："""
    prices = {'AAA': 45.23, 'ZZZ': 45.23}
    min_result = min(zip(prices.values(), prices.keys()))
    print(min_result)
    max_result = max(zip(prices.values(), prices.keys()))
    print(max_result)

if __name__ == '__main__':
    sample_01()









if __name__ == '__main__':
    sample_01()
