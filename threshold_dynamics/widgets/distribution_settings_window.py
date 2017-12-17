import sys
from PyQt5 import QtWidgets, QtCore


class DistributionSettingWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(DistributionSettingWindow, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.main_widget = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)

        self.lbl = QtWidgets.QLabel("Normal")
        self.combo_box_layout = QtWidgets.QHBoxLayout()
        self.params_layout = QtWidgets.QHBoxLayout()

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([
                        "Normal",
                        "Log-normal",
                        "Beta",
                        "Laplace",
                        ])

        self.mu_label = QtWidgets.QLabel('Expected Value')
        self.mu_line_edit = QtWidgets.QLineEdit()
        self.sigma_label = QtWidgets.QLabel('Dispersion')
        self.sigma_line_edit = QtWidgets.QLineEdit()
        self.alpha_label = QtWidgets.QLabel('Alpha')
        self.alpha_line_edit = QtWidgets.QLineEdit()
        self.beta_label = QtWidgets.QLabel('Beta')
        self.beta_line_edit = QtWidgets.QLineEdit()

        self.params_list = [
                       self.mu_label,
                       self.mu_line_edit,
                       self.sigma_label,
                       self.sigma_line_edit,
                       self.alpha_label,
                       self.alpha_line_edit,
                       self.beta_label,
                       self.beta_line_edit
                       ]

        self.close_win_obj(self.params_list)

        self.combo.activated[str].connect(self.onActivated)

        self.assembling()

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.setCentralWidget(self.main_widget)
        self.statusBar().showMessage("All hail matplotlib!", 2000)
        self.show()

    def assembling(self):

        self.main_layout.addStretch()
        self.main_layout.addLayout(self.combo_box_layout)
        self.main_layout.addLayout(self.params_layout)
        self.main_layout.addStretch()

        self.combo_box_layout.addStretch()
        self.combo_box_layout.addWidget(self.lbl)
        self.combo_box_layout.addWidget(self.combo)
        self.combo_box_layout.addStretch()

        self.params_layout.addStretch()
        self.params_layout.addWidget(self.mu_label)
        self.params_layout.addWidget(self.mu_line_edit)
        self.params_layout.addWidget(self.sigma_label)
        self.params_layout.addWidget(self.sigma_line_edit)
        self.params_layout.addWidget(self.alpha_label)
        self.params_layout.addWidget(self.alpha_line_edit)
        self.params_layout.addWidget(self.beta_label)
        self.params_layout.addWidget(self.beta_line_edit)
        self.params_layout.addStretch()

    def onActivated(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()

    @staticmethod
    def close_win_obj(win_obj):
        for j in win_obj:
            j.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = DistributionSettingWindow()
    sys.exit(app.exec_())
