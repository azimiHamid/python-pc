# input : We use input() method to get input from the user.
# Note: input() method always convert everything as a string. So if we input a number like 2, it's going to be processed as "2" not 2. And for this cases we can change the types of variables using Datatype conversion for example int(input("...")) or float(input("..."))

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