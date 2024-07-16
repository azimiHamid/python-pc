# Project #1 of dictionaries
phone = input("Phone : ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Fife",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}

output = ""
for char in phone:
    output += digits_mapping.get(char, "!") + " "

print(output)




print("--------------- project #2 -------------------")
# Project #2 of dictionaries -> emoji converter

emoji = {
    ":)": "😊",
    ":(": "😔",
}
msg = input("> ")
