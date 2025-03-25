# Create a Tuple (Rename variable to avoid conflict)
my_tuple = ("apple", "banana", "orange", "Jackfruit")
print(my_tuple)

# Tuple Length
print(len(my_tuple))

# Create Tuple With One Item
tuple3 = ("apple",)  # remember the comma
print(type(tuple3))  # Fixed: Checking type of tuple3 instead of `tuple`

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))  # Now it works fine
print(thistuple)

# Tuple containing different types of data
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)