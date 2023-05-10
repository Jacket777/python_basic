"simple use"
import numpy as np
#create array
arr = np.arange(10)
print(arr)
print(type(arr))

#to list to sqrt
import math
list01 = [3,4,9]
result=[]
for i in list01:
    result.append(math.sqrt(i))
    #print(math.sqrt(i))

# use numpy
print(np.sqrt(arr))


print("============2======array function========================")
#create one dimension array
a = np.array([1,2,3,4])
print(a)
print(type(a))

#create two dimension array
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(b)
print(type(b))

#create three dimension array
c = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(c)
print(type(c))

#array function of dtype use
d = np.array([3,4,5],dtype=float)
print(d)
print(type(d))

#array function of ndimn use
e = np.array([5,6,7],dtype=float,ndmin=3)
print(e)
print(type(e))

print("============3======range function to create array========================")
#range(start,end,step) [start,end)
list01 = list(range(1,10))
print(list01)
list02 = list(range(10))
print(list02)
list03 = list(range(1,10,3))
print(list03)

print("============4======arrange function to create array========================")
list04 = np.arange(1,11)#[1-->10]
print(list04)
list05 = np.arange(1,11,2)
print(list05)
#set dtype
list06 = np.arange(10,20,dtype=float)
print(list06)




