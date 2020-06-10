import numpy as np
import matplotlib.pyplot as plt
import time

N = 10000
N_bins = 25

start = time.time()
for i in range(100):
    X = np.random.rand(N)
print(time.time() - start)

n1, bins1, patches1 = plt.hist(
    X, N_bins, facecolor='red', density='true', alpha=0.5, label='np.random.rand()')
plt.axhline(y=1, xmin=0, xmax=1, label='Uniform')
plt.title("np.random.rand(); N=10000")
plt.legend()
plt.show()
