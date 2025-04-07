# F-Strings
txt = f"The price is 49 dollars"
print(txt)

# Placeholders
price = 59
txt = f"The price is {price} dollars"
print(txt)

# Modifiers
txt = f"The price is {price:.2f} dollars"
print(txt)

# Direct value formatting
txt = f"The price is {95:.2f} dollars"
print(txt)

# Operations in f-string
txt = f"The price is {20 * 59} dollars"
print(txt)

# Math with variables
price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

# if-else inside f-string
price = 49
txt = f"It is very {'Expensive' if price > 50 else 'Cheap'}"
print(txt)

# Functions in f-string
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# Thousand separator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# format() method
price = 49
txt = "The price is {} dollars"
print(txt.format(price))

txt = "The price is {:.2f} dollars"
print(txt.format(price))

# Multiple values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Index numbers
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Same value multiple times
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named indexes
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))