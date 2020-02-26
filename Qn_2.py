import numpy as np
A = np.array([[1, 0.67, 0.33], [.45, 1, 0.55], [0.67, 0.33, 1]])
B = np.array([2, 2, 2])

X = np.linalg.solve(A, B)

print(X)
