from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import os, sys, re, codecs
from classes import Rule
from MainWindow import Ui_MainWindow


class Markov(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(Markov, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()

        self.variables = [] 
        self.symbols = []
        self.markers = []
        self.rules = []

        self.runBt.clicked.connect(self.run)


    def run(self):
        self.load_attributes()
        rule = "βx"
        inputt = 'βa'
        pVariables = self.containsVariable("βx")

        if pVariables:
            for var in pVariables:
                test = rule.replace(var, "[" + self.symbols + "]")
                print(test)
                test2 = re.sub(test, 'xβ', inputt)
                print(test2)
        else:
            print("NO HAY")

        # self.load_attributes()s
        # self.replace("I bought a B of As from T S.")
    

    def load_attributes(self):
        lines = str(self.plainTextEdit.toPlainText()).splitlines()
        
        for line in lines:
            if re.match("#symbols", line):
                self.symbols = re.sub("^\#symbols", "", line).lstrip()
            else:
                if re.match("#vars", line):
                    self.variables = re.sub("^\#vars", "", line).lstrip()
                else:
                    if re.match("#markers", line):
                        self.markers = re.sub("^\#markers", "", line).lstrip()
                    else:
                        if re.match("^.+", line):
                            self.create_rule(line)
        

    def create_rule(self, line):
        rule = Rule()

        #ID
        forId = re.compile('([\D].*)(?=:)') #Regular expresion to extract identifiers
        reMatch = forId.search(line)
        if reMatch: #If the rule has an id
            rule.id = reMatch.group(0).lstrip()

        #Pattern
        compilerNoIdQuotes = re.compile('(?<=\")(.*)(?=\"\s*\→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with no id, ex: "x"->
        compilerNoId = re.compile('(.*)(?=→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with no id, ex: x->
        compilerId = re.compile('(?<=:)(.*)(?=→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with id, ex: P1: XX->
        
        reMatchNoIdQuotes = compilerNoIdQuotes.search(line)
        reMatchNoId = compilerNoId.search(line)
        reMatchId = compilerId.search(line)

        #print("TEST")

        if reMatchId:
            rule.pattern = reMatchId.group(0).lstrip()
        else:
            if reMatchNoIdQuotes:
                rule.pattern = reMatchNoIdQuotes.group(0).lstrip()
                
            else:
                if reMatchNoId:
                    rule.pattern = reMatchNoId.group(0).lstrip()

        #Substitution and isFinal
        compilerTag= re.compile('(?<=→)(.*)(?=\()', re.IGNORECASE | re.UNICODE) #Compiler for substitution with a tag
        compilerPoint = re.compile('(?<=→)(.*)(?=\.)', re.IGNORECASE | re.UNICODE) #Compiler for final substitution
        compilerSubs = re.compile('(?<=→)(.*)', re.IGNORECASE | re.UNICODE) #Compiler for just a substitution 
        
        reMatchTag = compilerTag.search(line)
        reMatchPoint = compilerPoint.search(line)
        reMatchSubs = compilerSubs.search(line)

        if reMatchTag:
            rule.substitution = reMatchTag.group(0).lstrip()
        else:
            if reMatchPoint:
                rule.substitution = reMatchPoint.group(0).lstrip()
                rule.isFinal=True
                
            else:
                if reMatchSubs:
                    #print(" Tercer IF nothing")
                    rule.substitution = reMatchSubs.group(0).lstrip()
        
        #Tag
        tag = re.compile('(?<=\()(.*)(?=\))') #Regular expresion to extract identifiers
        reMatchForTag = tag.search(line)
        if reMatchForTag : #If the rule has an id
            rule.tag = reMatchForTag.group(0).lstrip()

        self.rules.append(rule)    
                    

    def replace(self, input):
        while True:
            for rule in self.rules:
                if rule.pattern in input:
                    input = input.replace(rule.pattern, rule.substitution, 1)
                    if rule.isFinal:
                        print(input)
                        break
                    else:
                        print(input)
            break


    def containsVariable(self, pattern):
        pVariables = [] #Pattern variables
        for var in self.variables:
            if var in pattern:
                pVariables.append(var)

        return pVariables


############ Application Main #############
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    markov = Markov()
    sys.exit(app.exec_())