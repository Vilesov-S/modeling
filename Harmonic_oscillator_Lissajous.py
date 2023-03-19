from numpy import arange, sin, pi
import matplotlib.pyplot as plt


class Oscillator():
    '''
    A - амплитуда колебаний
    w - частота колебаний
    fi - начальная фаза колебаний
    color - цвет графика
    '''
    _count_ = 0
    def __init__(self, A, w, fi=0, color = 'b', t_start=0, t_stop=10, t_step=0.001):
        self.A = A
        self.w = w
        self.fi = fi
        self.color = color
        self.t = arange(t_start, t_stop, t_step)
        self.x = A * sin(w * self.t + fi)
        Oscillator._count_ += 1
        self._number_ = Oscillator._count_
        self._name_ = f'График: {self._number_}'

    def plotting(self):
        plt.figure(self._name_)
        plt.plot(self.t, self.x, self.color)
        plt.suptitle('Гармонический осциллятор', fontsize=14, fontweight='bold')
        plt.title('A = {}; ω = {}; φ = {:.2f};'.format(self.A, self.w, self.fi))
        plt.xlabel('Время')
        plt.ylabel('Смещение точки')
        plt.grid(True)

    def plotting_some(*args):
        nums = list(map(lambda arg: str(arg._number_), args))
        name = 'График: ' + ', '.join(nums)
        plt.figure(name)
        for arg in args:
            plt.plot(arg.t, arg.x, arg.color)
        plt.legend(nums, loc=2)
        plt.suptitle('Гармонический осциллятор', fontsize=14, fontweight='bold')
        plt.xlabel('Время')
        plt.ylabel('Смещение точки')
        plt.grid(True)

    def lissajous(self, other):
        plt.figure('Lissajous')
        plt.plot(self.x, other.x)
        

if __name__ == '__main__':
    
##    osc1 = Oscillator(2, 1, t_start=0, t_stop=25)
##    osc2 = Oscillator(1, 1.5, pi, 'r')
##    osc3 = Oscillator(3, 2, 1.5 * pi, 'g', 5, 20)
##    
##    osc1.plotting()
##    osc2.plotting()
##    osc3.plotting()
##    Oscillator.plotting_some(osc1, osc2, osc3)
##
##    plt.show()

    o1 = Oscillator(2, 16)
    o2 = Oscillator(2, 17, pi / 2, color='r')
    Oscillator.plotting_some(o1, o2)
    o1.lissajous(o2)
    plt.show()

