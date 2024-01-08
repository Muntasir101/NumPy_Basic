import numpy as np

# from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array = np.array(my_list)
print(my_array)  # [ 1  2  3  4  5  6  7  8  9 10]

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

random_array = np.random.rand(3, 4)
print(random_array)
"""
[[0.49673672 0.30506604 0.41849387 0.61079263]
 [0.89739196 0.41328725 0.00851819 0.5818078 ]
 [0.46283097 0.43670351 0.5676634  0.94334153]]
"""

