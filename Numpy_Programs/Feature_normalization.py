import numpy as np
X = np.array([10, 20, 30])
A = (X - X.mean()) / X.std()
print(A)