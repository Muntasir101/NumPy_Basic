import numpy as np

# create array
array = np.arange(6).reshape(2, 3) + 20
print(array)
"""
[[20 21 22]
 [23 24 25]]
"""

print(np.argmax(array))  # 5
print(np.argmin(array))  # 0

# from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array = np.array(my_list)
print(my_array)  # [ 1  2  3  4  5  6  7  8  9 10]

range_array = np.arange(0, 10, 2)
print(range_array)  # [0 2 4 6 8]

linspace_array = np.linspace(0, 1, 5)
print(linspace_array)  # [0.   0.25 0.5  0.75 1.  ]

# from function
zeros_array = np.zeros((3, 4))
print(zeros_array)
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

ones_array = np.ones((3, 4))
print(ones_array)
"""
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
"""

# array manipulation
reshaped_array = ones_array.reshape((4, 3))
print(reshaped_array)
"""
[[1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]
 [1. 1. 1.]]
"""
resize_array = np.resize(ones_array, (2, 6))
print(resize_array)
"""
[[1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1.]]
"""

flattened_array = reshaped_array.flatten()
print(flattened_array)  # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

random_array = np.random.rand(3, 4)
print(random_array)
"""
[[0.49673672 0.30506604 0.41849387 0.61079263]
 [0.89739196 0.41328725 0.00851819 0.5818078 ]
 [0.46283097 0.43670351 0.5676634  0.94334153]]
"""

# create 3-D array with random data
array_3d = np.random.randint(0, 10, size=(1, 2, 3))
print(array_3d)
"""
[[[3 6 2]
  [6 5 4]]]
"""

# create 3-D array with random data
array_3d = np.random.randint(0, 10, size=(2, 4, 5))
print(array_3d)
"""
[[[3 9 4 8 8]
  [0 8 7 0 2]
  [4 1 9 2 2]
  [1 6 0 8 3]]

 [[4 4 6 3 2]
  [5 6 4 5 4]
  [2 7 2 1 6]
  [7 0 1 2 4]]]
"""

# create 3-D array with random data
array_3d = np.random.randint(0, 10, size=(3, 4, 5))
print(array_3d)
"""
[[[4 9 6 2 2]
  [3 3 0 2 9]
  [6 4 5 7 6]
  [0 7 7 0 5]]

 [[6 5 1 5 8]
  [2 4 0 9 2]
  [8 3 8 2 0]
  [7 7 1 3 0]]

 [[7 2 3 4 9]
  [8 1 2 5 4]
  [2 1 6 7 8]
  [6 3 4 4 8]]]

"""
