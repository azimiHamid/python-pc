# Strings are immutable in python, it means that the initial string stay the same and will not be changed. when you apply a string method so it creates a copy of the initial string and apply the changes over the copy of that. Test it bellow:

course = "python for everyone"


print(course.capitalize())
print(course.lower())
print(course.upper())

# main/initial string
print(course)

# find() : it finds the starting index for a char or word
print(course.find("for"))
print(course.find("t"))

print(course.replace("p", "j"))
print(course.replace("o", "e"))
print(course.replace("for", "4"))

# in method
print("python" in course)
