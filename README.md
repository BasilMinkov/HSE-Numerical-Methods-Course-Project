# Numerical Methods Project

## English Documentation

### class _ApplicationWindow_
Displays one of the five operating modes. Passes and updates function parameters. Made with [_PyQt5_](https://pypi.python.org/pypi/PyQt5).

#### Integration
The integral approximation and interpolation mode.

#### Functions
 _ρ(ω)_, _x(t)_ plot mode.

#### SNR
 _x(t)_, _S(t)_, _x(t)-S(t)_ as signal-to-noise (SNR) ratio plot mode.

#### Cauchy Problem
Numerical solution of [the Cauchy problem](https://en.wikipedia.org/wiki/Cauchy_problem) mode.

#### Contour Line
Contour line plot mode.

### class _MyMplCanvas_
Implementation of graph plotting with [_matplotlib_](https://matplotlib.org/) backend.

### class Params
Class instances – discrete set and function parameters.

### class _NumericalMethods_
Numerical methods implementation with [_scipy_](https://www.scipy.org/) и [_numpy_](http://www.numpy.org/).

#### class _CauchyProblem_
##### Inherited from NumericalMethods
[The Cauchy problem](https://en.wikipedia.org/wiki/Cauchy_problem) implementation.

#### class _NumericalIntegration_
##### Inherited from NumericalMethods
The integral approximation and interpolation implementation.

## Русская документация

![alt text](https://github.com/BasilMinkov/NumericalMethodsProject/blob/master/static/NumericalMethodsProjects.jpg)

### class _ApplicationWindow_
Отображает  один из пяти режимов работы программы. Реализовано на [_PyQt5_](https://pypi.python.org/pypi/PyQt5). Передает и изменяет функций параметры.

#### Integration
Режим, в котором реализовано нахождение приближенного значения интеграла и интерполяция.

#### Functions
Режим, в котором реализовано изображение основных функций _ρ(ω)_, _x(t)_.

#### SNR
Режим, в котором реализовано изображение функций _x(t)_, _S(t)_, _x(t)-S(t)_ на примере SNR (отношение сигнал-шум).

#### Cauchy Problem
Режим, в котором реализовано численное решение задачи Коши.

#### Contour Line
Режим, в котором реализовано изображение линий уровня.

### class _MyMplCanvas_
Класс, который реализует изображение графиков с помощью пакета [_matplotlib_](https://matplotlib.org/).

### class Params
Экземпляры  класса – данные о интерполяционных сектах и коэффиценты функций.

### class NumericalMethods
Класс, в котором реализованы численные методы с помощью пакетов [_scipy_](https://www.scipy.org/) и [_numpy_](http://www.numpy.org/).

### class CauchyProblem
Класс, в котором реализовано решение [задачи Коши] (https://en.wikipedia.org/wiki/Cauchy_problem).

### class NumericalIntegration
Класс, в которм реализовано численное интегрирование и нахождение приближенного значения интеграла.