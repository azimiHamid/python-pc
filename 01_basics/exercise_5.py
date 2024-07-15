# Let's find the largest number in the list
print("\n")
numbers = [734, 656, 728, 432, 736, 748, 13, 739, 7000]  # output: max_num = 7000
print(numbers)

max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num

print(f"Largest number = {max_num}")


min_num = numbers[0]
for num in numbers:
    if num < min_num:
        min_num = num

print(f"Smallest number = {min_num}")