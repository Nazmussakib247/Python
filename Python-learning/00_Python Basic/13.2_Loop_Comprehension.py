fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Only accept items that are not "apple"
new = [x for x in fruits if x != "apple"]
print(new)
