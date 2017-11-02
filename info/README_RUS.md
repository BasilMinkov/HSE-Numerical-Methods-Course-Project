# Численые Методы: Русская Документация

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
