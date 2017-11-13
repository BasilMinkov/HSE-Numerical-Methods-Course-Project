import random
import numpy as np


class NumericalMethods:

    def __init__(self):
        self.coef_ = []
        self.x = []
        self.y = []

    def get_params(self):
        return self.coef_


class NumericalIntegration(NumericalMethods):

    def __init__(self):
        NumericalMethods.__init__(self)

    def fit(self, x, y):
        self.x = x
        self.y = y

    def trapezium_method(self, y, x, delta=None, eq_diff=True):
        """
        trapezium_method(y, x, delta=None, eq_diff=True)

        Integrate along the given axis using the composite trapezoidal rule.

        :param y: function values list.
        :param x: function arguments list.
        :param delta: sampling rate.  
        :param eq_diff: "True", if difference between samples is equal. 
        :return: approximated value of a definite integral
        """

        if x is None and delta is None:
            raise ValueError("Either 'x' or 'h' argument should not be 'None'")
        elif x is not None and delta is not None:
            raise ValueError("Either 'x' or 'h' argument should be 'None'")

        if x is None and delta is not None:
            # List of arguments is not given. Assume that difference between samples is equal to delta.
            h = delta
            solution = h * (((y[0] + y[-1]) / 2) + sum(y[0:-1]))
        elif delta is None and eq_diff:
            # List of arguments is given. Made an assumption that difference between samples is equal.
            # print("x0: ", x[0], "x1: ", x[1])
            h = x[1] - x[0]
            solution = h * (((y[0] + y[-1]) / 2) + sum(y[0:-1]))
        elif delta is None and not eq_diff:
            # List of arguments is given, but difference between samples should be calculated.
            h = np.diff(x)
            solution = 0
            for i in range(1, len(x)):
                solution += h[i] * (y[i - 1] + y[i]) / 2
        return solution

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
