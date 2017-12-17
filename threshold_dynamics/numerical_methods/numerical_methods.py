# import matplotlib.pyplot as plt
# import numpy as np
# from . import NumericalMethods, tridiagonal_matrix_algorithm
#
#
# class CubicSplineInterpolation(NumericalMethods):
#
#     def __init__(self, form):
#         NumericalMethods.__init__(self)
#
#         if form == 'usual':
#             # usual from params
#             self.a = np.array([])
#             self.b = np.array([])
#             self.c = np.array([])
#             self.d = np.array([])
#             self.form = form
#         elif form == 'symmetric':
#             # symmetric from params
#             self.k = np.array([])
#             self.a = np.array([])
#             self.b = np.array([])
#             self.xc = np.array([])
#             self.yc = np.array([])
#             self.form = form
#         else:
#             raise ValueError("Form should be either 'usual' or 'symmetric'.")
#
#     def fit(self, y=None, x=None, size_check=False):
#         """
#         fit(self, y, x)
#
#         Fits the data and gets the interpolation coefficients.
#
#         :param size_check:
#         :param form:
#         :param y: function values array
#         :param x: argument values array.
#         :return:
#         """
#
#         self.x = x
#         self.y = y
#
#         if x is None or y is None:
#             raise ValueError("Both argument value array and function value array are needed "
#                              "to process cubic spline interpolation.")
#         elif len(x) != len(y):
#             raise ValueError("Both argument value array and function value array should be of equal length.")
#
#         try:
#             if self.form == 'usual':
#                 h = np.array([x[i]-x[i-1] for i in range(1, len(x))])
#                 ac = np.array([x[i]-x[i-1] for i in range(2, len(x)-2)])
#                 b = np.array([2*(x[i+2]-x[i]) for i in range(len(x)-3)])
#                 d = np.array([6*(((y[i+2]-y[i+1])/(x[i+2]-x[i+1]))-((y[i+1]-y[i])/(x[i+1]-x[i])))
#                               for i in range(len(x)-3)])
#
#                 self.a = y[1:]
#
#                 self.c = np.append(tridiagonal_matrix_algorithm(ac, b, ac, d), 0)
#                 self.c = np.append(0, self.c)
#                 self.d = [(self.c[i]-self.c[i-1])/(x[i]-x[i-1]) for i in range(1, len(self.c))]
#                 self.b = [
#                     (0.5*(x[i+1]-x[i])*self.c[i+1])-(1/6)*(((x[i+1]-x[i])**2)*self.c[i+1])+((y[i+1]-y[i])/(x[i+1]-x[i]))
#                     for i in range(len(x)-1)
#                 ]
#                 self.c = self.c[:-1]
#
#             elif self.form == 'symmetric':
#                 ac = np.array([(1/(x[i+1]-x[i])) for i in range(0, len(x)-1)])  # first and third diagonals
#                 b = np.array([2/(x[1]-x[0])] + [2 * ((1/(x[i]-x[i-1]))+(1/(x[i+1]-x[i]))) for i in range(1, len(x)-1)] +
#                              [2/(x[-1]-x[-2])])  # main diagonal
#                 d = np.array([3*((y[1]-y[0])/((x[1]-x[0])**2))] +
#                              [3*(((y[i+1]-y[i])/((x[i+1]-x[i])**2)) +
#                              ((y[i+2]-y[i+1])/((x[i+2]-x[i+1])**2))) for i in range(len(x)-2)] +
#                              [3 * ((y[-1] - y[-2]) / ((x[-1] - x[-2]) ** 2))])  # array of d coefficients
#
#                 self.k = tridiagonal_matrix_algorithm(ac, b, ac, d)
#                 self.a = [(self.k[i]*(x[i+1]-x[i])-(y[i+1]-y[i])) for i in range(len(self.k)-1)]
#                 self.b = [(-self.k[i+1]*(x[i+1]-x[i])+(y[i+1]-y[i])) for i in range(len(self.k)-1)]
#
#         finally:
#             if size_check:
#                 if self.form == 'usual':
#                     print('h ac b d a c d b')
#                     for i in [h, ac, b, d, self.a, self.c, self.d, self.b]:
#                         print(len(i), end=' ')
#                     print("\n")
#                 elif self.form == 'symmetric':
#                     print("k x y a b ac b d")
#                     for i in [self.k, self.x, self.y, self.a, self.b, ac, b, d]:
#                         print(len(i), end=' ')
#                     print("\n")
#
#     def predict(self, h=0.01):
#         """
#         predict(self, h=0.01)
#
#         :param h: sampling rate.
#         :return: computed array of argument values and function values.
#         """
#
#         self.xc = np.array([])
#         self.yc = np.array([])
#
#         # for i in [self.k, self.x, self.y, self.a, self.b]:
#         #     print(len(i), end=' ')
#
#         if self.form == 'usual':
#             for i in range(1, len(self.x)-1):
#                 xd = np.arange(self.x[i - 1], self.x[i], h)
#                 self.xc = np.append(self.xc, xd)
#                 for j in xd:
#                     yd = self.a[i] + self.b[i]*(j-x[i]) + self.c[i]*((j-x[i])**2) + self.d[i]*((j-x[i])**3)
#                     self.yc = np.append(self.yc, yd)
#             return self.yc, self.xc
#
#         elif self.form == 'symmetric':
#             for i in range(1, len(self.x)):
#                 xd = np.arange(self.x[i-1], self.x[i], h)
#                 self.xc = np.append(self.xc, xd)
#                 for j in xd:
#                     t = (j - self.x[i-1])/(self.x[i] - self.x[i-1])
#                     yd = ((1-t)*self.y[i-1])+(t*self.y[i])+(t*(1-t)*((self.a[i-1]*(1-t))+(self.b[i-1]*t)))
#                     self.yc = np.append(self.yc, yd)
#             return self.yc, self.xc
#
#
# class EulerMethod(NumericalMethods):
#     def __init__(self, foo, foo1=None, order=1, n_eq=1):
#         NumericalMethods.__init__(self)
#         # differential equation parameters
#         self.order = order
#         self.x0 = 0  #
#         self.xf = 0
#         self.y0 = 0
#         self.dy0 = 0
#         self.y01 = 0
#
#         self.n_eq = n_eq
#         self.foo = foo
#         self.foo1 = foo1
#
#         self.n = 0
#         self.d = 0  # delta or step
#
#         self.x = np.array([])  # x array for prediction
#         self.y = np.array([])  # y array for prediction
#         self.dy = np.array([])
#         self.y1 = np.array([])
#
#     def fit(self, x0=0, y0=None, ey0=None, xf=10, n=100, d=None):
#         self.x0 = x0
#         self.xf = xf
#         self.y0 = y0
#         self.dy0 = ey0  # extra param
#         self.y01 = ey0  # extra param
#
#         if n is None and d is None:
#             raise ValueError("Either 'n' or 'd' argument should not be 'None'")
#         elif n is not None and d is not None:
#             raise ValueError("Either 'n' or 'd' argument should be 'None'")
#
#         if d is None:
#             self.n = n
#             self.d = (self.xf - self.x0) / (self.n - 1)
#             self.x = np.linspace(self.x0, self.xf, self.n)
#         else:
#             self.d = d
#             self.x = np.arange(self.x0, self.xf, self.d)
#             self.n = self.x.shape[0]
#
#         self.y = np.zeros([self.n])  # how does it work?
#         self.dy = np.zeros([self.n])
#         self.y1 = np.zeros([self.n])
#
#     def predict(self, prnt=False, plot=False):
#
#         if self.n_eq == 2 and self.order == 1:
#             self.y[0] = self.y0
#             self.y1[0] = self.y01
#             for i in range(1, self.n):
#                 self.y[i] = self.d * (self.foo(self.x[i - 1], self.y[i - 1], self.y1[i - 1])) + self.y[i - 1]
#                 self.y1[i] = self.d * (self.foo1(self.x[i - 1], self.y[i - 1], self.y1[i - 1])) + self.y1[i - 1]
#             if prnt:
#                 for i in range(self.n):
#                     print(self.x[i], self.y[i], self.y1[i])
#             if plot:
#                 plt.plot(self.x, self.y, "o", label=r"$y_1$")
#                 plt.plot(self.x, self.y1, "o", label=r"$y_2$")
#                 plt.xlabel(r"$x$")
#                 plt.xlabel(r"$x$")
#                 plt.ylabel(r"$y$")
#                 plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#                 plt.show()
#             return self.y, self.y1, self.x
#
#         if self.order == 1 and self.n_eq == 1:
#             self.y[0] = self.y0
#             for i in range(1, self.n):
#                 self.y[i] = self.d*(self.foo(self.x[i-1], self.y[i-1]))+self.y[i-1]
#             if prnt:
#                 for i in range(self.n):
#                     print(self.x[i], self.y[i])
#             if plot:
#                 plt.plot(self.x, self.y, "o")
#                 plt.xlabel(r"$x$", label=r"$y$")
#                 plt.ylabel(r"$y$")
#                 plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#                 plt.show()
#             return self.y, self.x
#
#         if self.order == 2:
#             self.y[0] = self.y0
#             self.dy[0] = self.dy0
#             for i in range(1, self.n):
#                 self.y[i] = self.d * self.dy[i - 1] + self.y[i - 1]
#                 self.dy[i] = self.d * (self.foo(self.x[i - 1], self.y[i - 1], self.dy[i - 1])) + self.dy[i - 1]
#             if prnt:
#                 for i in range(self.n):
#                     print(self.x[i], self.y[i], self.dy[i])
#             if plot:
#                 plt.plot(self.x, self.y, "o", label=r"$y$")
#                 plt.plot(self.x, self.dy, "o", label=r"$y'$")
#                 plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#                 plt.xlabel(r"$x$")
#                 plt.ylabel(r"$y$")
#                 plt.show()
#
#             return self.y, self.dy, self.x
#
#
# if __name__ == "__main__":
#
#     def diff_foo(x, y, dy):
#         return 6 * dy - 9 * y + pow(np.e, 3 * x)
#
#     def analytic_foo(x):
#         return x * pow(np.e, 3 * x) + 0.5 * pow(x, 2) * pow(np.e, 3 * x)
#
#     md = EulerMethod(foo=diff_foo)
#
#     x = np.arange(0, 1, 0.01)
#     y = analytic_foo(x)
#     md.fit(x0=0, y0=0, dy0=1, xf=1, n=None, d=0.001)
#     yp, dyp, xp = md.predict()
#
#     plt.plot(x, y, label='analytic')
#     plt.plot(xp, yp, label=r'$y$')
#     plt.plot(xp, dyp, label=r'$dy$')
#     plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
#     plt.show()