"array transpose"
import numpy as np


def transArray():
    arr01 = np.arange(1,13).reshape(2,6)
    print("arr01: ")
    print(arr01)
    arr02 = arr01.transpose()
    print("after transpose")
    print(arr02)
    print("=========more dimension============")
    arr03 = np.arange(1,37).reshape(1,3,3,4)
    print(arr03)
    print("=====after transpose=================")
    arr04 = np.transpose(arr03,[1,2,3,0])
    print(arr04)
    print("arr04.shape",arr04.shape)


transArray()




