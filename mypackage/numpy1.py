# 1-D array
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print("Array at index 2 is",arr[2])
# print("Array at index 3 is",arr[3])

#2D array 
# import numpy as np

# arr = np.array([[1,2,3,4],[5,6,7,8]])
# print(arr)
# print("2nd element at first row is",arr[0,1])
# print("3rd element on second row is",arr[1,2])

#3D array 
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr)
print('Element at 0 dim 2nd row 3rd column is',arr[0,1,2])
print('Element at 1 dim in 2nd row 3rd column is',arr[1,1,2])