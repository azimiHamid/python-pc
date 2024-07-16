# Exceptions are used to avoid crashing our program, instead it gives us the ability to handle the errors with approperiate messages.
# In python we use try ... except block for exception handling.

try:
    age = int(input("Enter your age : "))
    income = 20000
    risk = income / age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("Cannot divide by zero! age can't be zero.")
except ValueError:
    print("Invalid Value!")

