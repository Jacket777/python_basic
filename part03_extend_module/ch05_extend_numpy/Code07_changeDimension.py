"change array dimension"
import numpy as np

def changeDimension():
    a = np.arange(1,25)
    print("======one dimension===========")
    print(a)
    print("======two dimension===========")
    b = a.reshape(4,6)
    print(b)
    print("======three dimension===========")
    c = a.reshape((2,3,4))
    print(c)


#changeDimension()

def changeDim():
    a = np.arange(1,25)
    b = np.reshape(a,(3,8))
    c = np.reshape(a,(2,3,4))
    print("======two dimension=============")
    print(b)
    print("======three dimension=============")
    print(c)
    print("======two --->one=============")
    d = b.reshape(24)
    e = b.reshape(-1)
    print(d)
    print(e)
    print("======ravel=============")
    arr01 = b.ravel()
    print(arr01)
    print("======flatten=============")
    arr02 = b.flatten()
    print(arr02)




changeDim()





