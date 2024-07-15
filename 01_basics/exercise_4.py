print("------------------ Print F --------------------")
# Print F
numbers = [5, 2, 5, 2, 2]

for i in numbers:
    output = ""
    for j in range(i):
        output += "X"
    print(output)


print("\n------------------ Print H --------------------")
# Print H
rows = [5, 5, 5, 5, 5]  # Each row should have 5 positions

for i in range(len(rows)):
    if i == 2:
        print("XXXXX")
    else:
        print("X   X")