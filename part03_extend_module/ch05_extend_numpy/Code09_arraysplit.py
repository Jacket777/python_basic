"array split"
import numpy as np


def splitArray():
    arr01 = np.arange(1, 13)
    "平均分割"
    arr02 = np.split(arr01, 4)
    print(arr02)
    print(arr02[0])
    print(arr02[1])
    print(arr02[2])
    print(arr02[3])
    print("传递数组，按位置分割")
    arr03 = np.split(arr01,[4,6])
    print(arr03)


#splitArray()


def splitTwoArray():
    arr01 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    print(arr01)
    print("======axis = 0,垂直方向，平均分割=======")
    r,w = np.split(arr01, 2, axis=0)
    print(r)
    print(w)
    print("======axis = 0,垂直方向，位置分割=======")
    r, w, k= np.split(arr01, [2,3], axis=0)
    print(r)
    print("---------------")
    print(w)
    print("--------------")
    print(k)
    print("======axis = 1,水平方向，平均分割=======")
    r, w = np.split(arr01, 2, axis=1)
    print(r)
    print(w)
    print("======axis = 1,水平方向，位置分割=======")
    r, w = np.split(arr01, [3], axis=1)
    print(r)
    print(w)


#splitTwoArray()

def hsplitArray():
    arr01 = np.arange(16).reshape(4,4)
    print("原有的数组: ")
    print(arr01)
    print("按水平分割后的两个数组")
    r,w = np.hsplit(arr01,2)
    print("===1.第一个数组=========")
    print(r)
    print("===2.第二个数组=========")
    print(w)
    print("====按位置分割=====")
    r, w = np.hsplit(arr01, [3])
    print("===1.第一个数组=========")
    print(r)
    print("===2.第二个数组=========")
    print(w)


hsplitArray()



def vsplitArray():
    arr01 = np.arange(16).reshape(4,4)
    print("原有的数组: ")
    print(arr01)
    print("按垂直分割后的两个数组")
    r,w = np.vsplit(arr01,2)
    print("===1.第一个数组=========")
    print(r)
    print("===2.第二个数组=========")
    print(w)
    print("=======按位置分割================")
    r, w = np.vsplit(arr01, [3])
    print("===1.第一个数组=========")
    print(r)
    print("===2.第二个数组=========")
    print(w)

#vsplitArray()






