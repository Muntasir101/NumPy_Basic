import numpy as np

# single element accessing in 1D array
my_array_1d = np.array([1, 2, 3, 4, 5])
element_1d = my_array_1d[3]
print(element_1d)  # 4

# single element accessing in 2D array
my_array_2d = np.array([[1, 2, 3, 4, 5], [1, 3, 5, 7, 0]])
element_2d = my_array_2d[1, 2]
print(element_2d)  # 5

# single element accessing in 3D array
my_array_3d = np.array([[[1, 2, 3, 4, 5], [1, 3, 5, 7, 0], [10, 30, 50, 70, 100]]])
element_3d = my_array_3d[0, 2, 3]
print(element_3d)  # 70
