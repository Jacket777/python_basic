# code08: list api
from math import pi


# 1. 列表元素的新增
def list_add_element():
    # T 1. 尾部新增
    list01 = []
    for i in range(1, 10):
        list01.append(i)
    print(list01)
    # 指定位置插入与新增
    list01 = [1, 2]
    for i in range(11, 25):
        list01.insert(0, i)
    print(list01)
    # 列表的扩展--新增多个元素
    list01 = [1, 2]
    list02 = [3, 4]
    list01.extend(list02)
    print(list01)


# 2. 列表元素的移除
def list_remove_element():
    # 根据列表中的元素进行删除
    spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
    spam.remove('cat')
    for i in range(len(spam)):
        print(spam[i] + ' ', end='', sep=',')
    print()
    #  从列表的尾部删除
    spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
    result = spam.pop()
    print(result)
    print(spam)
    #  从列表的指定位置弹出
    spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
    result = spam.pop(1)
    print(result)
    print(spam)


# 3. 查询元素index 与统计元素count
def test_index_count():
    list01 = [1,2,3,4,18,19]
    #  查询元素在列表中的下标
    index = list01.index(18)
    print(index)
    # 查询元素在列表中个数
    count = list01.count(18)
    print(count)


# 4. 列表的生成
def list_generator():
    # . 使用表达式
    squares = []
    for x in range(10):
        squares.append(x**2)
    print(squares)
    # 2. 使用列表推导式
    print("---------------------------")
    squares02 = [x**2 for x in range(10)]
    print(squares02)
    print("----------------------------")
    #  3. 嵌套循环特殊表达式生成
    result = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(result)
    print("----------------------------")
    #  4. 特殊表达式生成
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    print(combs)


# 5. 列表的推导式
def list_introduce():
    vec = [-4, -2, 0, 2, 4]
    #  1 基于原有列表生成
    list01 = [x * 2 for x in vec]
    print(list01)
    #  2 基于原有列表生成
    list02 = [x * 2 for x in vec if x >= 0]
    print(list02)
    #  3 基于原有列表生成
    list03 = [abs(x) for x in vec]
    print(list03)
    #  4 基于原有列表生成
    fruit_list = ['  banana', '  loganberry', 'passion fruit']
    fruit = [fruit.strip() for fruit in fruit_list]
    print(fruit)
    list04 = [(x, x**2) for x in range(6)]
    print(list04)
    #  5 嵌套推导
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list05 = [num for elem in vec for num in elem]
    print(list05)
    #  6 复杂表达式与函数
    list06 = [str(round(pi, i)) for i in range(1, 6)]
    print(list06)


if __name__ == '__main__':
    list_generator()


