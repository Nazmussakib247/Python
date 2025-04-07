#If statement
a = 30
b = 60
if b > a :
    print("B is greater than a")

#Taking user input and comparing by if statement
"""
a = input("Input first Number:")
b = input("Input second Number:")
if a > b :
    print("A is greater than B")
else:
    print("B is greater than A")
"""

#elif
#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
a = 100
b = 100
if a > b :
    print("A is greater than B")
elif a == b :
    print("Both are equal")
else:
    print("B is greater")

#else statement
#The else keyword catches anything which isn't caught by the preceding conditions
a = 200
b = 50
if a < b :
    print("A is smaller")
elif a == b :
    print("Both are equal")
else :
    print("B is smaller")

#Short Hand If --> executing in one line
if a > b : print("A is greater than B")

#Short Hand If .... Else
a = 2
b = 5
print("A is greater") if a > b else print("B is greater")

#Ternary operation / conditional expression
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Using and operator
a = 100
b = 99
c = 98
if a > b and a > c :
    print("Both conditions are true")

# OR operator
a = 200
b = 500
c = 900
if a > b or b < c :
    print("At least one conditions is true")

#Use of NOT operator
a = 30
b = 45
if not a > b :
    print("A is not greater than B")

#Nested If ----> if statements inside a if statement
x = 200
if x > 10 :
    print("X is greater than ten")
    if x > 20 :
        print("Also above tweenty")
    else :
        print("Not above tweenty")

#Pass statement
a = 20
b = 10
if a > b :
    pass