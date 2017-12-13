#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore
import sys


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())


class LoadingBar(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(LoadingBar, self).__init__(parent)

        self.pbar = QtWidgets.QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        # self.btn = QtWidgets.QPushButton('Start', self)
        # self.btn.move(40, 80)
        # self.btn.clicked.connect(self.doAction)

        self.timer = QtCore.QBasicTimer()
        self.step = 0
        self.timer.start(100, self)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.close()
            return

        self.pbar.setValue(self.step)

    def update_timer(self, step):
        self.step = step


class First(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.pushButton = QtWidgets.QPushButton("click me")

        self.setCentralWidget(self.pushButton)

        self.pushButton.clicked.connect(self.button_clicked)
        self.dialog = Second(self)
        self.dialog.hide()

    def button_clicked(self):
        if self.dialog.isHidden():
            self.dialog.show()
        else:
            self.dialog.hide()


if __name__ == '__main__':
    main()