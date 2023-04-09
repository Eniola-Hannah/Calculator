import sys
import time

class Cal:
    def __init__(self):
        print("Welcome to Ana's calculator \n here, ur input will be evaluated correctly")
        time.sleep(1)
        self.menu()

    def menu():
        user = input("""
                kindly choose your operands
                
                    1. Addition
                    2. Subtraction
                    3. Multiplication
                    4. Division
                    0. Quit
        """)