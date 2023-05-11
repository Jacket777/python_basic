#  使用迭代器

# 1. 容器使用迭代器
def simple_use():
    for element in [1, 2, 3]:
        print(element)
    for element in ('a', 'b', 'c'):
        print(element)
    for key in {'one': 1, 'two': 2}:
        print(key)
    for element in "123":
        print(element)


# 2. 迭代器使用
def string_iter():
    str = 'abc'
    iter01 = iter(str)  # 获得迭代器
    a = next(iter01)
    print(a)
    a = next(iter01)
    print(a)
    a = next(iter01)
    print(a)
    a = next(iter01)  # 抛出StopIteration异常
    print(a)


# 3. 迭代器的实现
class Reverse:
    """迭代器实现反向输出"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print("调用迭代器")
        return self

    def __next__(self):
        print("调用next")
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def use_define_iter():
    rev = Reverse('spam')
    iter01 = iter(rev)
    print(iter01)
    char01 = next(iter01)
    print(char01)
    char01 = next(iter01)
    print(char01)
    char01 = next(iter01)
    print(char01)
    print("================")
    # 2.不使用iter,依然可以
    rev02 = Reverse('abc')
    char04 = next(rev02)
    print(char04)
    char04 = next(rev02)
    print(char04)
    char04 = next(rev02)
    print(char04)
    print("============")
    # 3.使用推导式的时候，查看是否调用iter---必须调用迭代器
    rev03 = Reverse('xyz')
    for ch in rev03:
        print(ch)





if __name__ == '__main__':
    # simple_use()
    # string_iter()
    use_define_iter()



# rev = Reverse('spam')
# print(rev)
# revIt = iter(rev)
# s = 'spams'
# for i in range(len(s)):
#     t = next(revIt)
#     print(t+" ,",end='')



# for char in rev:
#     print(char+",", end=' ')
# print("---------------generator----------------------")
# def reverse1(data):
#     for index in range(len(data) - 1, -1, -1):
#         yield data[index]
#
#
# for char in reverse1('golf'):
#     print(char + ",", end='')
# print()
#
#
# result = sum(i*i for i in range(10))
# print(result)
#
# xvec = [10,20,30]
# yvec = [7,5,3]
# result = sum( x*y for x, y in zip(xvec,yvec))
# print(result)
#
# data = 'golf'
# result = list(data[i] for i in range(len(data)-1,-1,-1))
# print(result)
