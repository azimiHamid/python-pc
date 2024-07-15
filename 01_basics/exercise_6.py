# Find the duplicates in a list and remove them:

numbers = [2, 2, 4, 6, 4, 5, 7, 7, 2, 6, 1, 3, 4, 3]
print(numbers)

uniques = []

for num in numbers:
    if num not in uniques:
        uniques.append(num)

uniques.sort()
print(uniques)