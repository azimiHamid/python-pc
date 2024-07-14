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

print(round(8.9))
print(round(8.3))


x = 4

x += 3  #==> x = x + 3  now x is : 7
print(x)

x -= 2  # now x is : 5
print(x)

x *= 2.1  # now x is : 10.5
print(x)

x /= 2  # now x is : 5.25
print(x)


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




# ////////////////////////// Comparison Operators //////////////////////////////
#   > , >= , < , <= , == , !=

d = 3 > 2 and 3 != 2
print(d)

c = 3 == 2
print(c)





# ////////////////////////// Logical Operators //////////////////////////////////
# and , or , not

price = 25
print(price > 10 and price < 30)
print(not price > 2)