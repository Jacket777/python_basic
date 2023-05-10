"create random array"
import numpy as np

#use random to create one dimension array
arr01 = np.random.random(size = 5)
print(arr01)
print(type(arr01))

#use random to create two dimension array
arr02 = np.random.random(size=(3,4))
print(arr02)
print(type(arr02))


#use random to create three dimension array
arr03 = np.random.random(size=(2,3,4))
print(arr03)
print(type(arr03))


#random integer
def randomIntTest():
    #generate 0-5 one dimension array
    arr = np.random.randint(6, size=10)
    print(arr)
    print(type(arr))
    print("====================================")
    #generate 5-10 two dimension array
    arr02 = np.random.randint(5,11,size=(4,3))
    print(arr02)
    print(type(arr02))
    print("====================================")
    # generate 5-10 three dimension array
    arr03 = np.random.randint(5,11,size=(2,4,3))
    print(arr03)
    print(type(arr03))


randomIntTest()

print("======dtype use============")
arr04 = np.random.randint(10,size=5)
print("default dtype",arr04.dtype)
arr05 = np.random.randint(10,size=5,dtype=np.int64);
print("default dtype",arr05.dtype)


print("======标准正态分布============")
def randnTest():
    # one dimension
    arr01 = np.random.randn(4)
    print(arr01)
    arr02 = np.random.randn(2,3)
    print(arr02)
    arr03 = np.random.randn(2,3,4)
    print(arr03)


randnTest()

print("======指定正态分布============")
def noralTest():
    arr01 = np.random.normal(size=5)#default loc=0.0 scale=1.0
    print(arr01)
    arr02 = np.random.normal(loc=2,scale=3,size=(3,4))
    print(arr02)

noralTest()
