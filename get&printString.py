
# 5 - Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
#
# Hints:
# Use _init_ method to construct some parameters

class Str():
    def __init__(self):
        self.string = ""

    def get(self):
        self.string = input("Enter string: ")

    def put(self):
        print("String is:", self.string.upper())

s=Str()
s.get()
s.put()



