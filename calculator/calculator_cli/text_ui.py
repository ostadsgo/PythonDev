import os
import sys

import calc





def quit_program(*args):
    sys.exit()


def menu():
    items = [
        "1) Addition",
        "2) Substraction",
        "3) Multipication",
        "4) Division",
        "5) Quit"
    ]

    for item in items:
        print(item)
        
    return input("Choose from menu pls: ")


def main():
    operations = {
        "1": calc.add,
        "2": calc.minus,
        "3": calc.mul,
        "4": calc.div,
        "5": quit_program
    }
    
    op_symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }
    
    while True:
        os.system("clear")
        response = menu()
        if operations.get(response) is not None:
            num1 = int(input("Enter number one: "))
            num2 = int(input("Enter number two: "))
            res = operations[response](num1, num2)
            print(f"{num1} {op_symbols[response]} {num2} = {res}")
        else:
            print("Invalid choose!")
            
        input("Press any key to back to menu ...")
        
        
if __name__ == "__main__":
    main()
