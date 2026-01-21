import numpy as np
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
X = np.sum(A, axis=1)
Y = np.sum(B, axis=1)
print(X)
print(Y)