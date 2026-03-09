"""del is used to delete any attribute of
an object or to delete and entire object itself"""
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age
#     def info(self):
#         print(f"name is {self.name} and age is {self.__age}")
# s1=student('john',20)
# print(s1.name)
# print(s1.age)
# print(s1)
# del s1.age
# print(s1.age)# will throw an error 
# print(s1.name)
# del s1
# print(s1)#will throw an error 
# print(s1.__age) # will throw an error
# print(s1.info()) # will run 

"""here in that code the attributes we used are
public attributes we can access them outside the clas
but if we want to make them private attributes
then we use __ before the attribute and it won't be 
possible to access them outside the class it applys
making a method private too __ can be used to 
private methods and those methods and attribute
can only be used within that function"""

# class person:
#     __name="none"
#     def __hello(self,__name):
       
#        print(f"Hello {__name}")
#     def info(self):
#         self.__hello(self.__name)
# p1=person()
# p1.info()

# class person:
#     __name="none"
#     def __hello(self,name):
       
#        print(f"Hello {name}")
#     def info(self):
#         self.__hello("john")
# p1=person()
# p1.info()
# print(p1.__name) # will throw an error
# print(p1.__hello()) # will throw an error

"""Inheritence :
it's like maintaining the order 
parent class and then child classes are the 
classes which are derived from the parent class
and used it's methods and attributes

"""
class Bike :
    @staticmethod
    def start():
        print("Bike is starting")
    @staticmethod
    def stop():
        print("Bike is stopping")
class honda(Bike):  # (Bike) by this we are inheriting the parent class bike
    def __init__(self,name):
        self.name = name
        print(f"This is {self.name} bike")
h1=honda("hero")
print(h1.name)
print(h1.start())
print(h1.stop())



