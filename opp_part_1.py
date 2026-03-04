"""oop is a way of writhing code using 
ojects / real world etities
car,student,bank account etc are all objects
each object has it'own properties and methonds
arttributes(data):name ,age,balance
methods(actions):drive(),study(),withdraw() etc
class is a blue print of an object
it is a user defined data type
that has it's own attributes and methods

constructor :
it's a special method that is used to 
initialize the attributes of an object automatically
when we create an object of a class
in java constructor name is same as class name 
but in python constructor name is __init__()
it takes self as first parameter and
other parameters as needed
self is a reference to the current object
it is used to access the attributes and
methods of the class

"explicit is better than implicit" -zen of python"

model : local variable only exixt inside the __init__ and erased
from memory after the execution of __init__menthod
self.model: global variable that is created in the
memory and can be accessed anywhere in the class
self act like a bridge between the local variable 
and global varibale i mean it helps store the data
in the object and access it anywhere in the class"""

# class Bike:
#     def __init__(self,model,color,brand):
#         self.model=model
#         self.color=color
#         self.brand=brand
    
#     def display(self):
#         print(f'model:{self.model},color:{self.color},brand:{self.brand}')

# bike1=Bike("Yamaha R15","Red","Yamaha")
# bike1.display()
# bike2=Bike("Honda CBR","Blue","Honda")
# bike2.display()
# print(type(bike1))

# class Car:
   
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
#         print(f'brand:{self.brand},speed:{self.speed}')
# car1=Car("BMW",200)
# car2=Car("Audi",250)   

# print(car1.brand)

"""class atribute is a variable that is shared by 
all objects of a class
self is used to refers instance/object atributes
common varialbe is used to before the def to save up
memory and it is accesed by class.atribute name
 object atribute > class atribute 
 class can store data/atributs and methods/functions

 """
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f'Name:{self.name},Age:{self.age}')
    def welcome(self):
           print("welcome", self.name)

    def getage(self):
         print('your age is',self.age)
        
s1=student('alice',24)
s1.welcome()
s1.getage()
