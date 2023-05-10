"ndarray attribute"
import numpy as np
#one dimension array
arr01 = np.array([1,2,3,4])
print(arr01)
#one dimension array
arr02 = np.arange(4,10)
print(arr02)
#two dimension array
arr03 = np.random.randint(4,10,size=(2,3))
print(arr03)
#three dimension array
arr04= np.random.randn(2,3,4)
print(arr04)

print("=======ndim================")
print("ndim:",arr01.ndim,arr03.ndim,arr04.ndim)
print("=======shap================")
print("shap:",arr01.shape,arr02.shape,arr03.shape)
print("=======dtype================")
print("dtype:",arr01.dtype,arr03.dtype,arr04.dtype)
print("=======size================")
print("size:",arr01.size,arr03.size,arr04.size)
print("=======itemsize================")
print("itemsize:",arr01.itemsize,arr03.itemsize,arr04.itemsize)


