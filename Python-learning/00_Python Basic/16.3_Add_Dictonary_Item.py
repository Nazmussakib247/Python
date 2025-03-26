#Adding new item 
thisdict = {
    "Brand" : "Yamaha",
    "Model" : "R15",
    "Year" : "2016",
}
thisdict["color"] = "red"
print(thisdict)

#Update a dictonary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)