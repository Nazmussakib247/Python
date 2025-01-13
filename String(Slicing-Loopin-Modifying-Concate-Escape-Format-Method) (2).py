#String in double qoutes and single qoutes
print("Hello sakib")
print('Hello Sakib')

#Qoutes inside qoute
print("it's Alright boy")
print("He is called 'The retake king'")
print('He is called "The retake king')

#Assign string to a variable
a = "Hello programmer"
print(a)

#Assigning multiple string to a variable
m = """Hey, myself sakib, Nazmus Sakib Shawon. I'm
Learning python from basic to advance. My target is to
Become a Data scientists or ML expert .
Let's See how far I can go"""
print(m)

m1 = '''But now the target is passing semister and
clearing my retake and having fully efficiency in python
within 10 Weeks, But InShaAllah i'll make it before 
10 weeks.'''
print(m1)

#Ascessing element of string
print(a[15]) #first character is 0

#Looping through a string.
for char in a:
    print(char)

for word in a.split():
    print(word)

#getting word length
print(len(a))

#Checking string 
print("Sakib" in a)

#Using If statement 
if "programmer" in a:
    print("Found it")

#Checking If Not
print("Python" not in a)

#Usinging If Not statement
if 'Python' not in a:
    print("Not found")


