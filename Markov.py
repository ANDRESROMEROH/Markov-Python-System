from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys

from MainWindow import Ui_MainWindow


class Markov(QMainWindow, Ui_MainWindow):

    symbols = []
    markers = []
    variables = []

    def __init__(self, *args, **kwargs):
        super(Markov, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.runBt.clicked.connect(self.test)

    def test(self):
        text = str(self.plainTextEdit.toPlainText())
        lines = text.splitlines()
        print(lines[0].partition(" ")[2].lstrip())




########## Application Main:
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    markov = Markov()
    sys.exit(app.exec_())