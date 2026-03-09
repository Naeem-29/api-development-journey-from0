"""multilevel inheritance : it's like a chain 
of clases where the child class is derived from
the parent class and then the child class is also
a parent class for another child class and so on
super() is used to call the parent class
method from the child class and it can be used to
call the parent class constructor from the child 
class constructor"""
# class grandparent:
#     def __init__(self):
#         print("grandparent constructor")
#     def info(self):
#         print("Dada-Dadi")
# class parent(grandparent):
#     def __init__(self):
#         super().__init__()
#         print("parent constructor")
#     def msg(self):
#         print("Ma-Baba")
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#     def yo(self):
#         print("Beta-Beti")

# c1=child()
# c1.info()
# c1.msg()
# c1.yo()

"""Multiple inheritance :
child inherits from more than one 
parent """

# class A :
#     def skills(self):
#         print("AAAAAAAAAAAA")
# class B :
#     def info(self):
#         print("BBBBBBBBBBBB")
# class C(A,B):
#      def inf(self):
#          print("CCCCCCCCCCCCC")

# c1=C()
# c1.info()
# c1.inf()
# c1.skills()

# class A:
#     def __init__(self):
#         print("Class A constructor")


# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("Class B constructor")


# class C(A):
#     def __init__(self):
#         super().__init__()
#         print("Class C constructor")


# class D(B, C):
#     def __init__(self):
#         super().__init__()
#         print("Class D constructor")


# d = D()

"""polymorphism(many forms) : operator overloading 
the same function?mehtod name can behave differently
depending on the object """

# print(len("polymorphism"))
# print(len([1,24,55,6,7]))
# print(len((91,2)))

# class A :
#     def info(self):
#         print("AAAAAAAAAAAA")
# class B :
#     def info(self):
#         print("BBBBBBBBBBBB")
# class C :
#     def info(self):
#         print("CCCCCCCCCCCC")

# a1=A()
# a1.info()
# animal=[A(),B(),C()]
# print(type(animal))
# for a in animal:
#     a.info()
"""here all the classes had info() method but they 
have diffrent behavior it's polymorphism"""

"""it allows us treat the object as the other variable 
we can traverse it's methods using for in loop
. same fucntion behave differently depending on the object
calling it """
"""for object in objects:
    object.method()"""


