from PyQt4 import QtCore, QtGui
import Markov
# from Markov import Markov_App


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    

    def setupUi(self, MainWindow):

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(802, 632)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 50, 781, 251))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.results = QtGui.QPlainTextEdit(self.centralwidget)
        self.results.setEnabled(False)
        self.results.setGeometry(QtCore.QRect(10, 310, 781, 261))
        self.results.setObjectName(_fromUtf8("results"))
        self.runBt = QtGui.QPushButton(self.centralwidget)
        self.runBt.setGeometry(QtCore.QRect(690, 10, 97, 31))
        self.runBt.setObjectName(_fromUtf8("runBt"))
        self.oneStepBt = QtGui.QPushButton(self.centralwidget)
        self.oneStepBt.setGeometry(QtCore.QRect(580, 10, 97, 31))
        self.oneStepBt.setAutoFillBackground(False)
        self.oneStepBt.setObjectName(_fromUtf8("oneStepBt"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuInput = QtGui.QMenu(self.menubar)
        self.menuInput.setObjectName(_fromUtf8("menuInput"))
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName(_fromUtf8("menuTools"))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSimple_Input = QtGui.QAction(MainWindow)
        self.actionSimple_Input.setObjectName(_fromUtf8("actionSimple_Input"))
        self.actionMultiple_Inputs = QtGui.QAction(MainWindow)
        self.actionMultiple_Inputs.setObjectName(_fromUtf8("actionMultiple_Inputs"))
        self.actionPalette = QtGui.QAction(MainWindow)
        self.actionPalette.setObjectName(_fromUtf8("actionPalette"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuInput.addAction(self.actionSimple_Input)
        self.menuInput.addAction(self.actionMultiple_Inputs)
        self.menuTools.addAction(self.actionPalette)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)

        #FILE Menu Management:
        self.actionOpen.triggered.connect(self.file_open)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#END OF GUI SETUP

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.runBt.setText(_translate("MainWindow", "One Step", None))
        self.oneStepBt.setText(_translate("MainWindow", "Run", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuInput.setTitle(_translate("MainWindow", "Input", None))
        self.menuTools.setTitle(_translate("MainWindow", "Tools", None))
        self.actionNew.setText(_translate("MainWindow", "New", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save", None))
        self.actionSimple_Input.setText(_translate("MainWindow", "Simple Input", None))
        self.actionMultiple_Inputs.setText(_translate("MainWindow", "Multiple Inputs", None))
        self.actionPalette.setText(_translate("MainWindow", "Palette", None))
        

#File Management Actions:

    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self.menuFile)
        file = open(name,'r')

        with file:
            text = file.read()
            self.plainTextEdit.setPlainText(text)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
