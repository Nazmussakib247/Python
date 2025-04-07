#Change Tuple value
#Convert the tuple into a list to be able to change it
x = ("apple","Orange","Banana","Jackfruit","Mangoes")
y = list(x)
y[1] = "Grape"
x = tuple(y)
print(x)

#Add Items
y = list(x)
y.append("Strawberry")
x = tuple(y)
print(x)

#Add tuple to a tuple
z = ("Goava",)
x += z
print(y)

#Remove Items
y = list(x)
y.remove("Banana")
x = tuple(y)
print(x)

#Delete Touple
x = ("apple","Orange","Banana","Jackfruit","Mangoes")
del x
print(x) #Rise an error bcz touple dosent exist anymore 