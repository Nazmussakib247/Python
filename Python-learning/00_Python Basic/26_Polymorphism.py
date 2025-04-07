#Built In Polymorphism
print(len("Hello"))
print(len([10, 20, 30]))
print(len({"Name" : "Nazmus Sakib", "Age" : 23}))

#-----------------
#Class Polymorphism
#--------->
class car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move (self):
        print("Drive!")

class boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move (self):
        print("Sail!")
class plane :
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move (self):
        print("Fly!")

car1 = car("ford","Mustang")
boat1 = boat("Ibiza", "Touring 20")
plane1 = plane("Boieng", "747")
for x in (car1, boat1, plane1):
    x.move()

#---------------->
#Inheritance Class Polymorphism
#---------------->
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

    