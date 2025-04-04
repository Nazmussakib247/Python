# defining a function
def my_function() :
    print("Hello World!")

#Calling a function
def myfunction() :
    print("Hello world!")
myfunction()

#Arguments
def greet(name) : #Parameter
    print("Welcome", name)
greet("Sakib") #Aeguments
greet("Rahim")

#Default arguments
def greet(name="Friend") :
    print("Hello", name)
greet()
greet("Sakib")

#Number of arguments
def full_name(first, last) : #Number of arguments must be same
    print("Full name is" , first + " " + last)
full_name("Nazmus", "Sakib")

#Arbitrary arguments (Args*)
def my_function(*Kids) :
    print("The youngest kid is " + Kids[2])
my_function("Nazmus", "Sakib", "Shawon")

#Keyword arguments
def my_function(child1, child2, child3) :
    print("The youngest child is " + child3)
my_function(child2 = "Emili", child1 = "Sakib", child3 = "Nazmus")

#Arbitrary Keyword Arguments (**kwargs)
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname="Tobias", lname="Refsnes")

#Passing a List as an Argument
def my_function(food) :
    for x in food :
     print(x)
fruits = ["Apple", "Banana", "Orange"]
my_function(fruits)

#Returns values
def my_function(x) :
    return 5 * x
print(my_function(3))
print(my_function(4))
print(my_function(5))

#The pass Statement
def my_function() :
    pass

#Positional-Only Arguments
def my_function(x, /):
    print(x)
my_function(3)

#Keyword-Only Arguments
def my_function(*, x):
    print(x)
my_function(x = 3)

#Combine Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)

#Recursion
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)  # Recursive call
        print(result)  # Print intermediate result
        return result  # Must return the result
    else:
        result = 0  # Base case (stops recursion)
        return result
print("Recursion Example Results:")
tri_recursion(6)

#Calculation in function
def add(a, b) :
    result = a + b
    return result
sum_value = add(5, 10)
print(sum_value)

    