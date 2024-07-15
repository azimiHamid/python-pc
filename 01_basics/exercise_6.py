# Find the duplicates in a list and remove them:

names = ["hamid", "hamid", "Hadi", "Hadi", "hamid", "Ahmad", "Hadi", "Ali"]
numbers = [2, 2, 4, 6, 4, 5, 7, 7, 2, 6, 1, 3, 4, 3]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(numbers)
unique_numbers.sort()
print(unique_numbers)


print("\n----------------------------------")

unique_names = []
for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(names)
unique_names.sort()
print(unique_names)