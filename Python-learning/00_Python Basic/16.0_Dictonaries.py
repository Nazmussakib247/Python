#Dictonaries
thisdict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
print(thisdict)

#Print the "brand" value of the 
print(thisdict["brand"])

#Dictionary Length
print(len(thisdict))

#Dictionary Items - Data Types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(type(thisdict))

#The dict() Constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)