# Adds an element at the end of the list
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.append("Jackfruit")
print(mylist)  # ['apple', 'banana', 'cherry', 'Orange', 'Jackfruit']

# Removes all the elements from the list
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.clear()
print(mylist)  # []

# Returns a copy of the list
mylist = ["apple", "banana", "cherry", "Orange"]
copy_list = mylist.copy()  # Fixed: use copy() correctly
print(copy_list)  # ['apple', 'banana', 'cherry', 'Orange']

# Returns the number of elements with the specified value
mylist = ["apple", "banana", "cherry", "Orange", "banana"]
print(mylist.count("banana"))  # 2

# Adds elements of another list (or any iterable) to the current list
mylist = ["apple", "banana", "cherry", "Orange"]
mylist2 = [1, 3, 4, 5]
mylist2.extend(mylist)
print(mylist2)  # [1, 3, 4, 5, 'apple', 'banana', 'cherry', 'Orange']

# Returns the index of the first occurrence of the specified value
mylist = ["apple", "banana", "cherry", "Orange"]
print(mylist.index("banana"))  # 1

# Adds an element at the specified position
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.insert(1, "Jackfruit")  # Insert at index 1
print(mylist)  # ['apple', 'Jackfruit', 'banana', 'cherry', 'Orange']

# Removes the element at the specified position
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.pop(2)  # Removes 'cherry'
print(mylist)  # ['apple', 'banana', 'Orange']

# Removes the first item with the specified value
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.remove("banana")
print(mylist)  # ['apple', 'cherry', 'Orange']

# Reverses the order of the list
mylist = ["apple", "banana", "cherry", "Orange"]
mylist.reverse()
print(mylist)  # ['Orange', 'cherry', 'banana', 'apple']

# Sorts the list in ascending order
mylist = ["banana", "apple", "cherry", "Orange"]
mylist.sort()
print(mylist)  # ['Orange', 'apple', 'banana', 'cherry']

# Sorting a list of numbers
num_list = [5, 2, 9, 1, 10]
num_list.sort()
print(num_list)  # [1, 2, 5, 9, 10]