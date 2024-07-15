# ////////////////////////// while loop ///////////////////////////

i = 1
while i <= 10:
    print(i * "*")
    i+=1




print("\n---------------------- for loop -------------------------")
# ////////////////////////// for loop ///////////////////////////
for letter in "Python\n":
    print(letter)


numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
print("\n")

prices = [20, 30, 40]
total = 0
for p in prices:
    total += p
print(f"Total price : {total}")


print("\n---------- let's do it in while loop -----------")
# let's do it with while loop
j = 0
while j < len(numbers):
    print(numbers[j])
    j += 1




print("\n---------- range() in for loop -----------")
# let's use range(a, b, c) : b is always excluded, c shows how many steps(increment/decrement)
num = range(5)
print(num)

for n in num:
    print(n)


print("\n")
for x in range(0, 10, 2): 
    print(f"{x} x 2 = {x*2}")




print("\n---------------- Nested loops -----------------")
# Nested loops
coordinates = []
for x in range(3):
    for y in range(3):
        coordinates += [(x, y)]
print(coordinates)

# Nested loops by using (list comprehension) method
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs)