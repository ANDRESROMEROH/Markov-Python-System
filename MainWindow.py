from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 632)

        self.currentFile = ""

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 781, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.resultsField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultsField.setEnabled(False)
        self.resultsField.setGeometry(QtCore.QRect(10, 310, 781, 261))
        self.resultsField.setObjectName("resultsField")
        self.oneStepBt = QtWidgets.QPushButton(self.centralwidget)
        self.oneStepBt.setGeometry(QtCore.QRect(690, 10, 97, 31))
        self.oneStepBt.setObjectName("oneStepBt")
        self.runBt = QtWidgets.QPushButton(self.centralwidget)
        self.runBt.setGeometry(QtCore.QRect(580, 10, 97, 31))
        self.runBt.setAutoFillBackground(False)
        self.runBt.setObjectName("runBt")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuInput = QtWidgets.QMenu(self.menubar)
        self.menuInput.setObjectName("menuInput")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionSimple_Input = QtWidgets.QAction(MainWindow)
        self.actionSimple_Input.setObjectName("actionSimple_Input")
        self.actionMultiple_Inputs = QtWidgets.QAction(MainWindow)
        self.actionMultiple_Inputs.setObjectName("actionMultiple_Inputs")
        self.actionPalette = QtWidgets.QAction(MainWindow)
        self.actionPalette.setObjectName("actionPalette")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs) 
        self.menuInput.addAction(self.actionSimple_Input)
        self.menuInput.addAction(self.actionMultiple_Inputs)
        self.menuTools.addAction(self.actionPalette)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        #FILE Menu Management:
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.actionSaveAs.triggered.connect(self.file_saveAs)
        

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.mainWindow = MainWindow


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Untitled"))
        self.oneStepBt.setText(_translate("MainWindow", "One Step"))
        self.runBt.setText(_translate("MainWindow", "Run"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionSimple_Input.setText(_translate("MainWindow", "Simple Input"))
        self.actionMultiple_Inputs.setText(_translate("MainWindow", "Multiple Inputs"))
        self.actionPalette.setText(_translate("MainWindow", "Palette"))


    #File Management Actions:

    def file_open(self):
        path = QFileDialog.getOpenFileName()

        if path[0]:
            try:
                file = open(path[0],'r')

                with file:
                    text = file.read()
                    self.plainTextEdit.setPlainText(text)
                
            except Exception as error:
                raise Exception("There was an error with the file: ".format(error))
            
            self.currentFile = path[0]
            self.mainWindow.setWindowTitle(file.name.split("/")[-1])


    def file_saveAs(self):
        information = self.plainTextEdit.toPlainText()
        
        if information:

            path = QFileDialog.getSaveFileName(self.menuFile, 'Save As', os.getenv('HOME'), 'TXT(*.txt)')
            
            try:
                file = open(path[0], 'w')

                with file:    
                    file.write(information)

            except Exception as error:
                raise Exception("There was an error saving the file: ".format(error))

            self.currentFile = path[0]
            self.mainWindow.setWindowTitle(file.name.split("/")[-1])
        
        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty file")
            msg.setInformativeText("Please type something before saving")
            msg.setWindowTitle("We are sorry!")
            msg.exec_()


    def file_save(self):
        information = self.plainTextEdit.toPlainText()

        try:
            file = open(self.currentFile, 'w')

            with file:    
                file.write(information)

        except Exception as error:
            raise Exception("There was an error saving the file: ".format(error))

    
    def file_new(self):
        self.plainTextEdit.clear()
        self.currentFile = ""
        self.mainWindow.setWindowTitle("Untitled")

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

