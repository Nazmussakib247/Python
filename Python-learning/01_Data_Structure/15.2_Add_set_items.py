#Add items
#Once a set is created, you cannot change its items, but you can add new items.
set = {"apple", "banana", "cherry"}
set.add("Mango")
print(set)

#Update set, update from another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#Add Any Iterable
#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)                                                                                 