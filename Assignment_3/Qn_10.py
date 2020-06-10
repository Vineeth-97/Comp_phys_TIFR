import numpy as np
import matplotlib.pyplot as plt

f = open("noise.txt", "r").read().split('\n')

data = []
for x in f:
    data.append(float(x))

X = np.array(data)
N = X.size

FT_x = np.fft.fft(X)
Ps = (1/N)*np.abs(FT_x)**2
k = 2*np.pi*np.fft.fftfreq(N, 1)

k_bins = 10
kmax = np.amax(k)
kmin = np.amin(k)
dk = (kmax - kmin)/(k_bins)

idx = np.argsort(k)

plt.plot(k[idx], Ps[idx], 'b', label='Unbinned')
plt.legend()
plt.title("Power Spectrum")
plt.show()

plt.figure(figsize=(16, 4))
plt.plot(X)
plt.title("Data")
plt.show()
plt.figure(figsize=(16, 4))
plt.plot(FT_x)
plt.title("Fourier Transform")
plt.show()
