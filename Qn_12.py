import time
import numpy as np

# Using np.linalg.svd

start_time = time.time()
A = np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]])
print(A)


U, s, VT = np.linalg.svd(A)

S = np.zeros(np.shape(A))
np.fill_diagonal(S, s)

print("U = ", U)
print("S = ", S)
print("VT = ", VT)

print("Time taken for execution  = %s seconds" % (time.time()-start_time))

# Self written code
