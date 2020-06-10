import numpy as np
import matplotlib.pyplot as plt
import time


def f(x):
    return np.sin(x)/x


def manual_dft(x):
    n = np.size(x)
    dft = np.zeros(n)
    for i in range(n):
        for j in range(n):
            dft[i] = dft[i] + x[i]*np.exp(-1j*2*np.pi*i*j/n)
    return dft/np.sqrt(n)


def numpy_dft(x):
    return np.fft.fft(x)


manual_time = np.zeros(100)
numpy_time = np.zeros(100)
N = np.arange(4, 104)

for n in N:
    x = np.random.randint(100, size=n)

    start_manual = time.time()
    dft_m = manual_dft(x)
    end_manual = time.time()
    manual_time[n-4] = end_manual-start_manual

    start_numpy = time.time()
    dft_n = numpy_dft(x)
    end_numpy = time.time()
    numpy_time[n-4] = end_numpy-start_numpy

plt.plot(N, manual_time, 'b-', label='Manual')
plt.plot(N, numpy_time, 'r-', label='Numpy')

plt.title("Time taken for FT vs Array size")
plt.legend()
plt.show()
