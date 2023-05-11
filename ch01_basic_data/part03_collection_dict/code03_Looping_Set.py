# 代码清单07: 循环的技巧
import math


def dict_loop():
    knights = {'Galahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)


def zip_loop():
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print('what is your {0}, It is {1}'.format(q, a))


def sort():
    for i in reversed(range(1, 10, 2)):
        print(i, sep=',', end=' ')
    print()
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f, sep=',', end=' ')


def filter_data():
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filtered_data = []
    for value in raw_data:
        if not math.isnan(value):
            filtered_data.append(value)
    print(filtered_data)


if __name__ == '__main__':
    # dict_loop()
    # zip_loop()
    # sort()
    filter_data()
