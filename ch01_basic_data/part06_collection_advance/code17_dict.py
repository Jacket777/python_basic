"""
1.17 从字典中提取子集
问题
你想构造一个字典，它是另外一个字典的子集。
解决方案
简单的方式是使用字典推导
"""


def sample_01():
    prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
    # Make a dictionary of all prices over 200
    p1 = {key: value for key, value in prices.items() if value > 200 }
    # Make a dictionary of tech stocks
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    # 使用dict函数 虽然也可以完成，但是效率慢--直接推导慢一杯
    p3 = dict((key,value) for key,value in prices.items() if value > 200)
    # 这种方案大概比第一种方案慢1.6倍
    p4 = { key:prices[key] for key in prices.keys() & tech_names}
