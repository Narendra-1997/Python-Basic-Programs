# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:
# Use __init__ method to construct some parameters

class inputoutstring:
    def  init  (self):
        self.s=""

    def input_string(self):
        self.s=input("entert something: ")

    def printstring(self):
        print(self.s.upper())

strObj=inputoutstring()
strObj.input_string()
strObj.printstring()  

