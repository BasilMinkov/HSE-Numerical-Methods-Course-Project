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

    def __init__(self, form):
        NumericalMethods.__init__(self)

        if form == 'usual':
            # usual from params
            self.a = np.array([])
            self.b = np.array([])
            self.c = np.array([])
            self.d = np.array([])
            self.form = form
        elif form == 'symmetric':
            # symmetric from params
            self.k = np.array([])
            self.a = np.array([])
            self.b = np.array([])
            self.xc = np.array([])
            self.yc = np.array([])
            self.form = form
        else:
            raise ValueError("Form should be either 'usual' or 'symmetric'.")

    def fit(self, y=None, x=None, size_check=False):
        """
        fit(self, y, x)
        
        Fits the data and gets the interpolation coefficients. 

        :param size_check:
        :param form:
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

        try:
            if self.form == 'usual':
                h = np.array([x[i]-x[i-1] for i in range(1, len(x))])
                ac = np.array([x[i]-x[i-1] for i in range(1, len(x)-1)])
                b = np.array([2*(x[i+2]-x[i]) for i in range(len(x)-2)])
                d = np.array([6*(((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))-((y[i+1]-y[i])/(x[i+1]-x[i])))
                              for i in range(len(x)-2)])

                self.a = h
                self.c = tridiagonal_matrix_algorithm(ac, b, ac, d)
                self.d = [(self.c[i]-self.c[i-1])/(x[i]-x[i-1]) for i in range(1, len(self.c))]
                self.b = [
                    (0.5*(x[i+1]-x[i])*self.c[i+1])-(1/6)*(((x[i+1]-x[i])**2)*self.c[i+1])+((y[i+1]-y[i])/(x[i+1]-x[i]))
                    for i in range(len(self.c)-1)
                ]

            elif self.form == 'symmetric':
                ac = np.array([(1/(x[i+1]-x[i])) for i in range(0, len(x)-1)])  # first and third diagonals
                b = np.array([2/(x[1]-x[0])] + [2 * ((1/(x[i]-x[i-1]))+(1/(x[i+1]-x[i]))) for i in range(1, len(x)-1)] +
                             [2/(x[-1]-x[-2])])  # main diagonal
                d = np.array([3*((y[1]-y[0])/((x[1]-x[0])**2))] +
                             [3*(((y[i+1]-y[i])/((x[i+1]-x[i])**2)) +
                             ((y[i+2]-y[i+1])/((x[i+2]-x[i+1])**2))) for i in range(len(x)-2)] +
                             [3 * ((y[-1] - y[-2]) / ((x[-1] - x[-2]) ** 2))])  # array of d coefficients

                self.k = tridiagonal_matrix_algorithm(ac, b, ac, d)
                self.a = [(self.k[i]*(x[i+1]-x[i])-(y[i+1]-y[i])) for i in range(len(self.k)-1)]
                self.b = [(-self.k[i+1]*(x[i+1]-x[i])+(y[i+1]-y[i])) for i in range(len(self.k)-1)]

        finally:
            if size_check:
                if self.form == 'usual':
                    for i in [h, ac, b, d, self.a, self.c, self.d, self.b]:
                        print(len(i), end=' ')
                    print("\n")
                elif self.form == 'symmetric':
                    print("k x y a b ac b d")
                    for i in [self.k, self.x, self.y, self.a, self.b, ac, b, d]:
                        print(len(i), end=' ')
                    print("\n")

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

        if self.form == 'usual':
            for i in range(2, len(self.x)-1):
                xd = np.arange(self.x[i - 1], self.x[i], h)
                self.xc = np.append(self.xc, xd)
                for j in xd:
                    yd = self.a[i] + self.b[i]*j + self.c[i]*(j**2) + self.d[i]*(j**3)
                    self.yc = np.append(self.yc, yd)
            return self.yc, self.xc

        elif self.form == 'symmetric':
            for i in range(1, len(self.x)):
                xd = np.arange(self.x[i-1], self.x[i], h)
                self.xc = np.append(self.xc, xd)
                for j in xd:
                    t = (j - self.x[i-1])/(self.x[i] - self.x[i-1])
                    yd = ((1-t)*self.y[i-1])+(t*self.y[i])+(t*(1-t)*((self.a[i-1]*(1-t))+(self.b[i-1]*t)))
                    self.yc = np.append(self.yc, yd)
            return self.yc, self.xc


class EulerMethod(NumericalMethods):
    def __init__(self, y=None, x=None, coefs=None, x0=0, y0=None, xf=10, n=100):
        NumericalMethods.__init__(self)
        # differential equation parameters
        self.x0 = x0
        self.xf = xf
        self.y0 = y0
        self.n = n

        self.d = (self.xf - self.x0)/(self.n - 1)
        self.x = np.linspace(self.x0, self.xf, self.self.n)
        self.y = np.zeros([self.n])  # how does it work?

        if coefs is None:
            md = CubicSplineInterpolation()

    def predict(self):
        self.y[0] = self.y0
        for i in range(1, self.n):
            self.y[i] = self.d*()+self.y[i-1]


if __name__ == "__main__":

    import matplotlib.pyplot as plt

    x = np.arange(1, 10, 1)
    y = np.sin(x)

    # h = np.array([x[i] - x[i - 1] for i in range(1, len(x))])

    md = CubicSplineInterpolation(form='symmetric')
    md.fit(y, x, size_check=True)
    # yp, xp = md.predict()

    # plt.plot(x, y)
    # plt.plot(xp, yp)
    # plt.show()
