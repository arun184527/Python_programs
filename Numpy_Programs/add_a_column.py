import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
new_col = np.array([10, 20, 30])
result = np.insert(A, 1, new_col, axis=1)
print(result)