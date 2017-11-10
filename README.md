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

### Trapezoidal rule

The trapezoidal rule (also known as the trapezoid rule or trapezium rule) is a technique for approximating the definite integral.
The complete trapezoidal formula in the case of dividing the entire integration interval into segments of the same length _h_:

![trapezoidal rule] (https://latex.codecogs.com/gif.latex?%5Cint_%7Ba%7D%5E%7Bb%7Df%5Cleft%20%28%20x%20%5Cright%20%29dx%5Capprox%20%5Cfrac%7Bb-a%7D%7Bn%7D%5Cleft%20%28%20%5Cfrac%7Bf%28x_%7B0%7D%29&plus;f%28x_%7Bn%7D%29%7D%7B2%7D%20&plus;%5Csum_%7Bi%3D1%7D%5E%7Bn-1%7Df%5Cleft%20%28%20x_%7Bi%7D%20%5Cright%20%29%20%5Cright%20%29)

### [class _CauchyProblem_](/numerical_methods.py)
[The Cauchy problem](https://en.wikipedia.org/wiki/Cauchy_problem) implementation. Inherited from **class _NumericalMethods_**.

### [class _NumericalIntegration_]((/numerical_methods.py))
The integral approximation and interpolation implementation. Inherited from **class _NumericalMethods_**.

## Reference



## Author
- Basil Minkov, Neuroimaging Methods Group, NRU HSE, Moscow, Russia

