"slice to array"
import numpy as np
a = np.arange(10)
print(a)

#index
#postive index to access, [0,length-1]
print("index = 0: ",a[0])
print("index = 5: ",a[5])

#negative index to access,
print("last index: ",a[-1])
print("last three index: ",a[-3])


#slice [start:stop:step]
#positive
print(a[:])
print(a[3:])
print(a[3:5])
print(a[1:7:2])
print("==========negative slice====================")
#negative
print(a[::-1]) #backward
print(a[-5:-2])


print("======shap======")
def shapTest():
    a = np.arange(1,13)
    print(a)
    a = a.reshape(4,3)
    print(a)
    print(a[2]) #第三行
    print(a[1][2]) #第二行第三列

#shapTest()

#slice to row[行进行切片，列进行切片] [start:stop:step,start:stop:step]

print("======slice to row======")
def sliceToRow():
    a = np.arange(1, 13)
    print(a)
    a = a.reshape(4, 3)
    #all row and line
    print(a[:,:])
    #all row and second column
    print(a[:,1])
    # all row and frist and second column
    print(a[:,0:2])
    # even row and all column
    print("even row and all column")
    print(a[::2,:])
    print("even row and first and second column")
    print(a[::2,0:2])
    print("get")


#sliceToRow()

print("======use x,y to get value======")
def getValueByXY():
    a = np.arange(1, 13)
    print(a)
    a = a.reshape(4, 3)
    print(a)
    print("get two row and three column value")
    print(a[1][2])
    print(a[1,2])
    print("get different row and colum")
    print(a[1,2],a[2][0])
    print(np.array([a[1,2],a[2][0]]))
    print("use x,y to get value")
    print(a[(1,2),(2,0)])


#getValueByXY()

print("two dimension array to use negative index")
def negativeIndexInTwoDimArray():
    a = np.arange(1, 13)
    print(a)
    a = a.reshape(4, 3)
    print(a)
    print("last row")
    print(a[-1])
    print("row reverse")
    print(a[::-1])
    print("row and column reverse")
    print(a[::-1,::-1])

negativeIndexInTwoDimArray()









