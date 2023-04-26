# eval函数 使用
s = "print('abcde')"

a = 10
b = 20
c = eval("a+b")

dict1 = dict(a=100, b=200)
d = eval("a+b", dict1)

if __name__ == '__main__':
    eval(s)
    print(c)
    print(d)
