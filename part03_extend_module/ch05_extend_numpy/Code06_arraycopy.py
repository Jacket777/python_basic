"use array copy"
import numpy as np

def copyarray():
    a = np.arange(1,13).reshape((3,4))
    print(a)
    print("get the two row and two column")
    #通过切片可以获得新数组，即使赋值给新的变量，但还是原来数组的视图，如果对切片数组进行修改，会影响原来的数组
    #如何避免--使用numpy中的copy方法实现
    sub_a = a[:2,:2]
    print(sub_a)
    sub_a[0][0] = 100
    print(sub_a)
    print(a)
    sub_b = np.copy(a[:2,:2]) #深拷贝
    sub_b[0][0] = 200
    print(sub_b)
    print(a)

copyarray()




