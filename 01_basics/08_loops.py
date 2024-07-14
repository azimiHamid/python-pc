# ////////////////////////// while loop ///////////////////////////

i = 1
while i <= 10:
    print(i * "*")
    i+=1



print("\n---------------------- for loop -------------------------")
# ////////////////////////// for loop ///////////////////////////

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)


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
for x in range(1, 10, 2): 
    print(f"{x}. Hello")
