print("\n----------------- Arithmetic Operators ------------------")
# Arithmetic Operators:

print(2+3)
print(2-3)
print(2*3)
print(2/3)

# floor (//)
print(10//3)
print(10/3)

# Modulus (%)
print(4%3)

print(round(8.7))
print(round(8.3))




print("\n----------------- Augmented/Enhanced Operator ------------------")
# Augmented/Enhanced Operator
x = 4

x += 3  #==> x = x + 3  now x is : 7
print(x)

x -= 2  # now x is : 5
print(x)

x *= 2.1  # now x is : 10.5
print(x)

x /= 2  # now x is : 5.25
print(x)




print("\n----------------- Operators Precedence ------------------")
# /////////////////////// Operators Precedence /////////////////////////////////
# PEMDAS: 
# Parenthessis
# Exponent
# Multiplication
# Division
# Addition
# Subtraction

a = 30 - 3 * 4 + 4 ** 2 / (2 + 3) - 5
print(a)




print("\n----------------- Math Operator ------------------")
# /////////////////////// Math Operator /////////////////////////////////
import math

print(abs(-23.5))
print(round(abs(-23.486)))

number = 4.8973
print(math.floor(number))
print(math.ceil(number))
print(math.factorial(5))





print("\n----------------- Comparison Operators ------------------")
# ////////////////////////// Comparison Operators //////////////////////////////
#   > , >= , < , <= , == , !=

d = 3 > 2 and 3 != 2
print(d)

c = 3 == 2
print(c)




print("\n----------------- Logical Operators ------------------")
# ////////////////////////// Logical Operators //////////////////////////////////
# and , or , not

price = 25
print(price > 10 and price < 30)
print(not price > 2)


has_haigh_income = True
has_good_credit = False

# and : both the conditions should be true
if has_haigh_income and has_good_credit:
    print("\nEligible for loan.\n")

# or : at least one of the conditions should be true
if has_haigh_income or has_good_credit:
    print("\nEligible for loan.\n")
