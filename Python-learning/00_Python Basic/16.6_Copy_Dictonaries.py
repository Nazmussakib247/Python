#Copy of dictonary using copy() method
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Using dict() function
mydict = dict(thisdict)
print(mydict) 