from PyQt5 import QtWidgets, QtCore


class LoadingBar(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(LoadingBar, self).__init__(parent)

        # Init loading bar widget
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # Set timer
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        # Set window properties
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.close()
            return

        self.pbar.setValue(self.step)