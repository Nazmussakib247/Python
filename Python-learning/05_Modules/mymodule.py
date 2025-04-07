#-------------------------------------
# Create a Module (mymodule.py)
#-------------------------------------
# Save this code in a separate file named: mymodule.py

# def greeting(name):
#     print("Hello, " + name)

# person1 = {
#     "name": "John",
#     "age": 36,
#     "country": "Norway"
# }


#-------------------------------------
# Use a Module
#-------------------------------------
import mymodule

# Call the greeting function from the module
mymodule.greeting("Jonathan")


#-------------------------------------
# Variables in Module
#-------------------------------------
# Access the dictionary from the module
x = mymodule.person1["age"]
print(x)


#-------------------------------------
# Re-naming a Module using alias
#-------------------------------------
import mymodule as mx

a = mx.person1["age"]
print(a)


#-------------------------------------
# Built-in Modules
#-------------------------------------
import platform

# Use a function from the platform module
x = platform.system()
print(x)


#-------------------------------------
# Using the dir() Function
#-------------------------------------
# List all functions and variables in the platform module
x = dir(platform)
print(x)


#-------------------------------------
# Import From Module
#-------------------------------------
from mymodule import person1

print(person1["age"])
