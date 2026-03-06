"""static methods are methods
that doesn't use self as parameter
they work at class level not at 
object level
@staticmethod is used to declare 
static method"""

# class Student:
#     def __init__(self,name,sub1,sub2,sub3):
#         self.name=name
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
#     # def hello():
#     #     print("Hello from student class")
#         #hello() will give error
#     @staticmethod # this is a decorator
#     def helloright():
#         print("aibar thik acche")
#         # this won't give error
#     def avg(self):
#         avg=(self.sub1+self.sub2+self.sub3)/3
#         print(f"{self.name} your Average marks is {round(avg)}")

# student=Student("John",80,90,85)
# student.avg()
# student.helloright()

"""decorator is way to modify the behaviour of 
the function without changing the actual
code of the function it is like
wrapping a function with another function to add
some extra functionality to it.it follows DRY 
principle means don't repeat yourself
"""

"""Abstraction"""
"""it hides the implementation details of a class
and only shows the essential features to the user
"""
"""Encapsulation is the process of wrapping data and
methods into a single unit called class
working with class and object is actually encapsulation
"""
"""abc module is used to create abstract classes
And ABC is that abstract base class
"""
# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(Self):
#         pass
#     @abstractmethod
#     def dangerlevel(Self):
#         pass
#     @abstractmethod
#     def loyalty(Self):
#         pass
"""this is telling us that any class that
    inherites from animal class must implemnet
    make_sound method i mean it is the base class animal
    and others will be called subclass 
    and they musht implement the make_sound methond in them
    otherwise this will throw error"""
# class Dog(Animal):
#     def make_sound(Self):
#         print("bhaw bhaw")
#     def dangerlevel(Self):
#         print("High if street dog")
#     def loyalty(Self):
#         print("highly loyal")
# class Cat(Animal):
#     def make_sound(Self):
#         print("meow meow")
#     def dangerlevel(Self):
#         print("low")
#     def loyalty(Self):
#         print("Cute but halara orom loyal na")


# dog=Dog()
# cat=Cat()
# dog.make_sound()
# dog.dangerlevel()
# dog.loyalty()
# cat.make_sound()
# cat.dangerlevel()
# cat.loyalty()

"""Practice 1 — Employee Salary System"""

# from abc import ABC,abstractmethod
# class Employee(ABC):
#     @abstractmethod
#     def calculate_Salary(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self,name,salary):
#                self.name=name
#                self.salary=salary

#     def calculate_Salary(self):
#           print(f"{self.name.upper()} your salary is : {self.salary}")

# class PartTimeEmployee(Employee):
#     def __init__(self,name,hours_worked,hourly_rate):
#         self.name=name
#         self.hours_worked=hours_worked
#         self.hourly_rate=hourly_rate

#     def calculate_Salary(self):
#         salary=self.hours_worked*self.hourly_rate
#         print(f"{self.name.upper()} your salary is : {salary}")
    
# e1=FullTimeEmployee("naeem",30000)
# e2=PartTimeEmployee("sajib",20,500)
# e1.calculate_Salary()
# e2.calculate_Salary()

"""Practice 2 — Notification System"""

# from abc import ABC,abstractmethod
# class Notification(ABC):
#     @abstractmethod
#     def send(self,message):
#         pass

"""method in class always needs 
    self as parametheras the first parameter
    so when ever a method needs to access
    the objects attributes use self 

    if we dont want to use self the we can use 
    @staticmethod decorator to declare a static method
    but it doens't follow the oop principles it's just
    like another fuction in the class that doesn't have
    access to the objects attributes
    """
# class Email(Notification):
#     def send(self,message):
#         print(f"sending Email : {message}")
# class SMS(Notification):
#     def send(self,message):
#         print(f"sending SMS : {message}")
# class PushNotification(Notification):
#     def send(self,message):
#         print(f"sending Push Notification : {message}")

# n1=Email()
# n2=SMS()
# n3=PushNotification()
# n1.send("Hello from Email")
# n2.send("Hello from SMS")
# n3.send("Hello from Push Notification")

"""Practice 3 — Payment Gateway System """

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class creditCardPayment(Payment):
     def pay (Self,amount):
         print(f"Paid {amount} using Credit Card")
     def refund(self,amount):
         print(f"Refunded {amount} to Credit Card")
class PayPalPayment(Payment):
     def pay (Self,amount):
         print(f"Paid {amount} using PayPal")
     def refund(self,amount):
         print(f"Refunded {amount} to PayPal")

cc=creditCardPayment()
pp=PayPalPayment()
cc.pay(100)
cc.refund(50)
pp.pay(200)
pp.refund(75)