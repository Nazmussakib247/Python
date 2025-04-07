#Loop Through a Dictionary
#Print all key names in the dictionary, one by one
thisdict = {
    "Brand" : "BMW",
    "Model" : "Ghost",
    "Year" : 2019 
}
for x in thisdict:
    print(x)

#Print all values in the dictionary, one by one
for x in thisdict:
    print(thisdict[x])

#Returns value of a dictonary
for x in thisdict.values():
    print(x)

#Key of the dictonary using key() method
for x in thisdict.keys():
    print(x)

#Loop through both keys and values, by using the items() method
for x, y in thisdict.items():
    print(x, y)