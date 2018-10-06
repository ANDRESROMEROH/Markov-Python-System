from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys, re

from MainWindow import Ui_MainWindow


class Markov(QMainWindow, Ui_MainWindow):


    symbols = []
    markers = []
    variables = []


    def __init__(self, *args, **kwargs):
        super(Markov, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.runBt.clicked.connect(self.load_attributes)


    def load_attributes(self):
        lines = str(self.plainTextEdit.toPlainText()).splitlines()


        for line in lines:
            if re.match("#symbols", line):
                symbols = re.sub("^\#symbols", "", line).lstrip()
            else:
                if re.match("#vars", line):
                    variables = re.sub("^\#vars", "", line).lstrip()
                else:
                    if re.match("#markers", line):
                        markers = re.sub("^\#markers", "", line).lstrip()




########## Application Main:
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    markov = Markov()
    sys.exit(app.exec_())