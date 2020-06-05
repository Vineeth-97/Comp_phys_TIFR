import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0, 1.0, 1024)

plt.plot(x)
plt.xlabel('Sample')
plt.ylabel('Value')
plt.title('Uniform distribution of Random Numbers')
plt.show()

Fs = 1/1024
ps = np.abs(np.fft.fft(x))**2
freqs = np.fft.fftfreq(x.size, Fs)
k = 2*np.pi*freqs
idx = np.argsort(k)

plt.plot(k[idx], ps[idx])
plt.show()

print(k.max(), k.min())
