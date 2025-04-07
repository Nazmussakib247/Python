#Syntax----> lambda arguments : expression
#add two number using lamda
add = lambda x, y : x + y
print(add(3,5))

#Square function
square = lambda x : x * x
print(square(4))

#even or odd checker
is_even = lambda x : x % 2 == 0
print(is_even(8))

#sorted() + lambda
students = [("Sakib", 90), ("Rafi", 80), ("Rumi", 85)]
sorted_list = sorted(students, key=lambda x: x[1])
print(sorted_list)

#Add 10 to argument a, and return the result
x = lambda a : a + 10
print(x(20))

#Multiply arguments
x = lambda a, b : a * b
print(x(4,6))

#Summarize argument a, b, and c and return the result
x = lambda a, b, c : a + b + c
print(x(4, 5, 6))

#Use that function definition to make a function that always doubles the number you send in
def my_function(n):
    return lambda a : a * n
my_doubler = my_function(2)
print(my_doubler(78))

#Return triple that send in
def my_function(n):
    return lambda a : a * n
multiplier = my_function(3)
print(multiplier(83))

#Both function in a same program
def my_function(n):
    return lambda a : a * n
my_doubler = my_function(2)
print(my_doubler(99))
multiplier = my_function(3)
print(multiplier(830))