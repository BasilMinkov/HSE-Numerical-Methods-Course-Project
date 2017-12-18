import random
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtWidgets
from threshold_dynamics.setup import figure_params


class MyMplCanvas(FigureCanvas):

    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, x, y, title, xlabel, ylabel, pen, parent=None, width=5, height=4, dpi=100):
        self.x = x
        self.y = y
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.pen = pen

        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        self.axes.set_title(self.title)
        self.axes.set_xlabel(self.xlabel)
        self.axes.set_ylabel(self.ylabel)
        try:
            for i in range(self.x.shape[1]):
                self.axes.plot(self.x[i], self.y[i], self.pen)
        except IndexError:
            self.axes.plot(self.x, self.y, self.pen, label="some stuff")
        self.axes.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    def update_figure(self, x, y, title=None, xlabel=None, ylabel=None, pen=None):
        self.x = x or self.x
        self.y = y or self.y
        self.title = title or self.title
        self.xlabel = xlabel or self.xlabel
        self.ylabel = ylabel or self.ylabel
        self.pen = pen or self.pen

        self.axes.cla()
        self.compute_initial_figure()
        self.draw()


# class MyDynamicMplCanvas(MyMplCanvas):
#
#     """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
#
#     def __init__(self, parent=None, width=5, height=4, dpi=100):
#
#         fig = Figure(figsize=(width, height), dpi=dpi)
#         self.axes = fig.add_subplot(111)
#         self.compute_initial_figure()
#         FigureCanvas.__init__(self, fig)
#         self.setParent(parent)
#         FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
#         FigureCanvas.updateGeometry(self)
#         timer = QtCore.QTimer(self)
#         timer.timeout.connect(self.update_figure)
#         timer.start(1000)
#
#     def update_figure(self):
#         self.axes.cla()
#         self.compute_initial_figure()
#         self.draw()


# class MyStaticMplCanvas(MyMplCanvas):
#
#     """Simple canvas with a sine plot."""
#
#     def __init__(self, *args, **kwargs):
#         MyMplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#
#         figure_params.ygraph1 = figure_params.a1 + np.sin(figure_params.b1 + figure_params.xgraph1)
#         # distribution of the audience by the probability of falling into the target.
#         self.axes.set_title(r"Distribution of the audience by the probability of hitting the target.")
#         self.axes.set_xlabel(r"$\rho(\omega) = a + \sin(b + \omega)$")
#         self.axes.set_ylabel(r"$\rho(\omega)$")
#         self.axes.plot(figure_params.xgraph1, figure_params.ygraph1, 'g')
#
#     def update_figure(self):
#
#         # Build a list of 4 random integers between 0 and 10 (both inclusive)
#         self.axes.cla()
#         self.compute_initial_figure()
#         self.draw()
#
#
# class MyDynamicMplCanvas(MyMplCanvas):
#
#     """A canvas that updates itself every second with a new plot."""
#
#     def __init__(self, *args, **kwargs):
#         MyMplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#
#         figure_params.ygraph2 = figure_params.a2*np.sin(figure_params.b2*figure_params.xgraph2)
#         self.axes.set_title(r"$x(t)=a\sin(bt)$")
#         self.axes.set_ylabel(r"$x(t)$")
#         self.axes.set_xlabel(r"$t$")
#         self.axes.set_xlim(0, 50)
#         self.axes.set_ylim(-1, 1)
#         self.axes.plot(figure_params.xgraph2, figure_params.ygraph2, 'r')
#
#     def update_figure(self):
#
#         self.axes.cla()
#         self.compute_initial_figure()
#         self.draw()
#
#
# class MyStaticMergedMplCanvas(MyMplCanvas):
#
#     """A canvas that updates itself every second with a new plot."""
#
#     def __init__(self, *args, **kwargs):
#         MyMplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         figure_params.ygraph3 = np.sin(figure_params.b3*figure_params.xgraph3)
#         noise = [random.gauss(0, np.std(figure_params.ygraph3)/figure_params.a3) for i in range(len(figure_params.xgraph3))]
#         self.axes.set_title(r"$x(t)=a\sin(bt)$")
#         self.axes.set_xlabel(r"$t$")
#         self.axes.set_ylabel(r"$x(t)$")
#         self.axes.set_xlim(0, 50)
#         self.axes.set_ylim(-1, 1)
#         self.axes.plot(figure_params.xgraph3, figure_params.ygraph3, 'b')
#         self.axes.plot(figure_params.xgraph3, figure_params.ygraph3 + noise, 'y')
#         self.axes.plot(figure_params.xgraph3, noise, 'g')
#         self.axes.set_title(r"$SNR=\frac{\sigma_s^2}{\sigma_n^2}$")
#
#     def update_figure(self):
#         self.axes.cla()
#         self.compute_initial_figure()
#         self.draw()
#
#
# class MyStaticDoubleMplCanvas(MyMplCanvas):
#
#     """A canvas that updates itself every second with a new plot."""
#
#     def __init__(self, *args, **kwargs):
#         MyMplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         figure_params.ygraph4 = 1.1**figure_params.xgraph4
#         figure_params.ygraph5 = 2**figure_params.xgraph4
#         self.axes.set_title(r"$C(\beta_1)$")
#         self.axes.set_xlabel(r"$\beta_1$")
#         self.axes.set_ylabel(r"$C(\beta_1)$")
#         self.axes.set_xlim(0, 20)
#         self.axes.set_ylim(0, 100)
#         self.axes.plot(figure_params.xgraph4, figure_params.ygraph4, 'g')
#         self.axes.plot(figure_params.xgraph5, figure_params.ygraph5, 'b')
#
#     def update_figure(self):
#         self.axes.cla()
#         self.compute_initial_figure()
#         self.draw()