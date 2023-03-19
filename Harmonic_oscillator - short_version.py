from numpy import arange, sin, pi
import matplotlib.pyplot as plt

A, fi, w = 2, 0, 1 # амплитуда / начальная фаза / частота
row_t = arange(0, 20, 0.01)
row_x = list(map(lambda t: A * sin(w * t + fi), row_t))
plt.plot(row_t, row_x, 'r')
plt.grid(True)
plt.show()
