#List_loop
#Loop Through a List
x = ["apple","Banana","Grape"]
for a in x:
    print(a)

#Loop Through the Index Numbers
x = ["apple","Banana","Grape"]
for i in range (len(x)):
    print(i)


#Print all items, using a while loop to go through all the index numbers
x = ["apple", "Banana", "Grape"]
i = 0
while i < len(x):   # ✅ Corrected condition
    print(x[i])
    i = i + 1

#Looping Using List Comprehension
x = ["apple", "Banana", "Grape"]
[print(a) for a in x]