"array connect"
import numpy as np

def HVstackCon():
    a = np.array([[1,2,3],[4,5,6]])
    b = np.array([[11, 12, 13], [14, 15, 16]])
    print("a:")
    print(a)
    print("b:")
    print(b)
    print("=====hstack==水平拼接=====")
    arr01 = np.hstack([a,b])
    print(arr01)
    print("=====vstack==垂直拼接=====")
    arr02 = np.vstack([a,b])
    print(arr02)
    print("=====concatenate=====")
    print("=====concatenate=====axis=0 默认情况==垂直拼接===")
    arr03 = np.concatenate((a,b),axis=0)
    print("arr03:")
    print(arr03)
    arr04 = np.concatenate((a, b))
    print("arr04:")
    print(arr04)
    arr05 = np.concatenate((a, b), axis=1)
    print("arr05:")
    print(arr05)
    print("=====concatenate====三维数组三个轴===")


#HVstackCon()

def conArray():
    a = np.arange(1,13).reshape(1,2,6)
    print("a:")
    print("a.shape",a.shape)
    print(a)
    b = np.arange(101,113).reshape(1,2,6)
    print("b:")
    print("b.shape", b.shape)
    print(b)
    print("three dimension axis = 0")
    arr01 = np.concatenate((a,b),axis=0)
    print("arr01")
    print("arr01.shape",arr01.shape)
    print(arr01)
    print("three dimension axis = 1")
    arr02 = np.concatenate((a, b), axis=1)
    print("arr02:")
    print("arr02.shape:", arr02.shape)
    print(arr02)
    arr03 = np.concatenate((a, b), axis=2)
    print("arr03:")
    print("arr03.shape:", arr03.shape)
    print(arr03)



conArray()

