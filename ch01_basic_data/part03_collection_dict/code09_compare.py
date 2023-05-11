# 代码清单08: 集合比较


def str_comp():
    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null = string1 or string2 or string3
    print(non_null)


def set_comp():
    a = (1, 2, 3) < (1, 2, 4)
    print(a)
    a = [1, 2, 7] < [1, 2, 4]
    print(a)
    a = 'ABC' < 'C' < 'Pascal' < 'Python'
    print(a)
    a = (1, 2, 3, 4) < (1, 2, 4)
    print(a)
    b = (1, 2) < (1, 2, -1)
    print(b)
    c = (1, 2, 3) == (1.0, 2.0, 3.0)
    print(c)
    d = (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
    print(d)


if __name__ == '__main__':
    set_comp()
