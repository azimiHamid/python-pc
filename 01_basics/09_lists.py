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
numbers = [1, 2, 3, 4, 5]

# append(item_to_be_added) : add at the end of a list
numbers.append(6)

# insert(which_index, item_to_be_added) : add at any index of a list
numbers.insert(2, 0)

# remove(item_to_be_removed) : remove an item from a list
numbers.remove(5)

# clear() : remove all the items of a list
# numbers.clear()

# in method:
print(1 in numbers)
print(100 in numbers)

# len(list_name)
print(len(numbers))

print(numbers)