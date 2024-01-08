import numpy as np

# all functions are for one dimension array
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = np.sum(my_array)
print(total_sum)  # 55

average_value = np.average(my_array)
print(average_value)  # 5.5

max_value = np.max(my_array)
print(max_value)  # 10

min_value = np.min(my_array)
print(min_value)  # 1

index_of_max = my_array.index(max_value)
print(index_of_max)  # 5.5

index_of_min = my_array.index(min_value)
print(index_of_min)  # 0


