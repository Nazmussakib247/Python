#create class
class MyClass:
    x = 5

#Creating object
object1 = MyClass()
print(object1.x)

#The __init__() Function
class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
p2 = Person("Doe", 50)
print(p1.name)
print(p1.age)
print(p2.name, p2.age)

#The __str__() Function
class person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = person("Nazmus Sakib", 23)
print(p1)

#Object Methods
class person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age
    def myfunction(self) :
        print("Hello my name is " + self.name)
p1 = person("Nazmus Sakib", 23)
p1.myfunction()

#The self Parameter
class person :
    def __init__(parameter, name, age) :
        parameter.name = name
        parameter.age = age
    def myfunction(abc) :
        print("Hello I'm " + abc.name)
p1 = person("Shawon", 23)
p1.myfunction()

#Modify Object Properties
class person :
    def __init__(parameter, name, age) :
        parameter.name = name
        parameter.age = age
    def myfunction(abc) :
        print("Hello I'm " + abc.name)
p1 = person("Shawon", 23)
p1.age = 999
print("Updated Age is", p1.age)

#Delete Object Properties
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1.age
print(p1.age)
'''
#Delete Objects
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
del p1
print(p1)
'''

#The pass Statement
class person :
    pass 