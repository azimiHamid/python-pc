# Type-conversion: converting DataTypes, like converting string to integer, integer to float, and so on...
# 2024 - "2003" ❌
# 2024 - int("2003") ✅ this is type-conversion

birth_year = input("Enter your birth year : ")
age = 2024 - int(birth_year)
print("You are " + str(age) + " years old.")


#  YOU CAN ALSO convert the type of birth_year when you are getting the input:
'''
birth_year = int(input("Enter your birth year : "))
age = 2024 - birth_year
print(f"You are {age} years old.")

'''

int_value = 50

print(float(int_value))
print(str(int_value) + " deg")
print(int(2.93938849))
print(float("230.23"))
print(int("2003"))