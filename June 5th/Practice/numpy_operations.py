import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)

print(arr + 5)
print(arr * 2)

print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(arr.shape) # shows the dimensions


# 2D Array

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr)

#Creates an array filled with zeros. (3,4) means 3 rows and 4 columns.
arr = np.zeros((3,4)) 
print(arr)

# Creates an array filled with ones. (2,3) means 2 rows and 3 columns.
arr = np.ones((2,3))
print(arr)

# Creates an array containing evenly spaced values within a range
arr = np.arange(1,11)
print(arr) #[ 1  2  3  4  5  6  7  8  9 10]

print(np.full((2,3), 7))