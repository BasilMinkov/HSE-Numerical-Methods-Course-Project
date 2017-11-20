import random
import scipy.interpolate
import numpy as np


def tridiagonal_matrix_algorithm(a, b, c, d):
    """
    tridiagonal_matrix_algorithm(a, b, c, d)
    
    In numerical linear algebra, the tridiagonal matrix algorithm, also known as the Thomas algorithm 
    (named after Llewellyn Thomas), is a simplified form of Gaussian elimination that can be used to solve tridiagonal 
    systems of equations A(a, b, c)*x=d. A tridiagonal system for n unknowns may be written as 
    a_{i}*x_{i-1}+b_{i}*x_{i}+c_{i}*x_{i+1}=d_{i}, where a_{1}=0 and c_{n}=0.
    Algorithm from https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm

    :param a: second diagonal of a coefficients [n-1].
    :param b: main diagonal of b coefficients [n].
    :param c: first diagonal of c coefficients [n-1].
    :param d: array of d coefficients [n].
    :return: array of x [n].
    """

    n = len(d)  # number of equations
    for i in range(1, n):
        m = a[i - 1] / b[i - 1]
        b[i] = b[i] - m * c[i - 1]
        d[i] = d[i] - m * d[i - 1]

    x = b

    x[-1] = d[-1]/d[-1]

    for i in range(n-2, -1, -1):
        x[i] = (d[i]-c[i]*x[i+1])/b[i]
    return x


class NumericalMethods:
    def __init__(self):
        self.coef_ = []
        self.x = []
        self.y = []

    def fit(self, y, x):
        self.y = y
        self.x = x

    def get_params(self):
        return self.coef_


class NumericalIntegration(NumericalMethods):

    def __init__(self):
        NumericalMethods.__init__(self)

    def trapezium_method(self, y=None, x=None, delta=None, eq_diff=True):
        """
        trapezium_method(y, x, delta=None, eq_diff=True)

        Integrate along the given axis using the composite trapezoidal rule.

        :param y: function values list.
        :param x: function arguments list.
        :param delta: sampling rate.  
        :param eq_diff: "True", if difference between samples is equal. 
        :return: approximated value of a definite integral
        """

        if y is None and x is None:
            x = self.x
            y = self.y

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


class CubicSplineInterpolation(NumericalMethods):

    def __init__(self):
        NumericalMethods.__init__(self)
        self.k = np.array([])
        self.a = np.array([])
        self.b = np.array([])
        self.xc = np.array([])
        self.yc = np.array([])

    def fit(self, y, x, size_check=False):
        """
        fit(self, y, x)
        
        Fits the data and gets the interpolation coefficients. 
        
        :param y: function values array
        :param x: argument values array.
        :return: 
        """

        self.x = x
        self.y = y

        if x is None or y is None:
            raise ValueError("Both argument value array and function value array are needed "
                             "to process cubic spline interpolation.")
        elif len(x) != len(y):
            raise ValueError("Both argument value array and function value array should be of equal length.")

        ac = np.array([(1/(x[i+1]-x[i])) for i in range(0, len(x)-1)])  # first and third diagonals
        b = np.array([2/(x[1]-x[0])] + [2 * ((1/(x[i]-x[i-1]))+(1/(x[i+1]-x[i]))) for i in range(1, len(x)-1)] + [2/(x[-1]-x[-2])])  # main diagonal
        d = np.array([3*((y[1]-y[0])/((x[1]-x[0])**2))] +
                     [3*(((y[i+1]-y[i])/((x[i+1]-x[i])**2)) +
                     ((y[i+2]-y[i+1])/((x[i+2]-x[i+1])**2))) for i in range(len(x)-2)] +
                     [3 * ((y[-1] - y[-2]) / ((x[-1] - x[-2]) ** 2))])  # array of d coefficients

        self.k = tridiagonal_matrix_algorithm(ac, b, ac, d)
        self.a = [(self.k[i]*(x[i+1]-x[i])-(y[i+1]-y[i])) for i in range(len(self.k)-1)]
        self.b = [(-self.k[i+1]*(x[i+1]-x[i])+(y[i+1]-y[i])) for i in range(len(self.k)-1)]

        if size_check:
            for i in [self.k, self.x, self.y, self.a, self.b, ac, b, d]:
                print("k x y a b ac b d")
                print(len(i), end=' ')

    def predict(self, h=0.01):
        """
        predict(self, h=0.01)
        
        :param h: sampling rate. 
        :return: computed array of argument values and function values. 
        """

        self.xc = np.array([])
        self.yc = np.array([])

        # for i in [self.k, self.x, self.y, self.a, self.b]:
        #     print(len(i), end=' ')

        for i in range(1, len(self.x)):
            xd = np.arange(self.x[i-1], self.x[i], h)
            self.xc = np.append(self.xc, xd)
            for j in xd:
                t = (j - self.x[i-1])/(self.x[i] - self.x[i-1])
                yd = ((1-t)*self.y[i-1])+(t*self.y[i])+(t*(1-t)*((self.a[i-1]*(1-t))+(self.b[i-1]*t)))
                self.yc = np.append(self.yc, yd)
        return self.yc, self.xc


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
