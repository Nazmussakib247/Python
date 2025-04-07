# Looping trhough list
fruits = ["Apple", "Orange", "Banana"]
for i in fruits :
    print(i)

#Looping through a string
for i in "Banana" :
    print(i)

#Break statements
fruits = ["Apple", "Orange", "Banana", "Cherry"]
for i in fruits :
    print(i)
    if i == "Banana" :  #Exit the loop when i is "banana"
        break

#Exit before x is "Banana"
fruit = ["Apple", "Orange", "Banana", "Cherry"]
for x in fruit :
    if x == "Banana" :
        break
    print(x)


#The range() function
for x in range(6) :
    print("X is Done", x)
    
#Range function with a start parameter 
for y in range (2, 9) :
    print(y)

print("done")
#Adding increment in same line
for z in range (2, 11, 2) :
    print(z)

#Else in For Loop
for i in range(10):
    print(i)
else :
    print("Finally, finished")

#Break and else
for i in range(10) :
    if i == 3:
        break
    print(i)
else :
    print("Finally finished")


#Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj :
    for y in fruits :
        print(x, y)

#The pass statement
for x in [0, 1 ,2, 3, 4, 5] :
    pass
