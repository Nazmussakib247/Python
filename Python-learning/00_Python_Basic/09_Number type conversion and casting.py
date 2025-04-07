#Number and type conversion
a = 1 #int
b = 2.06 #float
c = 4j #Complex 

# veryfing type of using type() function

print(type(a))
print(type(b))
print(type(c))

#Convert from one type to another
 
x = float(a)
y = int(b)
z = complex(a)
print(x)
print(y)
print(z)

# getting type of 
print(type(x))
print(type(y))
print(type(z))

#Random number using random module

import random
print(random.randrange(1,100))


