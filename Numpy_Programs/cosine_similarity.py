import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
A = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
print(A)