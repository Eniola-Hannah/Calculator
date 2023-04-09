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
            add()
        elif self.user=="2":
            subtract()
        elif self.user=="3":
            multiply()
        elif self.user=="4":
            divide()
        elif self.user=="0":
            self.que = input("Do you really want to quit? yes/no - ")
            if que=="yes":
                self.exit()
            else:
                self.menu()
        else:
            print("input do not match any of the options, try again")
            self.menu()
        
        
        
    