import os, sys, re

class Rule(object):

    def __init__(self):
        #Attributes:
        self.id = None
        self.pattern = ""
        self.substitution = ""
        self.tag = None
        self.isFinal = False
