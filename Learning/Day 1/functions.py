#Functions: Parameters, Return Values, Lambda
#1. Define and calling function
def add_numbers(a,b):
    add = a+b
    return add

a = int(input("Type number a: ")) 
b_str = input("Type number b: ")
b = int(b_str)
print(f"The sum of a and b is: {add_numbers(a,b)}")

#Lambda functions (for briefness)
multiply = lambda x,y: x*y
print(multiply(4,10)) #Output = 40

################_________EXERCISES___________###############
#Exercise 1:
person_name = input("Type your name: ")
def greet(person_name):
    hello = f"Hello, {person_name}!"
    return hello
print(greet(person_name))

#Exercise 2
a = int(input("Type a number: "))
def is_even(a):
    chill = a%2==0
    return chill
print(f"Is your number even? {is_even(a)}")

#Exercise 3
side = int(input("What is the side of your root? "))
square = lambda side: side**2
print(f"The square of your root is: {square(side)}")
