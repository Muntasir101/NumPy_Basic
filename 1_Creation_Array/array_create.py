import numpy as np

# create array
array = np.arange(6).reshape(2, 3) + 20
print(array)
"""
[[10 11 12]
 [13 14 15]]
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
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
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
