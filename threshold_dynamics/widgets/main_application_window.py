from __future__ import unicode_literals

from PyQt5 import QtGui
from scipy.stats import norm, beta, lognorm, laplace

from threshold_dynamics.numerical_methods import (NumericalIntegration, CubicSplineInterpolation, EulerMethod)
from threshold_dynamics.widgets.canvas import *
from threshold_dynamics.widgets.loading_bar import LoadingBar
from threshold_dynamics.setup import proginfo


class MainApplicationWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainApplicationWindow, self).__init__(parent)

        # Init loading bar
        self.loading = LoadingBar()

        # Set window properties
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("Main Application Window")
        self.setWindowIcon(QtGui.QIcon("/Users/basilminkov/PycharmProjects/NumericalMethodsProjects/static/gr.png"))
        self.loading.step += 10

        # Set menu
        self.file_menu = QtWidgets.QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.file_quit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)
        self.help_menu = QtWidgets.QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.help_menu.addAction('&About', self.about)
        self.loading.step += 10

        # Initialise all used widgets
        # 1. Layouts
        self.main_widget = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        self.buttons = QtWidgets.QHBoxLayout()
        self.loader = QtWidgets.QHBoxLayout()
        self.graphs = QtWidgets.QVBoxLayout()
        self.params1 = QtWidgets.QHBoxLayout()
        self.params2 = QtWidgets.QHBoxLayout()
        self.params3 = QtWidgets.QHBoxLayout()
        self.de_layout = QtWidgets.QHBoxLayout()
        self.intgr_layout = QtWidgets.QHBoxLayout()
        self.de_params = QtWidgets.QHBoxLayout()
        self.loading.step += 10
        # 2. Canvases
        self.set_figure_params()
        self.sc = MyMplCanvas(
            x=figure_params.xgraph1,
            y=figure_params.ygraph1,
            title=r"Distribution of the audience by the probability of hitting the target.",
            xlabel=r'\omega',
            ylabel=r"$\rho(\omega) = PDF(\omega)$",
            pen="r",
        )
        self.dc = MyMplCanvas(
            x=figure_params.xgraph2,
            y=figure_params.ygraph2,
            title=r"Actual Number Of Visits",
            xlabel=r't',
            ylabel=r"$x(t)=a\sin(bt)$",
            pen="g",
        )
        self.mc = MyMplCanvas(
            x=figure_params.xgraph3,
            y=figure_params.ygraph3,
            title=r"Distribution of the audience by the probability of hitting the target.",
            xlabel=r'\omega',
            ylabel=r"$\rho(\omega) = a + \sin(b + \omega)$",
            pen="g",
        )
        self.dbc = MyMplCanvas(
            x=figure_params.xgraph4,
            y=figure_params.ygraph4,
            title=r"Distribution of the audience by the probability of hitting the target.",
            xlabel=r'\omega',
            ylabel=r"$\rho(\omega) = a + \sin(b + \omega)$",
            pen="g",
        )
        self.loading.step += 10
        # 3. Button name
        self.itgr = QtWidgets.QPushButton("Calculate Integral")
        self.intrp = QtWidgets.QPushButton("Interpolate")
        self.sco = QtWidgets.QPushButton("Save Coefficients")
        self.de = QtWidgets.QPushButton("Solve Differential Equation")
        self.sder = QtWidgets.QPushButton("Save Result")
        self.fo = QtWidgets.QPushButton("Get Discrete Set")
        self.b1 = QtWidgets.QPushButton("Months Statistics")
        self.b2 = QtWidgets.QPushButton("Alignment With The Plan")
        self.b3 = QtWidgets.QPushButton("Cauchy Problem")
        self.b4 = QtWidgets.QPushButton("Contour Line")
        self.b5 = QtWidgets.QPushButton("Integration")
        self.ac1 = QtWidgets.QPushButton("Apply Changes")
        self.ac2 = QtWidgets.QPushButton("Apply Changes")
        self.ac3 = QtWidgets.QPushButton("Apply Changes")
        self.us1 = QtWidgets.QPushButton("Use Discrete Set")
        self.us2 = QtWidgets.QPushButton("Use Discrete Set")
        self.us3 = QtWidgets.QPushButton("Use Discrete Set")
        self.ss1 = QtWidgets.QPushButton("Save Discrete Set")
        self.ss2 = QtWidgets.QPushButton("Save Discrete Set")
        self.ss3 = QtWidgets.QPushButton("Save Discrete Set")
        self.loading.step += 10
        # 4. Labels And Line Edits (Inputs)
        # 4.1. Differential Equations System
        self.iv = QtWidgets.QLabel('Answer:')
        self.x0 = QtWidgets.QLabel('x0')
        self.y0 = QtWidgets.QLabel('y0')
        self.beta = QtWidgets.QLabel('Beta')
        self.T = QtWidgets.QLabel('T')
        self.le_x0 = QtWidgets.QLineEdit()
        self.le_y0 = QtWidgets.QLineEdit()
        self.le_beta = QtWidgets.QLineEdit()
        self.le_T = QtWidgets.QLineEdit()
        # 4.2.
        self.l_a = QtWidgets.QLabel('a')
        self.l_b = QtWidgets.QLabel('b')
        self.le_a = QtWidgets.QLineEdit()
        self.le_b = QtWidgets.QLineEdit()
        # 4.3.
        self.l_a2 = QtWidgets.QLabel('a')
        self.l_b2 = QtWidgets.QLabel('b')
        self.le_a2 = QtWidgets.QLineEdit()
        self.le_b2 = QtWidgets.QLineEdit()
        # 4.4.
        self.l_a3 = QtWidgets.QLabel('SNR')
        self.l_b3 = QtWidgets.QLabel('Alpha')
        self.le_a3 = QtWidgets.QLineEdit()
        self.le_b3 = QtWidgets.QLineEdit()
        self.loading.step += 10

        # Assemble widgets to lists
        self.win1obj = [self.l_a, self.le_a, self.l_b, self.le_b, self.sc, self.ac1, self.us1, self.ss1,
                        self.l_a2, self.le_a2, self.l_b2, self.le_b2, self.dc, self.ac2, self.us2, self.ss2]
        self.win2obj = [self.l_a3, self.le_a3, self.l_b3, self.le_b3, self.mc, self.ac3, self.us3, self.ss3]
        self.win3obj = [self.de, self.sder, self.x0, self.y0, self.beta, self.T, self.le_x0, self.le_y0, self.le_beta, self.le_T]
        self.win4obj = [self.dbc]
        self.win5obj = [self.iv, self.itgr, self.intrp, self.sco]
        self.win_obj_list = [self.win1obj, self.win2obj, self.win3obj, self.win4obj, self.win5obj]
        self.loading.step += 10

        # Assemble all layouts
        self.assembling()
        # close all widgets
        for i in self.win_obj_list:
            for j in i:
                j.close()
        self.loading.step += 10

        # Show main window
        self.setCentralWidget(self.main_widget)
        self.resize(1200, 800)
        self.statusBar().showMessage("All hail matplotlib!", 2000)
        self.current_window = None
        self.discrete_set = None
        self.loading.step += 10

        # Set buttons functions
        self.itgr.clicked.connect(self.calculate_integral)
        self.intrp.clicked.connect(self.interpolate)
        self.de.clicked.connect(self.solve_differential_equation)
        self.fo.clicked.connect(self.file_open)
        self.b1.clicked.connect(lambda: self.show_window(0))
        self.b2.clicked.connect(lambda: self.show_window(1))
        self.b3.clicked.connect(lambda: self.show_window(2))
        self.b4.clicked.connect(lambda: self.show_window(3))
        self.b5.clicked.connect(lambda: self.show_window(4))
        self.ac1.clicked.connect(self.apply_change)
        self.ac2.clicked.connect(self.apply_change)
        self.ac3.clicked.connect(self.apply_change)
        self.us1.clicked.connect(lambda: self.use_discrete_set(0))
        self.us2.clicked.connect(lambda: self.use_discrete_set(1))
        self.us3.clicked.connect(lambda: self.use_discrete_set(2))
        self.ss1.clicked.connect(lambda: self.save_discrete_set(0))
        self.ss2.clicked.connect(lambda: self.save_discrete_set(1))
        self.ss3.clicked.connect(lambda: self.save_discrete_set(2))
        self.loading.step += 10

    def assembling(self):

        """Assemble all layouts inside of main layout"""

        # assemble regime top buttons
        self.buttons.addStretch()
        self.buttons.addWidget(self.b1)
        self.buttons.addWidget(self.b2)
        self.buttons.addWidget(self.b3)
        self.buttons.addWidget(self.b4)
        self.buttons.addWidget(self.b5)
        self.buttons.addStretch()

        # assemble top regime buttons (Functions, SNR, )
        self.main_layout.addLayout(self.buttons)
        self.main_layout.addLayout(self.graphs)
        self.main_layout.addLayout(self.intgr_layout)
        self.main_layout.addLayout(self.de_layout)
        self.main_layout.addLayout(self.de_params)
        self.main_layout.addStretch()
        self.main_layout.addLayout(self.loader)

        self.de_params.addWidget(self.x0)
        self.de_params.addWidget(self.le_x0)
        self.de_params.addWidget(self.y0)
        self.de_params.addWidget(self.le_y0)
        self.de_params.addWidget(self.beta)
        self.de_params.addWidget(self.le_beta)
        self.de_params.addWidget(self.T)
        self.de_params.addWidget(self.le_T)
        self.de_params.addStretch()

        self.intgr_layout.addWidget(self.itgr)
        self.intgr_layout.addWidget(self.intrp)
        self.intgr_layout.addWidget(self.sco)
        self.intgr_layout.addWidget(self.iv)
        self.intgr_layout.addStretch()

        self.de_layout.addWidget(self.de)
        self.de_layout.addWidget(self.sder)
        self.de_layout.addStretch()

        # functions regime << first graph params widgets
        self.params1.addStretch()
        self.params1.addWidget(self.l_a)
        self.params1.addWidget(self.le_a)
        self.params1.addWidget(self.l_b)
        self.params1.addWidget(self.le_b)
        self.params1.addWidget(self.ac1)
        self.params1.addWidget(self.us1)
        self.params1.addWidget(self.ss1)
        self.params1.addStretch()

        # functions regime << second graph params widgets
        self.params2.addStretch()
        self.params2.addWidget(self.l_a2)
        self.params2.addWidget(self.le_a2)
        self.params2.addWidget(self.l_b2)
        self.params2.addWidget(self.le_b2)
        self.params2.addWidget(self.ac2)
        self.params2.addWidget(self.us2)
        self.params2.addWidget(self.ss2)
        self.params2.addStretch()

        self.params3.addStretch()
        self.params3.addWidget(self.l_a3)
        self.params3.addWidget(self.le_a3)
        self.params3.addWidget(self.l_b3)
        self.params3.addWidget(self.le_b3)
        self.params3.addWidget(self.ac3)
        self.params3.addWidget(self.us3)
        self.params3.addWidget(self.ss3)
        self.params3.addStretch()

        self.graphs.addWidget(self.sc)
        self.graphs.addLayout(self.params1)
        self.graphs.addWidget(self.dc)
        self.graphs.addLayout(self.params2)
        self.graphs.addWidget(self.mc)
        self.graphs.addLayout(self.params3)
        self.graphs.addWidget(self.dbc)

        self.loader.addWidget(self.fo)
        self.loader.addStretch()

    def show_window(self, n_window):

        """Process buttons clicks for the first graph"""

        if self.current_window is not None:
            self.close_win_obj(self.current_window)
        self.show_win_obj(self.win_obj_list[n_window])
        self.current_window = self.win_obj_list[n_window]

    def use_discrete_set(self, n_graph):

        """"""

        if self.discrete_set is not None:
            figure_params.xgraphs[n_graph] = self.discrete_set
        else:
            self.statusBar().showMessage("No data, bro!", 2000)

    def apply_change(self):

        """Apply changes, if 'Apply changes 1' button is clicked"""

        try:
            if self.current_window == self.win1obj:
                if self.le_a.text() != '':
                    figure_params.a1 = float(self.le_a.text())
                if self.le_b.text() != '':
                    figure_params.b1 = float(self.le_b.text())
                if self.le_a2.text() != '':
                    figure_params.a2 = float(self.le_a2.text())
                if self.le_b2.text() != '':
                    figure_params.b2 = float(self.le_b2.text())
            if self.current_window == self.win2obj:
                if self.le_a3.text() != '':
                    figure_params.a3 = float(self.le_a3.text())
                if self.le_b3.text() != '':
                    figure_params.b3 = float(self.le_b3.text())
        except ValueError:
            self.statusBar().showMessage("Value error, bro!", 2000)

    def file_open(self):

        """"""

        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File')
        self.discrete_set = np.genfromtxt(name[0], delimiter=',')
        sz = self.discrete_set.shape
        if len(sz) == 1:
            self.statusBar().showMessage("Received a {}x{} matrix, bro!".format(sz[0], 1), 2000)
        if len(sz) == 2:
            self.statusBar().showMessage("Received a {}x{} matrix, bro!".format(sz[0], sz[1]), 2000)

    def save_discrete_set(self, n_graph):

        """"""

        np.savetxt("/Users/basilminkov/PycharmProjects/NumericalMethodsProjects/results/graph{}.csv".format(str(n_graph+1)),
                   np.stack((figure_params.xgraphs[n_graph], figure_params.ygraphs[n_graph]), axis=1), delimiter=',')
        self.statusBar().showMessage("Graph{} is saved, bro!".format(str(n_graph+1)), 2000)

    def calculate_integral(self):

        """"""

        ni = NumericalIntegration()
        ni.fit(figure_params.xgraph1, figure_params.ygraph1)
        self.iv.setText(str(ni.calculate_integral()))
        self.statusBar().showMessage("Integral has been calculated, bro!", 2000)

    def interpolate(self):

        """"""

        ni = NumericalIntegration()
        ni.fit(figure_params.xgraph1, figure_params.ygraph1)
        ni.interpolate()
        np.savetxt("/Users/basilminkov/PycharmProjects/NumericalMethodsProjects/results/interpolation_coefs.csv",
                   ni.coefs_, delimiter=',')
        self.statusBar().showMessage("Interpolation has been done and saved to file, bro!", 2000)

    def calculate_integral(self):

        """"""

        ni = NumericalIntegration()
        ni.fit(figure_params.xgraph1, figure_params.ygraph1)
        self.iv.setText(str(ni.calculate_integral()))
        self.statusBar().showMessage("Integral has been calculated, bro!", 2000)

    def solve_differential_equation(self):

        """"""

        de = EulerMethod()
        try:
            if self.le_x0.text() != '':
                de.x0 = float(self.le_x0.text())
            if self.le_y0.text() != '':
                de.y0 = float(self.le_y0.text())
            if self.le_beta.text() != '':
                de.beta = float(self.le_beta.text())
            if self.le_T.text() != '':
                de.T = float(self.le_T.text())
        except ValueError:
            self.statusBar().showMessage("Value error, bro!", 2000)
        ni = NumericalIntegration()
        de.U = ni.calculate_integral()
        de.S = [random.random() for i in range(10)]
        de.z = [random.random() for i in range(10)]
        ni = NumericalIntegration()
        ni.fit(figure_params.xgraph1, figure_params.ygraph1)
        ni.interpolate()
        print(de.solve_differential_equation())
        np.savetxt("/Users/minkov/PycharmProjects/NumericalMethodsProjects/results/CauchyProblemAnswer.csv",
                   [de.solve_differential_equation()])
        self.statusBar().showMessage("Differential equation has been calculated, bro!", 2000)

    @staticmethod
    def set_figure_params():
        signal = figure_params.a2 * np.cos(figure_params.b2 * figure_params.xgraph2) + figure_params.a2
        noise = [random.gauss(0, np.std(signal) / figure_params.a3) for i in
                 range(len(figure_params.xgraph2))]

        figure_params.ygraph1 = norm.pdf(figure_params.xgraph1)
        figure_params.ygraph2 = signal + noise
        figure_params.ygraph3 = figure_params.a3 * np.cos(figure_params.b3 * figure_params.xgraph3) + figure_params.a3
        figure_params.ygraph4 = figure_params.xgraph4

    @staticmethod
    def close_win_obj(win_obj):

        """"""

        for j in win_obj:
            j.close()

    @staticmethod
    def show_win_obj(win_obj):

        """"""

        for j in win_obj:
            j.show()

    @staticmethod
    def clear_layout(layout):

        """"""

        for i in reversed(range(layout.count())):
            layout.removeItem(layout.takeAt(i))

    def about(self):

        """"""

        QtWidgets.QMessageBox.about(self, "About", proginfo)

    def file_quit(self):

        """"""

        self.close()

    def close_event(self):

        """"""

        self.file_quit()
