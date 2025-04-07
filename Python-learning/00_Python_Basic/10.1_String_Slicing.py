"""You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string."""

#Getting Character from 2 to 5. (5 not included)
s = "Hello, world!"
print(s[2:5])

#Slice From the Start
print(s[:5])

#Slice to the end
print(s[1:])

#Negative Indexing
#Use negative indexes to start the slice from the end of the string.
print(s[-5:-1])
