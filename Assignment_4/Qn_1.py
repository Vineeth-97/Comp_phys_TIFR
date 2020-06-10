import numpy as np
import matplotlib.pyplot as plt
import time

N = 10000
N_bins = 25
X = np.zeros(N)

a = 1542187
c = 10548952321
m = 2**(32)
X[0] = 1

start = time.time()
for i in range(N-1):
    X[i+1] = (a*X[i] + c) % m

X = X/m
print(time.time() - start)
X_uniform = np.random.random(N)


n, bins, patches = plt.hist(
    X, N_bins, facecolor='red', density='true', alpha=0.5, label='LCG')
plt.axhline(y=1, xmin=0, xmax=1, hold=None, label='Uniform Distribution')
plt.title("Linear Congruential Generator; n=10000")
plt.legend()
plt.show()
