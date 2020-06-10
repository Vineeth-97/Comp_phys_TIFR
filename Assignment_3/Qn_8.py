import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def f(x, y):
    return np.exp(-(x*x + y*y))


def FT_f(kx, ky):
    return 0.5*np.exp(-(kx*kx + ky*ky)/4)


xmin = -30.0
xmax = 30.0
N_x = 64
dx = (xmax - xmin)/(N_x-1)

ymin = -30.0
ymax = 30.0
N_y = 64
dy = (ymax - ymin)/(N_y-1)

x = np.linspace(xmin, xmax, N_x)
y = np.linspace(ymin, ymax, N_y)

X, Y = np.meshgrid(x, y)
data = f(X, Y)


FT = np.fft.fft2(data)
k_x = 2*np.pi*np.fft.fftfreq(N_x, dx)
k_y = 2*np.pi*np.fft.fftfreq(N_y, dy)
K_x, K_y = np.meshgrid(k_x, k_y)
factor = np.exp(-1j*K_x*xmin)*np.exp(-1j*K_y*ymin)

FT = dx*dy*factor*FT/(2*np.pi)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(K_x, K_y, np.real(FT), rstride=1,
                cstride=1, cmap='plasma', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Numerical 2dFT of gaussian")

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(K_x, K_y, FT_f(K_x, K_y), rstride=1,
                cstride=1, cmap='plasma', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title("Analytical 2dFT of gaussian")

plt.show()
