# Dictionaries in Python are a collection type that allows you to store key-value pairs.  [It's like an Object in JavaScript]
# They are: - un_ordered - mutable - key-value pairs - unique keys - dynamic size

# You can create a dictionary using curly braces {} or the dict() function.
# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Using the dict() function
my_dict = dict(name="Alice", age=25, city="New York")





print("-------------------------- Examples -------------------------")
customer = {
    "name": "John Smith",
    "age": 30,
    "city": "Kabul",
    "is_verified": True
}

# updation
customer["name"] = "Hamid Azimi"
customer["email"] = "hamid@ha.ai.com"

# deletion
del customer["city"]        # Removes the key "city" and its value
email = customer.pop("email")  # Removes the key "email" and returns its value

# Checking if a key exists
if "email" in customer:
    print("Email found:", customer["email"])


# Iterating over keys
for key in customer:
    print(key, ":", customer[key])


print(customer)
print(customer["name"])
# print(customer["birthdate"])  # output: KeyError - key does not exist ❌
print(customer.get("age"))
print(customer.get("birthdate"))  # output: None
print(customer.get("birthdate", "Jan 1 1980"))  # output: Jan 1 1980  ==> default value



print("\n------------------- dictionary methods ------------------")
# Using dictionary methods
keys = customer.keys()
values = customer.values()
items = customer.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)