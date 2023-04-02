from numpy import arange, random, sin, pi
import matplotlib.pyplot as plt


class Oscillator():
    '''
    A - амплитуда колебаний
    w - частота колебаний
    fi - начальная фаза колебаний
    color - цвет графика
    add_noise - добавляет к сигналу аддитивный белый шум.
    '''
    _count_ = 0
    def __init__(self, A, w, fi=0, color = 'b', t_start=0, t_stop=10, t_step=0.001, add_noise=False, mu=0, sigma=0.05):
        self.A = A
        self.w = w
        self.fi = fi
        self.color = color
        self.t = arange(t_start, t_stop, t_step)
        self.x = A * sin(w * self.t + fi)
        self.add_noise = add_noise
        if self.add_noise:
            self.mu = mu
            self.sigma = sigma
            self.noise = random.normal(self.mu, self.sigma, self.t.shape[0])
            self.signal_noise = self.x + self.noise
            self.SNR = self.signal_noise.mean() / self.signal_noise.std(ddof=0)
        Oscillator._count_ += 1
        self._number_ = Oscillator._count_
        self._name_ = f'График: {self._number_}'

    def plotting(self):
        plt.figure(self._name_)
        plt.plot(self.t, self.x, self.color)
        if self.add_noise:
            plt.plot(self.t, self.signal_noise, '#ffa500')
            plt.legend(['Чистый сигнал','Сигнал с шумом\nμ={}; σ={}\nSNR={:.10}'.format(self.mu, self.sigma, self.SNR)], loc=2)
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
        

if __name__ == '__main__':
    osc1 = Oscillator(2, 1, 0, color='#000000', t_start=0, t_step=0.1, t_stop=25, add_noise=True, sigma=0.05)
    
    osc1.plotting()
    plt.show()
