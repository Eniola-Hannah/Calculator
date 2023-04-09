import sys
import time

class Cal:
    def __init__(self):
        print("Welcome to Ana's calculator \nHere, ur input will be evaluated correctly")
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
            self.add()
        elif self.user=="3":
            self.subtract()
        elif self.user=="4":
            self.multiply()
        elif self.user=="5":
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
        print("here is your evaluations " + str(self.evalu))
        
        self.que2 = input("do you wish to perform any operations again? yes/no ")
        if self.que2=="yes":
            self.menu()
        elif self.que2=="no":
            sys.exit()
        
        
    def add(self):
        self.a = input("first Value - ")
        self.b = input("Second Value - ")
        self.sol = int(self.a) + int(self.b)
        print("here is your evaluations " + str(self.sol))
        
        self.que3 = input("do you wish to perform any operations again? yes/no ")
        if self.que3=="yes":
            self.menu()
        elif self.que3=="no":
            sys.exit()
        
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
        

calculator = Cal()
    