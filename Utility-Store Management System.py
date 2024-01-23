import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from LoginPage import Ui_MainWindow


class Window2(QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    SecondPage = QtWidgets.QMainWindow()

    window = Window2()
    window.show()

    sys.exit(app.exec_())