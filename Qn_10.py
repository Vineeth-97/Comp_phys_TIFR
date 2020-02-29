import numpy as np

A = np.array([[5, -2], [-2, 8]])
print("A = ", A)
q, r = np.linalg.qr(A)
print("Q = ", q)
print("R = ", r)

# iterating QR decomposition for 20 times to get eigenvalues
for i in range(20):
    q, r = np.linalg.qr(A)
    A = np.matmul(r, q)

print("diagonal(A%d) = " % (i+1), np.diagonal(A))


print("Eigenvalues = ", np.linalg.eigvals(A))
