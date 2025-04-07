#Return an iterator from a tuple, and print each value
mytuple = ("Apple", "Banana", "Orange", "Jackfruit")
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Return an iterator from a string , and print each value
mystring = "Nazmus Sakib"
myiter = iter(mystring)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#Looping Through an Iterator
#Iterate the values of a tuple
mytuple = ("Apple", "Banana", "Orange")
for x in mytuple:
    print(x)

#Iterate the characters of a string
mystring = "Nazmus Sakib"
for x in mystring:
    print(x)

#Iterator inside class
class MyNumbers:
 def __iter__(self):
    self.a = 1
    return self
 
 def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#>>>>>>>>>>>>>>
#StopIteration
#>>>>>>>>>>>>>>
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)