import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
row_deleted = np.delete(A, 1, axis=0)
print(row_deleted)