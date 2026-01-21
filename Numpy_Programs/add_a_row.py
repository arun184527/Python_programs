import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
new_row = np.array([[10, 11, 12]])
row_added = np.append(A,  new_row, axis=0)
print(row_added)