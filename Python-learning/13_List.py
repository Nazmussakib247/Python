#list-Access-change-Add-Remove

mylist=["Apple", "Banana", "Orange"]
print(mylist)
print(len(mylist)) #length of a list
print(type(mylist)) #Getting list type. all list in python is a list type data

#cunstructor to make list
listCons = list(("apple","Cherry",True, 100))
print(listCons)

#Access item
print(listCons[1]) # first index is 0.
print(listCons[-1]) # Negative indexing means from last
print(listCons[2:4]) #Getting ranges of list
print(listCons[:3]) #By leaving out the start value, the range will start at the first item
print(listCons[0:]) # By leaving out the end value, the range will go on to the end of the list
print(mylist[-1:-3]) #Start searching from negative index
list2 = ["Apple", "Banna", "Grape"]
if "Apple" in list2:
    print("Yes,It's here")

#Change a item value
change = ["Apple", "Orange", "Banana", "Jackfruit", "Mangoes", "Tomatos", "Guava"]
change[1:3] = ["Cherry", "Watermelon"]
print(change)

#inserting new item without changing other item in a fixed index
change.insert(7, "fish")
print(change)

#insertinh new item at the end
change.append("Last item")
print(change)

#To append elements from another list to the current list
change.extend(list2)
print(change)


#Remove first item
change2 = ["Apple", "Orange", "Banana"]
change2.remove("Apple")
print(change2)

#Remove specified item with index
change.pop(1) # if dont specified then it will remove last item

#using del keyward
del change2[0]
print(change)

change3 = ["orange","apple", "Banana"]
del change3
#will delete full list as I didn't mentioned index

#Clearing list 
clear = ["Apple", "Orange", "Banana"]
clear.clear()
print(clear)

