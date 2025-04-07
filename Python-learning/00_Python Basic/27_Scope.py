#Local scope
def myfunction():
    x = 300
    print(x)
myfunction()

#Function Inside Function
def myfunction():
    x = 300
    def myinnerfunction():
        print(x)
    myinnerfunction()
myfunction()

#Global Scope
x = 300293092
def myfunction():
    print(x)

myfunction()
print(x)

#Naming Variables
x = 3007
def naming():
    x = 200
    print(x)
naming()
print(x)

#Global Keyword
def myfunc():
    global x
    x = 999
myfunc()
print(x)

#Change the value of global variable
def myfucn():
    global x
    x = 10000
myfucn()
print(x)

#Nonlocal Keyword
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())