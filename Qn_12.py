import time
import numpy as np


A = np.array([[0, 1, 1], [0, 1, 0], [1, 1, 0], [0, 1, 0], [1, 0, 1]])
print("A = \n",A)

# Using np.linalg.svd
print("Using np.linalg.svd :\n")

start_time = time.time()
U, s, VT = np.linalg.svd(A)

S = np.zeros(np.shape(A))
np.fill_diagonal(S, s)

print("U = ", U)
print("\nS = ", S)
print("\nVT = ", VT)

print("\nTime taken for execution  = %s seconds" % (time.time()-start_time))

# SVD using QR algorithm
print("\nUsing QR Algorithm : \n")
start_time = time.time()

a = np.dot(A,np.transpose(A))
b = np.dot(np.transpose(A),A)

U = np.identity(a.shape[1])
V = np.identity(b.shape[1])

while np.linalg.norm(a - np.diagflat(np.diag(a))) >= 10e-16:
    Q,R = np.linalg.qr(a)
    a = np.dot(R,Q)
    U = np.dot(U,Q)

while np.linalg.norm(b - np.diagflat(np.diag(b))) >= 10e-16:
    Q,R = np.linalg.qr(b)
    b = np.dot(R,Q)
    V = np.dot(V,Q)

S = 0.0*A
for i in range(S.shape[1]):
    S[i][i] = np.sqrt(np.diag(a)[i])

print("U = ", U)
print("\nS = ", S)
print("\nVT = ", np.transpose(V))

print("\nTime taken for execution  = %s seconds" % (time.time()-start_time))