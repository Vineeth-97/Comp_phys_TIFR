import numpy as np

A = np.array([[2, 1], [1, 0], [0, 1]])
B = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])
u, s, vh = np.linalg.svd(A)
U, S, VH = np.linalg.svd(B)
print(s)
print(S)
