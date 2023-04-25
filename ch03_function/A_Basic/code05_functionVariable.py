#测试全局变量，局部变量
a = 3 #全局变量

def test01():
    b = 4
    print(b*10)
    global a #如果要在函数内改变全局变量的值，增加global关键字声明
    a = 300
    print(locals()) #打印输出局部变量
    print(globals())#打印输出全局变量

if __name__ == '__main__':
    test01()


