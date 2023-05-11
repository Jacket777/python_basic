"""
列表的排序与反转
"""


# 1.数字排序
def test01():
    spam = [2, 5, 3.14, 1, -7]
    spam.sort()
    for i in range(len(spam)):
        print(str(spam[i]) + ' ', end='')
    print()
    print(spam.reverse())


# 2.使用倒序
def test02():
    spam = ['ants', 'badgers', 'cats', 'dogs', 'elephant']
    spam.sort(reverse=True)
    for i in range(len(spam)):
        print(spam[i] + ' ', end='')
    print()


# 3.使用ASCII字符顺序
def sort_asci():
    spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
    spam.sort()
    for i in range(len(spam)):
        print(spam[i] + ' ', end='')
    print()


# 4.使用字典字符顺序
def sort_dict():
    spam = ['a', 'z', 'A', 'Z']
    spam.sort(key=str.lower)
    for i in range(len(spam)):
        print(spam[i] + ' ', end='')


# 5.列表可变
def list_change():
    eggs = [1, 2, 3]
    eggs = [4, 5, 6]
    for i in range(len(eggs)):
        print(str(eggs[i]) + ',', end='')
    print()

    eggs2 = [1, 2, 3]
    del eggs2[2]
    del eggs2[1]
    del eggs2[0]
    eggs2.append(7)
    eggs2.append(8)
    eggs2.append(9)
    for i in range(len(eggs2)):
        print(str(eggs2[i]) + ',', end='')
    print()


if __name__ == '__main__':
    test01()




