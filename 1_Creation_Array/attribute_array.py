import numpy as np

# from list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_array = np.array(my_list)

print(my_array.shape)

# index
print(my_list[0])  # 1

# slice
print(my_list[1:3])  # [2, 3]

# operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

sum_array = array1 + array2
print(sum_array)  # [5 7 9]

subtraction_array = array1 - array2
print(subtraction_array)  # [-3 -3 -3]

product_array = array1 * array2
print(product_array)  # [ 4 10 18]

divide_array = array1 / array2
print(divide_array)  # [0.25 0.4  0.5 ]

# matrix operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
matrix_product = np.dot(matrix1, matrix2)
print(matrix_product)
"""
[[19 22]
 [43 50]]
"""
