import sys
import time

class Cal:
    def __init__(self):
        print("Welcome to Ana's calculator \n here, ur input will be evaluated correctly")
        time.sleep(1)
        self.menu()

    def menu(self):
        self.user = input("""
                kindly choose your operands
                
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    0. Quit
        """)
        
        if self.user=="1":
            self.add()
        elif self.user=="2":
            self.subtract()
        elif self.user=="3":
            self.multiply()
        elif self.user=="4":
            self.divide()
        elif self.user=="0":
            self.que = input("Do you really want to quit? yes/no - ")
            if self.que=="yes":
                sys.exit()
            elif self.que=="no":
                self.menu()
        else:
            print("input do not match any of the options, try again")
            self.menu()
        
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
        

calculator = Cal()
    