import numpy as np

#  1D array slicing
my_array = np.array([1, 2, 3, 4, 5])
subset = my_array[1:4]
print(subset)  # [2 3 4]

# slicing with strides
subset2 = my_array[1:5:2]
print(subset2)  # [2 4]

#  2D array slicing
my_array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
subset3 = my_array[0:1, 1:2]
print(subset3)  # [[2]]

three_d_array = np.random.rand(2, 3, 4)
print(three_d_array)
"""
[[[0.70913226 0.93199233 0.30499074 0.04037798]
  [0.41926136 0.86254173 0.36023974 0.97590308]
  [0.57469408 0.55433548 0.52718156 0.26179495]]

 [[0.50094687 0.86780773 0.43746372 0.5073454 ]
  [0.14536212 0.07645489 0.51921743 0.37542837]
  [0.89994936 0.36881458 0.51533843 0.46456318]]]
"""

# ellipsis
subset4 = three_d_array[..., 1]  # access all the elements in second dimension
print(subset4)
"""
[[0.93199233 0.86254173 0.55433548]
 [0.86780773 0.07645489 0.36881458]]
"""

# integer array indexing
my_array2 = np.array([10, 22, 31, 45, 55])
indices = np.array([0, 2, 4])
selected_element = my_array2[indices]
print(selected_element)  # [10 31 55]
