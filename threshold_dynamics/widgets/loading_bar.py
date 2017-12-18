import sys
import time
from PyQt5 import QtWidgets, QtCore


class LoadingBar(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.update = 0

        # Init loading bar widget
        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # # Set timer
        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        # Set window properties
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.close()
            return

        self.step += self.update
        self.update = 0
        self.pbar.setValue(self.step)

    def update_timer(self, steps):
        self.update = steps


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    lb = LoadingBar()
    sys.exit(app.exec_())