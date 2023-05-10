#  02 simple program and function
def simple():
    print("Hello world")
    print("What is your name?")
    myName = input()
    print("It is good to meet your, " + myName)
    print('The length of your name %d' % (len(myName)))
    print("What is your age ? ")
    myAge = input()
    print("You will be " + str(int(myAge) + 1) + " i a year")


# 类型转换
def typeTrans():
    a = str(29)  # int-->str
    print(type(a), a)
    b = str(-3.14)  # float-->str
    print(type(b), b)
    c = int('42')  # str-->int
    print(type(c), c)
    d = int('-99')  # float-->int
    print(type(d), d)
    a = int(1.99)  # float-->int
    print(type(a), a)
    b = float('3.14')  # str-->float
    print(type(b), b)
    c = float(10)  # int-->float
    print(type(c), c)


if __name__ == '__main__':
    # simple()
    typeTrans()
