import numpy as np
import matplotlib.pyplot as plt


def f(x):
    if(x <= 1 and x >= -1):
        return 1
    return 0


xmin = -10.0
xmax = 10.0
N = 256

dx = (xmax - xmin)/(N-1)

x = np.linspace(xmin, xmax, N)
data = [f(i) for i in x]
data = np.pad(data, (0, N), mode='constant', constant_values=(0, 0))

# Fourier transform of convolution of two functions is equal to product of fourier transforms of the two functions
FT = np.fft.fft(data, norm='ortho')
conv = np.fft.ifft(FT*FT, norm='ortho')
conv = dx*np.sqrt(2*N)*conv

x_a = int(N/2)
x_b = int(3*N/2)

f_box = [f(i) for i in x]
plt.plot(x, f_box, 'r', label='Box function')
plt.plot(x, np.real(conv[x_a:x_b]), 'g', label='Convolution')
plt.legend()
plt.title("Convolution of box function with itself")
plt.show()
