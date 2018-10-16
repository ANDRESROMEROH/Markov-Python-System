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

        #Algorithm Components:
        self.variables = [] 
        self.symbols = []
        self.markers = []
        self.rules = []

        #Event listeners for action buttons:
        self.runBt.clicked.connect(self.run)
        self.ui.runInputsBt.clicked.connect(self.runMultipleInputs)        


    def run(self):
        self.variables = [] 
        self.symbols = []
        self.markers = []
        self.rules = []
        userInput = self.getUserInput()
        self.load_algorithm()
        self.remove_symbols()
        # print("Lista antes: ",self.symbols)
        self.execute_algorithm(userInput)
        
        # print("Lista despues: ",self.symbols)


    def runMultipleInputs(self):
        multipleInputs = self.getItems()
        for input in multipleInputs:
            self.resultsField.appendPlainText(input)

    
    def getUserInput(self):
        input=self.stringInput.text()
        return input   


    def getItems(self):
        multipleInputs = []
        for item in self.ui.rows:
            if item.text() != '':
                multipleInputs.append(item.text())
        return multipleInputs   

    def remove_symbols(self):
        for v in self.variables:
            if v in self.symbols:
                self.symbols=self.symbols.replace(v,'')
                


    def load_algorithm(self):
        lines = str(self.plainTextEdit.toPlainText()).splitlines()
        
        for line in lines:
            if re.match("#symbols", line):
                self.symbols = re.sub("^\#symbols", "", line).replace(" ", "")
            else:
                if re.match("#vars", line):
                    self.variables = re.sub("^\#vars", "", line).replace(" ", "")
                else:
                    if re.match("#markers", line):
                        self.markers = re.sub("^\#markers", "", line).replace(" ", "")
                    else:
                        if re.match("^.+", line):
                            self.create_rule(line)


    def create_rule(self, line):
        rule = Rule()

        #ID
        forId = re.compile('([\D].*)(?=:)') #Regular expresion to extract identifiers
        reMatch = forId.search(line)
        if reMatch: #If the rule has an id
            rule.id = reMatch.group(0).replace(" ", "")

        #Pattern
        compilerNoIdQuotes = re.compile('(?<=\")(.*)(?=\"\s*\→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with no id, ex: "x"->
        compilerNoId = re.compile('(.*)(?=→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with no id, ex: x->
        compilerId = re.compile('(?<=:)(.*)(?=→)', re.IGNORECASE | re.UNICODE) #Compiler for pattern with id, ex: P1: XX->
        
        reMatchNoIdQuotes = compilerNoIdQuotes.search(line)
        reMatchNoId = compilerNoId.search(line)
        reMatchId = compilerId.search(line)

        #print("TEST")

        if reMatchId:
            rule.pattern = reMatchId.group(0).replace(" ", "")
        else:
            if reMatchNoIdQuotes:
                rule.pattern = reMatchNoIdQuotes.group(0).replace(" ", "")
                
            else:
                if reMatchNoId:
                    rule.pattern = reMatchNoId.group(0).replace(" ", "")

        #Substitution and isFinal
        compilerTag= re.compile('(?<=→)(.*)(?=\()', re.IGNORECASE | re.UNICODE) #Compiler for substitution with a tag
        compilerPoint = re.compile('(?<=→)(.*)(?=\.)', re.IGNORECASE | re.UNICODE) #Compiler for final substitution
        compilerSubs = re.compile('(?<=→)(.*)', re.IGNORECASE | re.UNICODE) #Compiler for just a substitution 
        
        reMatchTag = compilerTag.search(line)
        reMatchPoint = compilerPoint.search(line)
        reMatchSubs = compilerSubs.search(line)

        if reMatchTag:
            rule.substitution = reMatchTag.group(0).replace(" ", "")
        else:
            if reMatchPoint:
                rule.substitution = reMatchPoint.group(0).replace(" ", "")
                rule.isFinal=True
                
            else:
                if reMatchSubs:
                    #print(" Tercer IF nothing")
                    rule.substitution = reMatchSubs.group(0).replace(" ", "")
        
        #Tag
        tag = re.compile('(?<=\()(.*)(?=\))') #Regular expresion to extract identifiers
        reMatchForTag = tag.search(line)
        if reMatchForTag : #If the rule has an id
            rule.tag = reMatchForTag.group(0).replace(" ", "")

        self.rules.append(rule)             

    def execute_algorithm(self, userInput):
        restart = True
        userInput = self.nullrule(userInput)
        while restart:
            for rule in self.rules:

                if self.variables != []:

                    regex = self.getRuleRegex(rule)
                
                    if regex.search(userInput) != None: #Same as -> if rule.pattern in userInput:
                        userInput = self.processRuleCase1(regex, rule, userInput)
                        
                        if rule.isFinal:
                            userInput=self.remove_null(userInput)
                            self.resultsField.appendPlainText(userInput + "  Aplicando: " + rule.id)
                            self.resultsField.appendPlainText("---------------------------")
                            restart = False
                            break
                        else:
                            userInput=self.remove_null(userInput)
                            self.resultsField.appendPlainText(userInput + "  Aplicando: " + rule.id)
                            restart = True
                            break

                else: 
                    if rule.pattern in userInput:
                        userInput = self.processRuleCase2(rule, userInput)

                        if rule.isFinal:
                            userInput=self.remove_null(userInput)
                            self.resultsField.appendPlainText(userInput)
                            break
                        else:
                            userInput=self.remove_null(userInput)
                            self.resultsField.appendPlainText(userInput)
                
                restart = False


    def processRuleCase1(self, regex, rule, userInput): #Process rules which pattern contains variables...  
        #Below line extracts the matching part of the input string:
        matchingString = regex.search(userInput).group(0) 
        #Below line applies the substitution:
        return re.sub(regex, self.applySubstitution(matchingString, rule.pattern, rule.substitution), userInput, 1) 
    

    def processRuleCase2(self, rule, userInput): #Process rules which pattern doesn't contain variables...
        return userInput.replace(rule.pattern, rule.substitution, 1)
        

    def applySubstitution(self, matchingString ,pattern, substitution):     
        nvars = self.containsVariable(pattern)

        if len(nvars) > 1:
            strvars = self.variablesFromString(matchingString)

            for i in range(0, len(nvars)):
                substitution=substitution.replace(nvars[i], strvars[i], 1)
            
        else:       
            for m in matchingString:
                if m in self.symbols:
                    for s in substitution:
                        if s in self.variables:
                            substitution = substitution.replace(s, m, 1)
                            break
        
        return substitution

    def getRuleRegex(self, rule): #Return the regex of a given rule..
        patternVariables = self.containsVariable(rule.pattern)
        regex = rule.pattern

        if patternVariables:
            for var in patternVariables: 
                #Below line constructs a regex based on the symbols and markers found on the pattern:
                regex = regex.replace(var, "[" + self.symbols + "]", 1)
        
        return re.compile(regex, re.IGNORECASE | re.UNICODE)


    def containsVariable(self, pattern):
        patternVariables = [] #Pattern variables
        for var in self.variables:
            if var in pattern:
                patternVariables.append(var)

        return patternVariables

    def remove_null(self,input):
        if "\u039B" in input:
            input=input.replace("\u039B","")
        return input

    
    def nullrule(self,userInput):
        for rule in self.rules:
            if "\u039B" ==rule.pattern:
                userInput="\u039B"+userInput
                break
        return userInput


    def variablesFromString(self, matchingString):
        strVariables = [] #Matching string variables
        for var in self.symbols:
            if var in matchingString:
                strVariables.append(var)

        return strVariables


####################### APPLICATION MAIN(): ###########################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    markov = Markov()
    sys.exit(app.exec_())