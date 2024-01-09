import numpy as np

data = np.array([1, 2, 3, 4, 5])
# create a boolean mask based on a condition
mask = (data > 2)
result = data[mask]
print(result)  # [3 4 5]

# combining multiple conditions
mask2 = (data > 2) & (data < 5)
result2 = data[mask2]
print(result2)  # [3 4]

# updating values based on condition
data[data > 3] = 0
print(data)  # [1 2 3 0 0]
