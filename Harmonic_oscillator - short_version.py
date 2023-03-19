from numpy import arange, sin, pi
import matplotlib.pyplot as plt

A, w, fi = 2, 1, 0 # амплитуда / начальная фаза / частота
t = arange(0, 20, 0.01)
x = A * sin(w * t + fi)
plt.plot(t, x, 'r')
plt.grid(True)
plt.show()
