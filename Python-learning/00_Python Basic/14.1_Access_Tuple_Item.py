#Print the second item in the tuple
tuple = ("apple", "banana", "cherry")
print(tuple[1])

#Negative Indexing/Print the last item of the tuple
print(tuple[-1])

#Range of Indexes/Return the third, fourth, and fifth item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#returns the items from the beginning to, but NOT included, "kiwi"
print(thistuple[:4])

#returns the items from "cherry" and to the end
print(thistuple[:4])

#Range of Negative Indexes
print(thistuple[-4:-1])

#Check if Item Exists
if "apple" in thistuple:
    print("Yes,'apple' is present in the tuple")
else:
    print("No,'apple' is not present")