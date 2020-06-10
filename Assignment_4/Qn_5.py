import numpy as np
import matplotlib.pyplot as plt


def gauss(x):
    return np.sqrt(1/(2*np.pi))*np.exp(-x**2/2)


N = 10000
N_bins = 25
x = np.linspace(-10, 10, 100)

x1 = np.random.rand(N)
x2 = np.random.rand(N)
y = np.sqrt(-2*np.log(x1)) * np.cos(2*np.pi*x2)

n, bins, patches = plt.hist(
    y, N_bins, facecolor='red', density='true', alpha=0.5, label='Sample')
plt.plot(x, gauss(x), 'b', label='Gaussian PDF')
plt.axvline(y.mean(), color='k', linestyle='dashed', linewidth=1)
min_ylim, max_ylim = plt.ylim()
plt.text(y.mean()*1.1, max_ylim*0.9, 'Mean: {:.2f}'.format(y.mean()))
plt.title("Box-Muller")
plt.legend()
plt.show()
