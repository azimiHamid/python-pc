from email import message


print("\n------------------ function defination --------------------")
def greet():
    print("Hey, there!")
    print("How is the weather in your city?")
    
    
greet()



print("\n------------------ function with parameter --------------------")
def greet_with(name, age, city):
    print(f"Hey, {name}!")
    print(f"You are {age} years old.")
    print(f"How is the weather in {city}?")
    
    
greet_with(21, "Kabul", "Hamid")




print("\n------------------ function keyword arguments --------------------")
def greetings(name, age, city):
    print(f"Hey, {name}!")
    print(f"You are {age} years old.")
    print(f"How is the weather in {city}?")
    
    
greetings(city="Kabul", name="Hamid", age=21)




print("\n------------------ return keyword --------------------")
def sum(a, b):
    print(a + b)

print(sum(3, 4)) # output: 7  and  None : why None? because in Python, by-default, all the functions return None.




print("\n------------------ Emoji-converter --------------------")
def emoji_converter(msg):
    words = msg.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😔",
        ":o" : "😲",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    
    return output
    
    
msg = input("> ")
print(emoji_converter(msg))




print("\n----------- Deep explanation of emoji-converter(msg) function ------------")


# for word in words:
#     output += emojis.get(word, word) + " "   👇
''' ⬇️
This for loop iterates over each word in the words list.

emojis.get(word, word) attempts to find the word in the emojis dictionary:

    👉 If the word is a key in the emojis dictionary (e.g., ":)"), it returns the corresponding emoji (e.g., "😊").

    👉 If the word is not found in the emojis dictionary, it returns the word itself.

The result of emojis.get(word, word) is then concatenated to the output string, along with a space.

👇 Here's a detailed breakdown of the for loop for the example input "Hello :) world":
    
 - word = 'Hello'
 - emojis.get('Hello', 'Hello') returns 'Hello'
 - output becomes 'Hello '

 - word = ':)'
 - emojis.get(':)', ':)') returns '😊'
 - output becomes 'Hello 😊 '
 
 - word = 'world'
 - emojis.get('world', 'world') returns 'world'
 - output becomes 'Hello 😊 world '

'''