import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 5


xmin = -100
xmax = 100
N = 512

dx = (xmax - xmin)/(N-1)

x = np.fft.fftshift(np.linspace(xmin, xmax, N))
data = [f(i) for i in x]

FT_x = np.fft.fft(data, norm='ortho')
k = np.fft.fftfreq(N, dx)
k = 2*np.pi*k
factor = np.exp(-1j*k*xmin)

FT_x = dx*np.sqrt(N/(2*np.pi))*factor*FT_x

plt.plot(k, np.abs(FT_x), 'r-', label='Numerical')
plt.legend()
plt.title("Fourier tranform of a constant function")
plt.show()
