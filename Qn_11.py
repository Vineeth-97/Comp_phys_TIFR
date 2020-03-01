import numpy as np

A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])

# Define an unit initial vector (used random numbers, to make it less probable for it to be orthogonal to the desired eigenvector)
v = np.random.rand(A.shape[1])
v = v/np.linalg.norm(v)

# Iteration until a desired precision is achieved
while True:
    Av = A.dot(v)
    ev = v.dot(Av)

    v_new = Av/np.linalg.norm(Av)
    Av_new = A.dot(v_new)
    ev_new = v_new.dot(Av_new)

    if np.abs((ev - ev_new)/ev) < 0.01:
        break

    v = v_new
    ev = ev_new

print("Dominant Eigenvalue = ", ev_new)
print("Eigenvector = ", v_new)
