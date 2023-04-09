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
                
                    1. Random Calculation
                    2. Addition
                    3. Subtraction
                    4. Multiplication
                    5. Division
                    0. Quit
        """)
        
        if self.user=="1":
            self.random()
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
        
    def random(self):
        self.evalu = eval(input("""
                                Input your expression for it to be evaluated:
                    """))
        print("here is your evaluations " + self.evalu)
        que2 = input("do you wish to perform any operations again? yes/no ")
            if self.que=="yes":
                self.menu()
            elif self.que=="no":
                sys.exit()
        
        
    def add(self):
        pass
        
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
        

calculator = Cal()
    