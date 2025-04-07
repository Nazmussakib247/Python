#Nested Dictionaries
#A dictionary can contain dictionaries, this is called nested dictionaries.
#Example_nested_dictonary,a dictionary that contain three dictionaries
myfamily = {
    "child1" : {
        "Name" : "Emili",
        "Year" : 2009
    },
    "child2" : {
        "Name" : "Nazmus",
        "Year" : 2001
    },
    "Child3" : {
        "Name" : "Sakib",
        "Year" : 2009
    }
}
print(myfamily)

# Define individual dictionaries
child1 = {
    "Name": "Emili",
    "Year": 2009
}
child2 = {
    "Name": "Nazmus",
    "Year": 2001
}
child3 = {
    "Name": "Sakib",
    "Year": 2009
}

# Merge them into a new dictionary
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# Print the final dictionary
print(myfamily)

#Access Items in Nested Dictionaries
#Print the name of child 2
print(myfamily["child2"]["Name"],"<--Name")


#Loop_Through_Nested_Dictionaries
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print( y + ':', obj[y])