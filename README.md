# Numerical Methods Project [:ru:](/info/README_RUS.md)

## Flowchart

![alt text](https://github.com/BasilMinkov/NumericalMethodsProject/blob/master/static/NumericalMethodsProjects_eng.jpg)

## [class _ApplicationWindow_](/main.py)
Displays one of the five operating modes. Passes and updates function parameters. Made with [_PyQt5_](https://pypi.python.org/pypi/PyQt5).

### Integration
The integral approximation and interpolation mode.

### Functions
 _ρ(ω)_, _x(t)_ plot mode.

### SNR
_x(t)_, _S(t)_, _x(t)-S(t)_ as [signal-to-noise (SNR)](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) ratio plot mode.

### Cauchy Problem
Numerical solution of [the Cauchy problem](https://en.wikipedia.org/wiki/Cauchy_problem) mode.

### Contour Line
Contour line plot mode.

## [class _MyMplCanvas_](/canvas.py)
Implementation of graph plotting with [_matplotlib_](https://matplotlib.org/) backend.

## [class _Params_](/params.py)
Class instances – discrete set and function parameters.

## [class _NumericalMethods_](/numerical_methods.py)
Numerical methods implementation with [_scipy_](https://www.scipy.org/) и [_numpy_](http://www.numpy.org/).

### [class _CauchyProblem_](/numerical_methods.py)
[The Cauchy problem](https://en.wikipedia.org/wiki/Cauchy_problem) implementation. Inherited from **class _NumericalMethods_**.

### [class _NumericalIntegration_]((/numerical_methods.py))
The integral approximation and interpolation implementation. Inherited from **class _NumericalMethods_**.

## Author
- Basil Minkov, Neuroimaging Methods Group, NRU HSE, Moscow, Russia