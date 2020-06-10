import numpy as np
import matplotlib.pyplot as plt


def sinc(x):
    if(x == 0):
        return 1
    return np.sin(x)/x


def f_ft(k):
    if(k <= 1 and k >= -1):
        return np.sqrt(np.pi/2)
    else:
        return 0


xmin = -5*np.pi
xmax = 5*np.pi
N = 512
dx = (xmax - xmin)/(N-1)

x = np.linspace(xmin, xmax, N)
data = [sinc(i) for i in x]

FT_x = np.fft.fft(data, norm='ortho')
k = np.fft.fftfreq(N, dx)
k = 2*np.pi*k
factor = np.exp(-1j*k*xmin)

FT_x = dx*np.sqrt(N/(2*np.pi))*factor*FT_x

FT_x = np.fft.fftshift(FT_x)
k = np.fft.fftshift(k)

FT_analytical = [f_ft(i) for i in k]

plt.plot(k, np.real(FT_x), 'r', label='Numerical')
plt.plot(k, FT_analytical, 'b', label='Analytical')

plt.legend()
plt.title("Fourier Transform of sin(x)/x")
plt.show()
