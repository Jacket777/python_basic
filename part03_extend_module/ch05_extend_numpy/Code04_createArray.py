"create array by other method"
import numpy as np
#zeros method
def zerosTest():
    a = np.zeros(5)
    print(a)
    #define type
    b = np.zeros((5,),dtype=int)
    print(b)
    #two dimension array
    c = np.zeros((3,4))
    print(c)

#zerosTest()

print("===============================")
#ones
def onesTest():
    a = np.ones(10)
    print(a)
    b = np.ones((2,5),dtype=int)
    print(b)

#onesTest()

#empty
def emptyTest():
    a = np.empty(8)
    print(a)
    b = np.empty((3,4))
    print(b)


#emptyTest()



#linespace 等差数列
def linespaceTest():
    a = np.linspace(1,10,10)
    print(a)
    b = np.linspace(5,20,5,endpoint=True)
    print(b)
    c = np.linspace(5, 20, 5, endpoint=False)
    print(c)


#linespaceTest()

#logspace
def logspaceTest():
    a = np.logspace(0,9,10,base=2)
    print(a)

logspaceTest()






