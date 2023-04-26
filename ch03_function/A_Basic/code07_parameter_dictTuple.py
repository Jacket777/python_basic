#函数可变参数处理--元组，字典两种方式
#测试强制命名参数

#元组方式
def testTupleParameter(a,b,*c):
    print(a,b,c)



#字典方式
def testDictParameter(a,b,**c):
    print(a,b,c)


# 元组与字典参数混合使用
def f3(a,b,*c,**d):
    print(a,b,c,d)

f3(8,9,20,30,name="jack",age=18)

def f4(*a,b,c):
    print(a,b,c)




if __name__ == '__main__':
    testTupleParameter(8, 9, 19, 20)
    testDictParameter(8, 9, name="jack", age=18)
    f3(8, 9, 20, 30, name="jack", age=18)
    # f4(2,3,4) #会报错，a是可变参数，将2,3,4全部收集，造成b,c没有赋值
    f4(2, b=3, c=4)