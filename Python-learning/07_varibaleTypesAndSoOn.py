Age=10
AGE=11
age=12
#3 different variables cause variables are case sensitive

#Variable name with more than one word
myNameIs="Nazmus Sakib shawon"
#This is camel case,Each word except the first word start with capital letter

MyVariableName="Ki j dibo"
#Pascal case, each word start with capital letter

my_variable_name="Shawon"
#Snake case, each word separated with an underscore

x, y, z="Orange", "Apple", "Banana"
print(x), print(y), print(z)
#Many values to multiple variable in one line

a=b=c="Grape"
print(a), print(b), print(c)
#One value to multiple variables in one line

fruits=["Jackfruit","Malta","Mangoes"]
P, Q, R = fruits
print(P,Q,R)
#Unpacking a collection

A='Python '
B='is '
C='Awesome'
print(A+ B+ C)
#Printing multiple variable using + operator

H=90
V=80
print(H+V)
# For numbers + operator work as mathmatical operator

k=100
l=" that's my math marks"
print(k,l)
# Using comma to print different data types variable 

x='Awesome'

def myfunc():
    x='Hard'
    print("C/C++ is " + x)
myfunc()

print("Python is " + x)
#Using global variable and local variable 

def myfunction():
    global N
    N = "I love python that's why I'm learning it"
myfunction()
print(N)
# Creating a global variable inside a function using keyword "global"

w = 'CSE'
def anotherfunction():
    global w
    w = "EEE"
anotherfunction()
print(w)
#Changing value of a global variable inside a function 


