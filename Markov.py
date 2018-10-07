from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys, re
from classes import Rule

from MainWindow import Ui_MainWindow


class Markov(QMainWindow, Ui_MainWindow):

    symbols = []
    markers = []
    variables = [] 
    rules = []

    def __init__(self, *args, **kwargs):
        super(Markov, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
        self.runBt.clicked.connect(self.run)

    def run(self):
        self.load_attributes()


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
                    else:
                        if re.match("^\w+\:", line):
                            self.create_rule(line)

    
    def create_rule(self, line): #Creates a new Rule() object, entry example: P1:βx → xβ (P1)
        rule = Rule()

        rule.id = line.split(":")[0] #Splits the ID, ID=P1
        line = line.split(":")[1].split("\u2192") #Splits the pattern,  pattern=βx
        rule.pattern = line[0] 
        rule.substitution = line[1].split("(")[0].lstrip() #splits the subs, substitution=xβ

        if re.search("\(\w+\)", line[1]):
            rule.tag = line[1].split("(")[1].replace(')', '') #splits the tag, tag=P1

        if re.search("\.$",line[1]): #Look up if the given rule is final
            rule.isFinal=True

        rules.append(rule)


########## Application Main:
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    markov = Markov()
    sys.exit(app.exec_())