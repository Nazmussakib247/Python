#Create an array containing car names
cars = ["BMW", "Toyota", "Supra"]

#Access the Elements of an Array
x = cars[1]
print(x)

#Modify the value of the first array item
cars[0] = "Volvo"
print(cars)

#The Length of an Array
print(len(cars))

#Looping Array Elements
for x in cars:
    print(x)

#Adding Array Elements
cars.append("Honda")
print(cars)

#Removing Array Elements
cars.pop(3)
print(cars)
