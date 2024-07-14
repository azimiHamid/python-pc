# Most of times, we use lists but sometimes you don't want someone to change a list, so you make it tuple instead of list.
# Tuples are immutable, once we create them we can't change them. like bellow example:
numbers = (1, 2, 3, 4, 5, 3, 3, 3, 4, 5, 4)
# numbers[0] = 9  ❌ 'tuple' object does not support item assignment

# count(item_to_be_counted) : shows how many times an item is repeated in a tuple.
print(numbers.count(4)) # output: 3 --> means that 4 is repeated 3 times in this tuple

# count(item_to_find_it's_index) : shows the index of an item in a tuple.
# remember that it shows just the first accurance of an item.
print(numbers.index(3)) # output: 2 --> means that 3 is located at 2nd index in tuple
