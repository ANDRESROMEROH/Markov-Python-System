from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys

class Ui_multiInputsDialog(object):
    def setupUi(self, multiInputsDialog):
        multiInputsDialog.setObjectName("multiInputsDialog")
        multiInputsDialog.resize(321, 590)
        multiInputsDialog.setFocusPolicy(QtCore.Qt.NoFocus)
        multiInputsDialog.setSizeGripEnabled(False)
        multiInputsDialog.setModal(False)
        self.listWidget = QtWidgets.QListWidget(multiInputsDialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 300, 514))
        self.listWidget.setObjectName("listWidget")

        self.rows = [] #List for input rows
        
        self.loadInputsBt = QtWidgets.QPushButton(multiInputsDialog)
        self.loadInputsBt.setGeometry(QtCore.QRect(10, 545, 91, 30))
        self.loadInputsBt.setObjectName("loadInputsBt")
        self.runInputsBt = QtWidgets.QPushButton(multiInputsDialog)
        self.runInputsBt.setGeometry(QtCore.QRect(110, 545, 91, 30))
        self.runInputsBt.setObjectName("runInputsBt")
        self.clearInputsBt = QtWidgets.QPushButton(multiInputsDialog)
        self.clearInputsBt.setGeometry(QtCore.QRect(220, 545, 89, 30))
        self.clearInputsBt.setObjectName("clearInputsBt")
        self.line = QtWidgets.QFrame(multiInputsDialog)
        self.line.setGeometry(QtCore.QRect(10, 521, 301, 30))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(multiInputsDialog)
        self.line_2.setGeometry(QtCore.QRect(200, 535, 20, 70))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #EVENTS:
        self.loadInputsBt.clicked.connect(self.file_load)
        self.clearInputsBt.clicked.connect(self.clear_rows)

        self.retranslateUi(multiInputsDialog)
        self.generateRows(self.rows)
        QtCore.QMetaObject.connectSlotsByName(multiInputsDialog)


    def retranslateUi(self, multiInputsDialog):
        _translate = QtCore.QCoreApplication.translate
        multiInputsDialog.setWindowTitle(_translate("multiInputsDialog", "Inputs"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.loadInputsBt.setText(_translate("multiInputsDialog", "Load Inputs"))
        self.runInputsBt.setText(_translate("multiInputsDialog", "Run Inputs"))
        self.clearInputsBt.setText(_translate("multiInputsDialog", "Clear"))


    def generateRows(self, rows): #The app is meant to process a maximum of 30 string entries...

        for i in range(0,30):
            item = QtWidgets.QListWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
            rows.append(item)

        for i in rows:
             self.listWidget.addItem(i)

    
    def file_load(self): #Loads a file and allocate the strings on individual rows
        path = QFileDialog.getOpenFileName()

        if path[0]:
            try:
                file = open(path[0],'r')

                with file:
                    content = file.readlines()
                    content = [x.strip() for x in content] 
                
            except Exception as error:
                raise Exception("There was an error with the file: ".format(error))
            
            for i in range(len(content)):
                self.rows[i].setText(content[i])


    def clear_rows(self):
        for row in self.rows:
            row.setText("")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    multiInputsDialog = QtWidgets.QDialog()
    ui = Ui_multiInputsDialog()
    ui.setupUi(multiInputsDialog)
    multiInputsDialog.show()
    sys.exit(app.exec_())

