#Change Values
thisdict = {
    "Brand" : "Yamaha",
    "Model" : "R15",
    "Year" : "2010"
}
thisdict["Year"] = 2018
print(thisdict)

#Using update() method
thisdict.update({"Year" : 1000})
print(thisdict)