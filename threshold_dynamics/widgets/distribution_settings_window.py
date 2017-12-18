import sys
from PyQt5 import QtWidgets, QtCore
from scipy.stats import norm, lognorm, laplace, beta

from threshold_dynamics.setup import figure_params


class DistributionSettingWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        self.distribution = "Normal"
        self.mu = 0.5
        self.sigma = 0.1
        self.alpha = 0.5
        self.beta = 0.5

        super(DistributionSettingWindow, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.main_widget = QtWidgets.QWidget(self)
        self.main_layout = QtWidgets.QVBoxLayout(self.main_widget)

        self.lbl = QtWidgets.QLabel("Current Distribution: {}\n"
                                    "Current Expected Value: {}\n"
                                    "Current Dispersion: {}"
                                    "Current Alpha: {}\n"
                                    "Current Beta: {}".format(self.distribution,
                                                              self.mu,
                                                              self.sigma,
                                                              self.alpha,
                                                              self.beta))
        self.info_layout = QtWidgets.QHBoxLayout()
        self.combo_box_layout = QtWidgets.QHBoxLayout()
        self.params_layout = QtWidgets.QHBoxLayout()
        self.apply_button_layout = QtWidgets.QHBoxLayout()

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([
                        "Normal",
                        "Log-normal",
                        "Beta",
                        "Laplace",
                        ])

        self.apply_changes_button = QtWidgets.QPushButton("Apply Changes")

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

        self.apply_changes_button.clicked.connect(self.apply_changes)
        self.combo.activated[str].connect(self.on_activated)

        self.assembling()

        self.setWindowTitle('Distribution Setting Window')
        self.setCentralWidget(self.main_widget)
        self.statusBar().showMessage("Set distribution, please!", 5000)
        self.show()

    def assembling(self):

        self.main_layout.addStretch()
        self.main_layout.addLayout(self.info_layout)
        self.main_layout.addLayout(self.combo_box_layout)
        self.main_layout.addLayout(self.params_layout)
        self.main_layout.addLayout(self.apply_button_layout)
        self.main_layout.addStretch()

        self.info_layout.addStretch()
        self.info_layout.addWidget(self.lbl)
        self.info_layout.addStretch()

        self.combo_box_layout.addStretch()
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

        self.apply_button_layout.addWidget(self.apply_changes_button)
        self.apply_button_layout.addStretch()

        self.close_win_obj(self.params_list[4:])

    def on_activated(self, text):
        if self.distribution != text:
            self.close_win_obj(self.params_list)
            self.distribution = text
            if self.distribution == "Beta":
                for widget in self.params_list[4:]:
                    widget.show()
            else:
                for widget in self.params_list[:4]:
                    widget.show()

    def apply_changes(self):

        if self.mu_line_edit.text() != '':
            figure_params.mu = float(self.mu_line_edit.text())
            self.mu = float(self.mu_line_edit.text())
        if self.sigma_line_edit.text() != '':
            figure_params.sigma = float(self.sigma_line_edit.text())
            self.sigma = float(self.sigma_line_edit.text())
        if self.beta_line_edit.text() != '':
            figure_params.beta = float(self.beta_line_edit.text())
            self.beta = float(self.beta_line_edit.text())
        if self.alpha_line_edit.text() != '':
            figure_params.alpha = float(self.alpha_line_edit.text())
            self.alpha = float(self.alpha_line_edit.text())

        if self.distribution == "Normal":
            figure_params.foo = norm.pdf
        if self.distribution == "Log-normal":
            figure_params.foo = lognorm.pdf
        if self.distribution == "Beta":
            figure_params.foo = beta.pdf
        if self.distribution == "Laplace":
            figure_params.foo = laplace.pdf

        figure_params.set_figure_params()

        self.lbl.setText("Current Distribution: {}\n"
                         "Current Expected Value: {}\n"
                         "Current Dispersion: {}\n"
                         "Current Alpha: {}\n"
                         "Current Beta: {}".format(self.distribution,
                                                   self.mu,
                                                   self.sigma,
                                                   self.alpha,
                                                   self.beta))
        self.lbl.adjustSize()

    @staticmethod
    def close_win_obj(win_obj):
        for j in win_obj:
            j.close()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = DistributionSettingWindow()
    sys.exit(app.exec_())
