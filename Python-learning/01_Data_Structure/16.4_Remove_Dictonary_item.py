#Remove item using pop() method
thisdict = {
    "Brand" : "BMW",
    "Model" : "Ghost",
    "Year" : "2008"
}
thisdict.pop("Model")
print(thisdict)

#remove last inserted item
thisdict = {
    "Brand" : "BMW",
    "Model" : "Ghost",
    "Year" : 2008,
}
thisdict.popitem()
print(thisdict)

#Delete item
del thisdict["Model"] #key name
print(thisdict)

#Empty the dictonary
thisdict.clear()
print(thisdict)