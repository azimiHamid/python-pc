# Project #1 of dictionaries
phone = input("Phone : ").replace(" ", "")
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

# output = ""
# for char in phone:
#     output += digits_mapping.get(char, "!") + " "

# print(output)

for num in digits_mapping:
    if num in phone:
        phone = phone.replace(num, digits_mapping.get(num) + " ")

print(phone)




print("\n--------------- project #2 -------------------")
# Project #2 of dictionaries -> emoji converter

emojis = {
    ":)": "😊",
    ":(": "😔",
    ":D": "😁",
    ":P": "😜",
    ";)": "😉",
    ":o": "😮",
}
msg = input("> ")

for emoji in emojis:
    if emoji in msg:
        msg = msg.replace(emoji, emojis[emoji])
    else:
        msg = "⛔"
        
print(msg)