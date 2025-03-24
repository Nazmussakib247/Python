#String_Method
#All string methods return new values. They do not change the original string.

#Converts the first character to upper case
txt = "hello good people"
print(txt.capitalize())

#Converts string into lower case
txt = "Hello,Im Sakib,Nazmus Sakib"
print(txt.casefold())

#Returns a centered string
txt = 'Apple'
print(txt.center(30))

#Returns the number of times a specified value occurs in a string
txt = "I love Apple, Apple is my fav. An apple a day keeps the doctor away"
print(txt.count("apple"))

#Returns an encoded version of the string
txt = "Sakib"
print(txt.encode())

#Returns true if the string ends with the specified value
txt = "I'm Nazmus Sakib"
print(txt.endswith("a"))

#Sets the tab size of the string
txt = "H\tE\tL\tL\tO"
print(txt.expandtabs(4))

#Searches the string for a specified value and returns the position of where it was found
txt = "Im Nazmus Sakib Shawon, the NOOB coder"
print(txt.find("a"))

#Using index
txt = "Im Nazmus Sakib Shawon, the NOOB coder"
print(txt.index("a"))

#Formats specified values in a string
txt = "Hello,Im SakiB"
print(txt.format())

#Formats specified values in a string
txt = "Hello,Im SakiB"
print(txt.format_map())

#

