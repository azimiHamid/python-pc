# input : We use input() method to get input from the user.

name = input("What is your name? ")
print("Hello, " + name)


# Calculator:
a = int(input("1st number = "))
b = int(input("2nd number = "))

def sum(a, b):
    return a+b
print("Sum = " + str(sum(a,b)))

def subtract(a, b):
    return a-b
print("Subtract = " + str(subtract(a,b)))

def product(a, b):
    return a*b
print("Product = " + str(product(a,b)))

def division(a, b):
    return a/b
print("Division = " + str(division(a,b)))