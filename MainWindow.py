from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
#!/usr/bin/python
#  # -*- coding: U+0395 -*-
import os, sys, codecs
from InputsGui import Ui_multiInputsDialog

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1014, 605)

        self.currentFile = ""

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 761, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.resultsField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.resultsField.setReadOnly(True)
        self.resultsField.setGeometry(QtCore.QRect(10, 310, 761, 251))
        self.resultsField.setObjectName("resultsField")
        self.InputgroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.InputgroupBox.setGeometry(QtCore.QRect(790, 290, 211, 121))
        self.InputgroupBox.setObjectName("InputgroupBox")
        self.stringInput = QtWidgets.QLineEdit(self.InputgroupBox)
        self.stringInput.setGeometry(QtCore.QRect(10, 30, 191, 25))
        self.stringInput.setObjectName("stringInput")
        self.oneStepBt = QtWidgets.QPushButton(self.InputgroupBox)
        self.oneStepBt.setGeometry(QtCore.QRect(110, 80, 91, 21))
        self.oneStepBt.setObjectName("oneStepBt")
        self.runBt = QtWidgets.QPushButton(self.InputgroupBox)
        self.runBt.setGeometry(QtCore.QRect(10, 80, 91, 21))
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
        self.actionMultiple_Inputs = QtWidgets.QAction(MainWindow)
        self.actionMultiple_Inputs.setObjectName("actionMultiple_Inputs")
        self.actionPalette = QtWidgets.QAction(MainWindow)
        self.actionPalette.setObjectName("actionPalette")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs) 
        self.menuInput.addAction(self.actionMultiple_Inputs)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuInput.menuAction())

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

        self.line.setGeometry(QtCore.QRect(770, 0, 20, 571))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.multiInputsDialog = QtWidgets.QDialog()
        self.ui = Ui_multiInputsDialog()
        self.ui.setupUi(self.multiInputsDialog)
        self.mainWindow = MainWindow

        #FILE MENU EVENTS:
        self.actionNew.triggered.connect(self.file_new)
        self.actionOpen.triggered.connect(self.file_open)
        self.actionSave.triggered.connect(self.file_save)
        self.actionSaveAs.triggered.connect(self.file_saveAs)

        #PALETTE EVENTS
        self.alfabtn.clicked.connect(self.put_Alfa)
        self.betabtn.clicked.connect(self.put_Beta)
        self.gammabtn.clicked.connect(self.put_Gamma)
        self.deltabtn.clicked.connect(self.put_Delta)
        self.epsilonbtn.clicked.connect(self.put_Epsilon)
        self.dsetabtn.clicked.connect(self.put_Dseta)
        self.etabtn.clicked.connect(self.put_Eta)
        self.thetabtn.clicked.connect(self.put_Theta)
        self.iotabtn.clicked.connect(self.put_Iota)
        self.kappabtn.clicked.connect(self.put_Kappa)
        self.lambdaminbtn.clicked.connect(self.put_LambdaMin)
        self.lambdamaybtn.clicked.connect(self.put_LambdaMay)
        self.mybtn.clicked.connect(self.put_My)
        self.nybtn.clicked.connect(self.put_Ny)
        self.xibtn.clicked.connect(self.put_Xi)
        self.omicronbtn.clicked.connect(self.put_Omicron)
        self.pibtn.clicked.connect(self.put_Pi)
        self.rhobtn.clicked.connect(self.put_Rho)
        self.sigmabtn.clicked.connect(self.put_Sigma)
        self.taubtn.clicked.connect(self.put_Tau)
        self.ypsilonbtn.clicked.connect(self.put_Ypsilon)
        self.fibtn.clicked.connect(self.put_Fi)
        self.jibtn.clicked.connect(self.put_Ji)
        self.psibtn.clicked.connect(self.put_Psi)
        self.omegabtn.clicked.connect(self.put_Omega)
        self.arrowbtn.clicked.connect(self.put_Arrow)

        #INPUT OPTIONS EVENTS:
        self.actionMultiple_Inputs.triggered.connect(self.open_multi_inputs)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Untitled"))
        self.oneStepBt.setText(_translate("MainWindow", "One Step"))
        self.runBt.setText(_translate("MainWindow", "Run"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuInput.setTitle(_translate("MainWindow", "Input"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSaveAs.setText(_translate("MainWindow", "Save As"))
        self.actionMultiple_Inputs.setText(_translate("MainWindow", "Multiple Inputs"))
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
        self.InputgroupBox.setTitle(_translate("MainWindow", "Input"))
        self.stringInput.setPlaceholderText(_translate("MainWindow", "Enter String"))
        self.plainTextEdit.setPlaceholderText("#symbols abcdefghijklmnopqrstuvwxyz0123456789\n#vars x\n#markers β\nP1:βx → xβ (P1)\nP2:xβ → Λ.\nP3:x → βx (P1)")


    #File Management Actions:

    def file_open(self):
        path = QFileDialog.getOpenFileName()
        
        if path[0]:
            try:
                file = codecs.open(path[0],'r', encoding='UTF-8')
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
                file = codecs.open(path[0],'w', encoding='UTF-8')

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

        if information:

            if self.currentFile == "":
                self.file_saveAs()

            else:
                try:
                    file = codecs.open(self.currentFile, 'w', encoding='UTF-8')

                    with file:    
                        file.write(information)

                except Exception as error:
                    raise Exception("There was an error saving the file: ".format(error))

        else:
            msg = QMessageBox(self.centralwidget)
            msg.setText("You cannot save an empty file")
            msg.setInformativeText("Please type something before saving")
            msg.setWindowTitle("We are sorry!")
            msg.exec_()

    
    def file_new(self):
        self.plainTextEdit.clear()
        self.resultsField.clear()
        self.currentFile = ""
        self.mainWindow.setWindowTitle("Untitled")

    def put_Alfa(self):
        self.plainTextEdit.insertPlainText("\u03B1")
        self.plainTextEdit.setFocus()
    
    def put_Beta(self):
        self.plainTextEdit.insertPlainText("\u03B2")
        self.plainTextEdit.setFocus()

    def put_Gamma(self):
        self.plainTextEdit.insertPlainText("\u03B3")
        self.plainTextEdit.setFocus()

    def put_Delta(self):
        self.plainTextEdit.insertPlainText("\u03B4")
        self.plainTextEdit.setFocus()

    def put_Epsilon(self):
        self.plainTextEdit.insertPlainText("\u03B5")
        self.plainTextEdit.setFocus()

    def put_Dseta(self):
        self.plainTextEdit.insertPlainText("\u03B6")
        self.plainTextEdit.setFocus()

    def put_Eta(self):
        self.plainTextEdit.insertPlainText("\u03B7")
        self.plainTextEdit.setFocus()

    def put_Theta(self):
        self.plainTextEdit.insertPlainText("\u03B8")
        self.plainTextEdit.setFocus()

    def put_Iota(self):
        self.plainTextEdit.insertPlainText("\u03B9")
        self.plainTextEdit.setFocus()

    def put_Kappa(self):
        self.plainTextEdit.insertPlainText("\u03BA")
        self.plainTextEdit.setFocus()
    
    def put_LambdaMin(self):
        self.plainTextEdit.insertPlainText("\u03BB")
        self.plainTextEdit.setFocus()
    
    def put_LambdaMay(self):
        self.plainTextEdit.insertPlainText("\u039B")
        self.plainTextEdit.setFocus()

    def put_My(self):
        self.plainTextEdit.insertPlainText("\u03BC")
        self.plainTextEdit.setFocus()
    
    def put_Ny(self):
        self.plainTextEdit.insertPlainText("\u03BD")
        self.plainTextEdit.setFocus()
    
    def put_Xi(self):
        self.plainTextEdit.insertPlainText("\u03BE")
        self.plainTextEdit.setFocus()

    def put_Omicron(self):
        self.plainTextEdit.insertPlainText("\u03BF")
        self.plainTextEdit.setFocus()

    def put_Pi(self):
        self.plainTextEdit.insertPlainText("\u03C0")
        self.plainTextEdit.setFocus()

    def put_Rho(self):
        self.plainTextEdit.insertPlainText("\u03C1")
        self.plainTextEdit.setFocus()
    
    def put_Sigma(self):
        self.plainTextEdit.insertPlainText("\u03C3")
        self.plainTextEdit.setFocus()
    
    def put_Tau(self):
        self.plainTextEdit.insertPlainText("\u03C4")
        self.plainTextEdit.setFocus()

    def put_Ypsilon(self):
        self.plainTextEdit.insertPlainText("\u03C5")
        self.plainTextEdit.setFocus()

    def put_Fi(self):
        self.plainTextEdit.insertPlainText("\u03C6")
        self.plainTextEdit.setFocus()
    
    def put_Ji(self):
        self.plainTextEdit.insertPlainText("\u03C7")
        self.plainTextEdit.setFocus()

    def put_Psi(self):
        self.plainTextEdit.insertPlainText("\u03C8")
        self.plainTextEdit.setFocus()
    
    def put_Omega(self):
        self.plainTextEdit.insertPlainText("\u03C9")
        self.plainTextEdit.setFocus()

    def put_Arrow(self):
        self.plainTextEdit.insertPlainText("\u2192")
        self.plainTextEdit.setFocus()


############################## Multiple Inputs GUI:

    def open_multi_inputs(self):
        self.multiInputsDialog.show()