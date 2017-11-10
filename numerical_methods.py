import random
import numpy as np


class NumericalMethods:

    def __init__(self):
        self.coef_ = np.array([])
        self.x = np.array([])
        self.y = np.array([])

    def get_params(self):
        return self.coef_


class NumericalIntegration(NumericalMethods):

    def __init__(self):
        NumericalMethods.__init__(self)

    def fit(self, x, y):
        self.x = x
        self.y = y

    def trapezium_method(self, func, mim_lim, max_lim, delta):
        def integrate(func, mim_lim, max_lim, n):
            integral = 0.0
            step = (max_lim - mim_lim) / n
            for x in np.arange(mim_lim, max_lim - step, step):
                integral += step * (func(x) + func(x + step)) / 2
            return integral

        d, n = 1, 1
        while np.absolute(d) > delta:
            d = (integrate(func, mim_lim, max_lim, n * 2) - integrate(func, mim_lim, max_lim, n)) / 3
            n *= 2

        print('Rect')
        print(' '.join(['\t',
                        str(n),
                        str(np.absolute(integrate(func, mim_lim, max_lim, n))),
                        str(np.absolute(integrate(func, mim_lim, max_lim, n)) + d)]))

        print('The integral has been calculated.')

    def interpolate(self):
        self.coefs_ = np.array([random.random() for i in range(len(self.x)+1)])


class CauchyProblem(NumericalMethods):

    def __init__(self, x0=None, y0=None, beta=None, T=None):
        NumericalMethods.__init__(self)
        self.x0 = x0
        self.y0 = y0
        self.beta = beta
        self.T = T
        self.U = np.array([])
        self.S = np.array([])
        self.z = np.array([])

    def solve_differential_equation(self):
        print('The differential equation has been calculated.')
        return random.random()
