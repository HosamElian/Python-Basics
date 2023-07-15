import numpy as np 
import time
import sys
# one type can store  array
# data stored in same locaion
# print(np.__version__)

myList = [1, 2, 3, 4]
myArray = np.array(myList)

print(myList)
print(myArray)

print(type(myList))
print(type(myArray))

print("=" * 50)

# access item
print(myList[0])
print(myArray[0])

print("=" * 50)

d0 = np.array(4) # 0D
d1 = np.array([4, 10]) # 1D
d2 = np.array( [[1, 2], [3, 4]]) # 2D

d3 = np.array([ 
                [[1, 2], [3, 4]],
                [[5, 6], [7, 8]] 
              ]) # 3D

print(d0)
print(d1[0])
print(d2[1][1])
print(d3[0][1][1]) 

print("=" * 50)

# or
print(d1[0])
print(d2[1, 1])
print(d3[0, 1, 1]) 
# or 
print(d3[0, 1, -1]) 

print("=" * 50)

# Get number of dimentions

print(d0.ndim)
print(d1.ndim)
print(d2.ndim)
print(d3.ndim) 

print("=" * 50)

# create custom array
customArray = np.array([1, 2, 3], ndmin=3)

print(customArray)
print(customArray.ndim)

print("=" * 50)

# id() Get memory location
print(id(d1[0]))
print(id(d1[1]))

print("=" * 50)


print("=" * 50)


# create array with items and compare between adding time

# elments = 1_000_000_000
# startTime = time.time()
# myList1 = range(elments)
# myList2 = range(elments)
# for o, t in zip(myArrayOne, myArrayTwo):
#     print(o + t)
# or
# list_result = [(o + t) for o, t in zip(myList1, myList2) ]
# print(f" Time: {time.time() - startTime}")

# startTime = time.time()
# myArrayOne = np.arange(elments)
# myArrayTwo = np.arange(elments)
# array_result = myArrayOne + myArrayTwo
# print(f" Time: {time.time() - startTime}")

print("create array with items and compare between adding time")

print("=" * 50)

# item size and array size

myArray = np.arange(100)
# print(myArray)
print(myArray.itemsize) # item size in byte
print(myArray.size) # array number of items
print(f"Memory Reserved for Array: {myArray.size * myArray.itemsize}") # allcated in memory

myList = range(100)
print(f"Memory Reserved for List: {sys.getsizeof(myList[1]) *len(myList)}") # allcated in memory

print(sys.getsizeof(myList[1]))

print("=" * 50)

# Slicing

myArray = np.array(['a', 'b', 'c', 'd', 'f'])
print(myArray[1:2])
print(myArray[:2])
print(myArray[2:])

print("=" * 50)

my2DArray = np.array([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']])
print(my2DArray[1:, :2])

print("=" * 50)

# get array data type
a = np.array([1, 2])
print(a.dtype)

print("=" * 50)

# Change type 
myArray = np.array([1.4, 4.3, 1.5], dtype=int)
print(type(myArray))
# or
print(myArray.astype('int'))

print("=" * 50)

# min - max - sum

myArray = np.array([20, 30, 50])
print(myArray.min())
print(myArray.max())
print(myArray.sum())

print("=" * 50)

# Ravel: take ndarray => return 1D array
 
myArray = np.array([[1, 2], [3, 4]])
print(myArray.ravel())

print("=" * 50)

### Shape

myArray = np.array([1, 2, 3, 4])
print(myArray.shape) # return (numberOfItemsPerDim, numberOfDim) => (4,)
print("=" * 50)

myArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(myArray.shape) # return (numberOfItemsInDim, numberOfItemInArrayOfDim) => (2,4)
print("=" * 50)

myArray = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
print(myArray.shape) # return (numberOfItemsInDim, numberOfItemInArrayOfDim) => (2, 2 ,4)
print("=" * 50)

# Reshaped 
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

reshapedMyArray = myArray.reshape(2,6)
print(reshapedMyArray)
print(reshapedMyArray.ndim)
print(reshapedMyArray.shape)
print("=" * 50)

reshapedMyArray = myArray.reshape(3,4)
print(reshapedMyArray)
print(reshapedMyArray.ndim)
print(reshapedMyArray.shape)

myArray = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])
# reshapedMyArray = myArray.reshape(16)
# or
reshapedMyArray = myArray.reshape(-1) # all items => 1D
print(reshapedMyArray)
print(reshapedMyArray.ndim)
print(reshapedMyArray.shape)

