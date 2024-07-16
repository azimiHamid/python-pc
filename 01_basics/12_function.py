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
def greet_with(name, age, city):
    print(f"Hey, {name}!")
    print(f"You are {age} years old.")
    print(f"How is the weather in {city}?")
    
    
greet_with(city="Kabul", name="Hamid", age=21)
