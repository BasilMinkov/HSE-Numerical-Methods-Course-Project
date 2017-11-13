import numpy as np
from scipy.integrate import quad, trapz
from scipy.signal import square
from numerical_methods import NumericalIntegration
import matplotlib.pyplot as plt
fig_size = [8, 6]  # Sets figure size
plt.rcParams["figure.figsize"] = fig_size


def test_trapezium_method(func):
    """
    
    :param func: 
    :return: 
    """
    Hs = np.linspace(0.01, np.pi, 100)[::-1]
    model = NumericalIntegration()
    Es = []
    Es2 = []
    for h in Hs:
        x = np.arange(0.0, 100.0, h)
        y = func(x)
        Es.append(abs(model.trapezium_method(y, x) - quad(func, x[0], x[-1])[0]))
        Es2.append(abs(model.trapezium_method(y, x) - trapz(y, x)))
    plt.plot(Hs, Es, label="abs(trapezium_method - scipy.integrate.quad)")
    plt.plot(Hs, Es2, label="abs(trapezium_method - scipy.integrate.trapz)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.title(r'$E(h)$ for {} function'.format(func.__name__))
    plt.ylabel(r'$E(h)$')
    plt.xlabel(r'$h$')
    plt.show()


def log_trapezium_error(func):
    """
    
    :param func: 
    :return: 
    """
    Hs = np.linspace(0.01, np.pi, 100)[::-1]
    model = NumericalIntegration()
    Es = []
    Ns = []
    for h in Hs:
        x = np.arange(0.0, 100.0, h)
        y = func(x)
        Es.append(abs(model.trapezium_method(y, x) - quad(func, x[0], x[-1])[0]))
        Ns.append(len(x))
    plt.plot(Ns, Es, label="abs(trapezium_method - scipy.integrate.quad)")
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.xscale("log")
    plt.yscale("log")
    plt.title(r'$logE(N)$ for {} function'.format(func.__name__))
    plt.ylabel(r'$logE(N)$')
    plt.xlabel(r'$log(N)$')
    plt.show()


def test_methods(func_list, test_func):
    """
    The function considers the method error for the set of Hs steps for the selected approximable functions func_list.
    :param func_list: 
    :param test_func: 
    :return: 
    """
    for i in range(len(func_list)):
        test_func(func_list[i])