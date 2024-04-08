# Day 10 Project - Calculator

def sum(a,b):
    print(f"the sum is: {a+b}")
def dif(a,b):
    print(f"the difference is: {a-b}")
def multiply(a,b):
    print(f"the product is: {a*b}")
def divide(a,b):
    print(f"the quotient is: {a/b}")

number1 = int(input("first number: "))
number2 = int(input("second number: "))
wish = input("enter what would you like to do with these numbers: ").lower()

if wish == 'add':
    sum(number1,number2)
elif wish == 'subtract':
    dif(number1,number2)
elif wish == 'multiply':
    multiply(number1,number2)
else:
    divide(number1,number2)        