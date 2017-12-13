"""Threshold Dynamics

Notes
-----
This program is a prototype for the socio-demographic advertising server
allowing dynamic setting of the parameters.
"""
from __future__ import division, absolute_import, print_function

import sys

from threshold_dynamics.widgets.canvas import *
from threshold_dynamics.widgets.main_application_window import MainApplicationWindow
from threshold_dynamics.setup import progname, progversion

if __name__ == "__main__":

    qApp = QtWidgets.QApplication(sys.argv)  # Starts Qt application.
    aw = MainApplicationWindow()  # Initialises main application window.
    aw.setWindowTitle("%s %s" % (progname, progversion))  # Sets the window title.
    aw.show()  # Shows the window.
    sys.exit(qApp.exec_())  # Exits the application after a command from MainApplicationWindow class.
