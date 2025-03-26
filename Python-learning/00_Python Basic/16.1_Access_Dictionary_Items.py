#Get the value of the "model" key
thisdict = {
    "Brand" : "Ford",
    "Model" : "Mustang",
    "Year" : "1967"
}
x = thisdict["Model"]
print(x)

#Using get() method 
y = thisdict.get("Brand")
print(y)

#Get a list of the keys
z = thisdict.keys()
print(z)

#Get a list of the values
a = thisdict.values()
print(a)

#Get a list of the key:value pairs
z = thisdict.items()
print(z)

#Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("yes,Found")
else:
    print("Not,found")