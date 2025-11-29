#####################################
# Day 1 - Project 1: CLI Calculator
#####################################

import math

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def times(a,b):
    return a*b
def over(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Denominator must not be 0"
def sqroot(a):
    if a < 0:
        return "Cannot take sqrt of negative numbers."
    else: 
        return math.sqrt(a)
def power(a,b):
    return a**b
def modulo(a,b):
    try:
        return a%b
    except ZeroDivisionError:
        return "Denominator must not be 0"
def calculator():
    print("=" * 50)
    print("CLI Calculator")
    print("=" * 50)
    print("- Available operations: +, -, *, /, %, **, sqrt")
    print("- Print 'esc' to exit.")
    print("=" * 50)

    while True:
        try:
            operation = input("\n Enter operation: ")

            if operation == 'esc':
                print("Thank you for using CLI Calculator!")
                break
            elif operation in ["+", "add", "addition"]:
                num1 = int(input("\n Enter no. 1: "))
                num2 = int(input("\n Enter no. 2: "))
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operation in ["-", "subtraction", "subtract"]:
                num1 = int(input("\n Enter no. 1: "))
                num2 = int(input("\n Enter no. 2: "))
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operation in ["/", "division", "divide"]:
                num1 = int(input("\n Enter numerator: "))
                num2 = int(input("\n Enter denominator: "))
                print(f"{num1} / {num2} = {over(num1, num2)}")
            elif operation in ["*", "times", "multiply", "multiplication"]:
                num1 = int(input("\n Enter no. 1: "))
                num2 = int(input("\n Enter no. 2: "))
                print(f"{num1} * {num2} = {times(num1, num2)}")
            elif operation in ["sqrt", "square root"]:
                num1 = int(input("Enter number: "))
                print(f"sqrt({num1}) = {sqroot(num1)} ")
            elif operation in ["pow", "**", "power"]:
                num1 = int(input("\n Enter base no.: "))
                num2 = int(input("\n Enter exponent no.: "))
                print(f"{num1}^{num2} = {power(num1, num2)}")
            elif operation == "modulo":
                num1 = int(input("\n Enter no. 1: "))
                num2 = int(input("\n Enter no. 2: "))
                print(f"{num1} % {num2} = {modulo(num1, num2)}")
            else: print("Invalid operation.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")
    
if __name__ == "__main__":
    calculator()