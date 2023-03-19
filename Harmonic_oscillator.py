from numpy import arange, sin, pi


import matplotlib.pyplot as plt


class Oscillator():
    '''
    A - Амплитуда колебаний
    fi - начальная фаза колебаний
    w - частота колебаний
    '''
    _count_ = 0
    def __init__(self, A, fi, w, t_start=0, t_stop=10, t_step=0.01):
        self.A = A
        self.fi = fi
        self.w = w
        self.row_x = arange(t_start, t_stop, t_step)
        self.row_y = list(map(lambda t: A * sin(w * t + fi), self.row_x))
        Oscillator._count_ += 1
        self._name_ = f'График: {Oscillator._count_}'

    def plotting(self, color='b'):
        '''
        color - цвет графика
        n - название / номер графика
        '''
        plt.figure(self._name_)
        plt.plot(self.row_x, self.row_y, color)
        plt.suptitle('Гармонический осциллятор')
        plt.title('A = {}; ω = {}; φ = {:.2f};'.format(self.A, self.w, self.fi))
        plt.xlabel('Время')
        plt.ylabel('Смещение точки')
        plt.grid(True)


if __name__ == '__main__':
    
    osc1 = Oscillator(2, 0, 1, 0, 25)
    osc2 = Oscillator(2, pi, 1)
    
    osc1.plotting()
    osc2.plotting('r')
    plt.show()
