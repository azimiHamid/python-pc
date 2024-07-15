# Lists: is a complex type, used to represent a list of strings, objects, ...
# We can use negative indices in Python

names = ["Hamid", "Hadi", "Jamal", "Sarah", "Nabila"]
print(names)

names[2] = "9ine"
print(names)

print(names[0])
print(names[-1]) # Nabila
print(names[-2]) # Sarah

# It returns a new list and don't change the original list let's check it bellow:
print(names[0:3])
print("Original list: " + str(names))




print("\n\n\n------------------ List Methods -------------------\n")
# ////////////////////////// List Metthods ////////////////////////////////////
numbers = [1, 2, 3, 4, 5, 6, 7, 7, 9]

# append(item_to_be_added) : add at the end of a list
numbers.append(6)

# insert(which_index, item_to_be_added) : add at any index of a list
numbers.insert(2, 0)

# remove(item_to_be_removed) : remove an item from a list
numbers.remove(5)

# pop() : remove the last item from a list
numbers.pop()

# index(item) : find the index/location of an item in a list
print(numbers.index(3))

# count(item) : count how many times an item has been repeated in a list
print(numbers.count(7))

# clear() : remove all the items of a list
# numbers.clear()

# in method:
print(1 in numbers)
print(100 in numbers)

# len(list_name)
print(len(numbers))

# sort() : sort all the list items [ASCENDING Order]
numbers.sort()

# reverse() : reverse all the list items [DESCENDING Order]
numbers.reverse()

# copy() : Take a copy from a list
second_list = numbers.copy()
second_list.append(12)
print(second_list)

print(numbers)




print("\n------------------ 2D List -------------------\n")
# 2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    output = ""
    for element in row:
        output += str(element) + ", "
    print(output)
print("\n")


print(matrix[0])  # print the 1st row

matrix[0][0] = 20
print(matrix[0][0])

print(matrix)