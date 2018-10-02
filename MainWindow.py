from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#!/usr/bin/python
#  # -*- coding: U+0395 -*-
import os, sys


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1014, 615)

        self.currentFile = ""

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 761, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.resultsField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultsField.setReadOnly(True)
        self.resultsField.setGeometry(QtCore.QRect(10, 270, 761, 261))
        self.resultsField.setObjectName("resultsField")
        self.oneStepBt = QtWidgets.QPushButton(self.centralwidget)
        self.oneStepBt.setGeometry(QtCore.QRect(130, 540, 97, 31))
        self.oneStepBt.setObjectName("oneStepBt")
        self.runBt = QtWidgets.QPushButton(self.centralwidget)
        self.runBt.setGeometry(QtCore.QRect(20, 540, 97, 31))
        self.runBt.setAutoFillBackground(False)
        self.runBt.setObjectName("runBt")
        MainWindow.setCentralWidget(self.centralwidget)
        self.groupPalette = QtWidgets.QGroupBox(self.centralwidget)
        self.groupPalette.setGeometry(QtCore.QRect(790, 10, 211, 271))
        self.groupPalette.setObjectName("groupPalette")
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

        #Palette
        self.alfabtn = QtWidgets.QPushButton(self.groupPalette)
        self.alfabtn.setGeometry(QtCore.QRect(10, 30, 31, 31))
        self.alfabtn.setObjectName("alfabtn")
        self.betabtn = QtWidgets.QPushButton(self.groupPalette)
        self.betabtn.setGeometry(QtCore.QRect(50, 30, 31, 31))
        self.betabtn.setObjectName("betabtn")
        self.gammabtn = QtWidgets.QPushButton(self.groupPalette)
        self.gammabtn.setGeometry(QtCore.QRect(90, 30, 31, 31))
        self.gammabtn.setObjectName("gammabtn")
        self.deltabtn = QtWidgets.QPushButton(self.groupPalette)
        self.deltabtn.setGeometry(QtCore.QRect(130, 30, 31, 31))
        self.deltabtn.setObjectName("deltabtn")
        self.epsilonbtn = QtWidgets.QPushButton(self.groupPalette)
        self.epsilonbtn.setGeometry(QtCore.QRect(170, 30, 31, 31))
        self.epsilonbtn.setObjectName("epsilonbtn")
        self.dsetabtn = QtWidgets.QPushButton(self.groupPalette)
        self.dsetabtn.setGeometry(QtCore.QRect(10, 70, 31, 31))
        self.dsetabtn.setObjectName("dsetabtn")
        self.etabtn = QtWidgets.QPushButton(self.groupPalette)
        self.etabtn.setGeometry(QtCore.QRect(50, 70, 31, 31))
        self.etabtn.setObjectName("etabtn")
        self.thetabtn = QtWidgets.QPushButton(self.groupPalette)
        self.thetabtn.setGeometry(QtCore.QRect(90, 70, 31, 31))
        self.thetabtn.setObjectName("thetabtn")
        self.iotabtn = QtWidgets.QPushButton(self.groupPalette)
        self.iotabtn.setGeometry(QtCore.QRect(130, 70, 31, 31))
        self.iotabtn.setObjectName("iotabtn")
        self.kappabtn = QtWidgets.QPushButton(self.groupPalette)
        self.kappabtn.setGeometry(QtCore.QRect(170, 70, 31, 31))
        self.kappabtn.setObjectName("kappabtn")
        self.lambdaminbtn = QtWidgets.QPushButton(self.groupPalette)
        self.lambdaminbtn.setGeometry(QtCore.QRect(10, 110, 31, 31))
        self.lambdaminbtn.setObjectName("lambdaminbtn")
        self.lambdamaybtn = QtWidgets.QPushButton(self.groupPalette)
        self.lambdamaybtn.setGeometry(QtCore.QRect(50, 110, 31, 31))
        self.lambdamaybtn.setObjectName("lambdamaybtn")
        self.mybtn = QtWidgets.QPushButton(self.groupPalette)
        self.mybtn.setGeometry(QtCore.QRect(90, 110, 31, 31))
        self.mybtn.setObjectName("mybtn")
        self.nybtn = QtWidgets.QPushButton(self.groupPalette)
        self.nybtn.setGeometry(QtCore.QRect(130, 110, 31, 31))
        self.nybtn.setObjectName("nybtn")
        self.xibtn = QtWidgets.QPushButton(self.groupPalette)
        self.xibtn.setGeometry(QtCore.QRect(170, 110, 31, 31))
        self.xibtn.setObjectName("xibtn")
        self.omicronbtn = QtWidgets.QPushButton(self.groupPalette)
        self.omicronbtn.setGeometry(QtCore.QRect(10, 150, 31, 31))
        self.omicronbtn.setObjectName("omicronbtn")
        self.pibtn = QtWidgets.QPushButton(self.groupPalette)
        self.pibtn.setGeometry(QtCore.QRect(50, 150, 31, 31))
        self.pibtn.setObjectName("pibtn")
        self.rhobtn = QtWidgets.QPushButton(self.groupPalette)
        self.rhobtn.setGeometry(QtCore.QRect(90, 150, 31, 31))
        self.rhobtn.setObjectName("rhobtn")
        self.sigmabtn = QtWidgets.QPushButton(self.groupPalette)
        self.sigmabtn.setGeometry(QtCore.QRect(130, 150, 31, 31))
        self.sigmabtn.setObjectName("sigmabtn")
        self.taubtn = QtWidgets.QPushButton(self.groupPalette)
        self.taubtn.setGeometry(QtCore.QRect(170, 150, 31, 31))
        self.taubtn.setObjectName("taubtn")
        self.ypsilonbtn = QtWidgets.QPushButton(self.groupPalette)
        self.ypsilonbtn.setGeometry(QtCore.QRect(10, 190, 31, 31))
        self.ypsilonbtn.setObjectName("ypsilonbtn")
        self.fibtn = QtWidgets.QPushButton(self.groupPalette)
        self.fibtn.setGeometry(QtCore.QRect(50, 190, 31, 31))
        self.fibtn.setObjectName("fibtn")
        self.jibtn = QtWidgets.QPushButton(self.groupPalette)
        self.jibtn.setGeometry(QtCore.QRect(90, 190, 31, 31))
        self.jibtn.setObjectName("jibtn")
        self.psibtn = QtWidgets.QPushButton(self.groupPalette)
        self.psibtn.setGeometry(QtCore.QRect(130, 190, 31, 31))
        self.psibtn.setObjectName("psibtn")
        self.omegabtn = QtWidgets.QPushButton(self.groupPalette)
        self.omegabtn.setGeometry(QtCore.QRect(170, 190, 31, 31))
        self.omegabtn.setObjectName("omegabtn")
        self.arrowbtn = QtWidgets.QPushButton(self.groupPalette)
        self.arrowbtn.setGeometry(QtCore.QRect(60, 230, 89, 25))
        self.arrowbtn.setObjectName("arrowbtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(770, 0, 20, 531))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #FILE Menu Management:
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.actionSaveAs.triggered.connect(self.file_saveAs)
        self.alfabtn.clicked.connect(self.putAlfa)
        self.betabtn.clicked.connect(self.putBeta)
        self.gammabtn.clicked.connect(self.putGamma)
        self.deltabtn.clicked.connect(self.putDelta)
        self.epsilonbtn.clicked.connect(self.putEpsilon)
        self.dsetabtn.clicked.connect(self.putDseta)
        self.etabtn.clicked.connect(self.putEta)
        self.thetabtn.clicked.connect(self.putTheta)
        self.iotabtn.clicked.connect(self.putIota)
        self.kappabtn.clicked.connect(self.putKappa)
        self.lambdaminbtn.clicked.connect(self.putLambdaMin)
        self.lambdamaybtn.clicked.connect(self.putLambdaMay)
        self.mybtn.clicked.connect(self.putMy)
        self.nybtn.clicked.connect(self.putNy)
        self.xibtn.clicked.connect(self.putXi)
        self.omicronbtn.clicked.connect(self.putOmicron)
        self.pibtn.clicked.connect(self.putPi)
        self.rhobtn.clicked.connect(self.putRho)
        self.sigmabtn.clicked.connect(self.putSigma)
        self.taubtn.clicked.connect(self.putTau)
        self.ypsilonbtn.clicked.connect(self.putYpsilon)
        self.fibtn.clicked.connect(self.putFi)
        self.jibtn.clicked.connect(self.putJi)
        self.psibtn.clicked.connect(self.putPsi)
        self.omegabtn.clicked.connect(self.putOmega)
        self.arrowbtn.clicked.connect(self.putArrow)
        
        self.retranslateUi(MainWindow)

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
        self.groupPalette.setTitle(_translate("MainWindow", "Palette"))
        self.alfabtn.setText(_translate("MainWindow", "\u03B1"))
        self.betabtn.setText(_translate("MainWindow", "\u03B2"))
        self.gammabtn.setText(_translate("MainWindow", "\u03B3"))
        self.deltabtn.setText(_translate("MainWindow", "\u03B4"))
        self.epsilonbtn.setText(_translate("MainWindow", "\u03B5"))
        self.dsetabtn.setText(_translate("MainWindow", "\u03B6"))
        self.etabtn.setText(_translate("MainWindow", "\u03B7"))
        self.thetabtn.setText(_translate("MainWindow", "\u03B8"))
        self.iotabtn.setText(_translate("MainWindow", "\u03B9"))
        self.kappabtn.setText(_translate("MainWindow", "\u03BA"))
        self.lambdaminbtn.setText(_translate("MainWindow", "\u03BB"))
        self.lambdamaybtn.setText(_translate("MainWindow", "\u039B"))
        self.mybtn.setText(_translate("MainWindow", "\u03BC"))
        self.nybtn.setText(_translate("MainWindow", "\u03BD"))
        self.xibtn.setText(_translate("MainWindow", "\u03BE"))
        self.omicronbtn.setText(_translate("MainWindow", "\u03BF"))
        self.pibtn.setText(_translate("MainWindow", "\u03C0"))
        self.rhobtn.setText(_translate("MainWindow", "\u03C1"))
        self.sigmabtn.setText(_translate("MainWindow", "\u03C3"))
        self.taubtn.setText(_translate("MainWindow", "\u03C4"))
        self.ypsilonbtn.setText(_translate("MainWindow", "\u03C5"))
        self.fibtn.setText(_translate("MainWindow", "\u03C6"))
        self.jibtn.setText(_translate("MainWindow", "\u03C7"))
        self.psibtn.setText(_translate("MainWindow", "\u03C8"))
        self.omegabtn.setText(_translate("MainWindow", "\u03C9"))
        self.arrowbtn.setText(_translate("MainWindow", "\u2192"))


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

    def putAlfa(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B1")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)
    
    def putBeta(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B2")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putGamma(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B3")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putDelta(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B4")
        cursor.movePosition(cursor.Right, cursor.KeepAnchor,  3)

    def putEpsilon(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B5")

    def putDseta(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B6")

    def putEta(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B7")

    def putTheta(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B8")

    def putIota(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03B9")

    def putKappa(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BA")
    
    def putLambdaMin(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BB")
    
    def putLambdaMay(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u039B")

    def putMy(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BC")
    
    def putNy(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BD")
    
    def putXi(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BE")

    def putOmicron(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03BF")

    def putPi(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C0")

    def putRho(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C1")
    
    def putSigma(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C3")
    
    def putTau(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C4")

    def putYpsilon(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C5")

    def putFi(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C6")
    
    def putJi(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C7")

    def putPsi(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C8")
    
    def putOmega(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u03C9")

    def putArrow(self):
        cursor = self.plainTextEdit.textCursor()
        self.plainTextEdit.insertPlainText("\u2192")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

