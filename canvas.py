import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from params import *
from main import figure_params


class MyMplCanvas(FigureCanvas):

    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        pass


class MyStaticMplCanvas(MyMplCanvas):

    """Simple canvas with a sine plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):

        figure_params.ygraph1 = figure_params.a1 + np.sin(figure_params.b1 + figure_params.xgraph1)
        self.axes.set_title(r"$\rho(\omega) = a + \sin(b + \omega)$")
        self.axes.set_xlabel(r"$\omega$")
        self.axes.set_ylabel(r"$\rho(\omega)$")
        self.axes.set_xlim(0, 50)
        self.axes.set_ylim(-1, 1)
        self.axes.plot(figure_params.xgraph1, figure_params.ygraph1, 'g')

    def update_figure(self):

        # Build a list of 4 random integers between 0 and 10 (both inclusive)
        self.axes.cla()
        self.compute_initial_figure()
        self.draw()


class MyDynamicMplCanvas(MyMplCanvas):

    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):

        figure_params.ygraph2 = figure_params.a2*np.sin(figure_params.b2*figure_params.xgraph2)
        self.axes.set_title(r"$x(t)=a\sin(bt)$")
        self.axes.set_ylabel(r"$x(t)$")
        self.axes.set_xlabel(r"$t$")
        self.axes.set_xlim(0, 50)
        self.axes.set_ylim(-1, 1)
        self.axes.plot(figure_params.xgraph2, figure_params.ygraph2, 'r')

    def update_figure(self):

        self.axes.cla()
        self.compute_initial_figure()
        self.draw()


class MyStaticMergedMplCanvas(MyMplCanvas):

    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        figure_params.ygraph3 = np.sin(figure_params.b3*figure_params.xgraph3)
        noise = [random.gauss(0, np.std(figure_params.ygraph3)/figure_params.a3) for i in range(len(figure_params.xgraph3))]
        self.axes.set_title(r"$x(t)=a\sin(bt)$")
        self.axes.set_xlabel(r"$t$")
        self.axes.set_ylabel(r"$x(t)$")
        self.axes.set_xlim(0, 50)
        self.axes.set_ylim(-1, 1)
        self.axes.plot(figure_params.xgraph3, figure_params.ygraph3, 'b')
        self.axes.plot(figure_params.xgraph3, figure_params.ygraph3 + noise, 'y')
        self.axes.plot(figure_params.xgraph3, noise, 'g')
        self.axes.set_title(r"$SNR=\frac{\sigma_s^2}{\sigma_n^2}$")

    def update_figure(self):
        self.axes.cla()
        self.compute_initial_figure()
        self.draw()


class MyStaticDoubleMplCanvas(MyMplCanvas):

    """A canvas that updates itself every second with a new plot."""

    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        figure_params.ygraph4 = 1.1**figure_params.xgraph4
        figure_params.ygraph5 = 2**figure_params.xgraph4
        self.axes.set_title(r"$C(\beta_1)$")
        self.axes.set_xlabel(r"$\beta_1$")
        self.axes.set_ylabel(r"$C(\beta_1)$")
        self.axes.set_xlim(0, 20)
        self.axes.set_ylim(0, 100)
        self.axes.plot(figure_params.xgraph4, figure_params.ygraph4, 'g')
        self.axes.plot(figure_params.xgraph5, figure_params.ygraph5, 'b')

    def update_figure(self):
        self.axes.cla()
        self.compute_initial_figure()
        self.draw()