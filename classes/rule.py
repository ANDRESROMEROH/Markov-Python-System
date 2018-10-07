import os, sys, re

class Rule(object):

    def __init__(self):
        #Attributes:
        self.id = ""
        self.pattern = ""
        self.substitution = ""
        self.tag = None
        self.isFinal = False

    def is_final_rule(self):
        return self.isFinal
    

# if __name__ == '__main__':
#     test = Rule()
#     test.id = "p1"
#     print(test.id)

