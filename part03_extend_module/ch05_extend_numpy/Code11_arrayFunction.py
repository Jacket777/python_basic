"array function"
import numpy as np

def artihFunction():
    a = np.arange(9,dtype=float).reshape(3,3)
    print("a 数组：")
    print(a)
    b = np.array([10,10,10])
    print("b 数组：")
    print(b)
    print(" a 数组与 b 数组之和 ")
    arr01 = np.add(a,b)
    print(arr01)
    arr02 = a + b
    print(" a 数组与 b 数组之和 另一种表示 ")
    print(arr02)
    arr03 = np.subtract(a,b)
    print(" a 数组与 b 数组之差 ")
    print(arr03)
    arr04 = a - b
    print(" a 数组与 b 数组之差 另一种表示 ")
    print(arr04)
    arr05 = np.multiply(a,b)
    print(" a 数组与 b 数组之积 ")
    print(arr05)
    print(" a 数组与 b 数组之积 另一种表示")
    arr06 = a * b
    print(arr06)
    arr07 = np.divide(a,b)
    print(" a 数组 / b 数组")
    print(arr07)



#artihFunction()

"通用函数指定输出结果的用法"
def getResult():
    x = np.arange(5)
    y = np.empty(5) #存储结果
    print(y)
    np.multiply(x,10,out=y)
    print(y)

#getResult()


def triangleFun():
    arr01 = np.array([0,30,45,60,90])
    print(arr01)
    print("不同角度的sin")
    print(np.sin(arr01*np.pi/180))
    print("不同角度的cos")
    print(np.cos(arr01 * np.pi / 180))
    print("不同角度的tan")
    print(np.tan(arr01 * np.pi / 180))

#triangleFun()



def floatFun():
    arr01 = np.array([1.0,4.55,123,0.567,25.532])
    print("arr01: ")
    print(arr01)
    print("after round")
    print(np.around(arr01)) #
    print(np.around(arr01,decimals=  1))
    print(np.around(arr01,decimals = -1))
    print("after floor")
    print(np.floor(arr01))
    print("after ceil")
    print(np.ceil(arr01))

#floatFun()

def powerFun():
    arr01 = np.arange(12).reshape(3,4)
    print("arr01:")
    print(arr01)
    print(np.power(arr01,2))
    print("=====指定输出结果=======")
    x = np.arange(5)
    y = np.zeros(10)
    np.power(2,x,out=y[:5])
    print('power:',x)
    print(y)

#powerFun()




def medianFun():
    arr01 = np.array([4,2,1,5])
    print("偶数的中位数: ",np.median(arr01))
    arr02 = np.array([4,2,1])
    print("奇数的中位数: ", np.median(arr02))
    arr03 = np.arange(1,16).reshape(3,5)
    print("arr03: ")
    print(arr03)
    print("use median")
    print("arr03 median: ",np.median(arr03))
    print("use median axis= 1 行的中值")
    print("arr03 median: ", np.median(arr03,axis=1))
    print("use median axis= 0 列的中值")
    print("arr03 median: ", np.median(arr03, axis=0))

#medianFun()



def meanFun():
    arr01 = np.arange(1,11).reshape(2,5)
    print("arr01: ")
    print(arr01)
    print("调用 mean 函数")
    print(np.mean(arr01))
    print("调用 mean 函数 axis = 0")
    print(np.mean(arr01,axis = 0))
    print("调用 mean 函数 axis = 1")
    print(np.mean(arr01, axis=1))


meanFun()














