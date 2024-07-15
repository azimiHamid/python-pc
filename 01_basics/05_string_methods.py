print("\n----------------- strings ------------------")
# Strings are immutable in python, it means that the initial string stay the same and will not be changed. when you apply a string method so it creates a copy of the initial string and apply the changes over the copy of that. Test it bellow:

name = "Hamid"
print(name[1:])  # output: amid
print(name[1:-1])  # output: ami




print("\n----------------- formatted strings ------------------")
# Formatted Strings
firstname = "John"
lastname = "Smith"
message = firstname + " [" + lastname + "] is a pro-coder." # concatinated
msg = f"{firstname} [{lastname}] is a pro-coder."  # formatted
print(message)
print(msg)




print("\n----------------- string methods ------------------")
# String Methods
course = "python for everyone"
print(len(course))
print(course.capitalize())
print(course.lower())
print(course.upper())

# main/initial string
print(course)

# find() : it finds the starting index for a char or word
print(course.find("for"))
print(course.find('t'))

print(course.replace("python", "django"))
print(course.replace("o", "e"))
print(course.replace("for", "4"))

# The title() method in Python is a string method that returns a new string where the first character of each word is converted to uppercase and all other characters are converted to lowercase. This is often referred to as title case.
print(course.title())

# in method
print("python" in course)
