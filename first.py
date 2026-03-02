# """
# PYTHON QUICK OVERVIEW SCRIPT
# Covers most core Python basics in one file.
# """

# # =========================
# # 1. PRINTING & COMMENTS
# # =========================
# print("Hello, Python!")

# # This is a single-line comment
# """
# This is a multi-line comment (docstring)
# """

# # =========================
# # 2. VARIABLES & DATA TYPES
# # =========================
# name = "Alice"          # str
# age = 25                # int
# height = 5.6            # float
# is_student = True       # bool
# nothing = None          # NoneType

# print(type(name), type(age), type(height), type(is_student), type(nothing))

# # =========================
# # 3. TYPE CASTING
# # =========================
# num_str = "123"
# num_int = int(num_str)
# num_float = float(num_int)
# print(num_int, num_float)

# # =========================
# # 4. BASIC OPERATORS
# # =========================
# a = 10
# b = 3

# print(a + b)   # addition
# print(a - b)   # subtraction
# print(a * b)   # multiplication
# print(a / b)   # division
# print(a // b)  # floor division
# print(a % b)   # modulus
# print(a ** b)  # exponent

# # =========================
# # 5. STRINGS
# # =========================
# text = "Python"
# print(text.lower())
# print(text.upper())
# print(text[0])
# print(text[0:3])
# print(f"My name is {name} and I am {age} years old")

# # =========================
# # 6. LISTS
# # =========================
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")
# fruits.remove("banana")
# print(fruits)
# print(fruits[0])

# # List comprehension
# squares = [x**2 for x in range(5)]
# print(squares)

# # =========================
# # 7. TUPLES
# # =========================
# coordinates = (10, 20)
# print(coordinates[0])

# # =========================
# # 8. SETS
# # =========================
# unique_numbers = {1, 2, 3, 3, 2}
# unique_numbers.add(4)
# print(unique_numbers)

# # =========================
# # 9. DICTIONARIES
# # =========================
# person = {"name": "Alice", "age": 25}
# person["city"] = "New York"
# print(person["name"])
# print(person.keys())
# print(person.values())

# # Dictionary comprehension
# square_dict = {x: x**2 for x in range(5)}
# print(square_dict)

# # =========================
# # 10. CONDITIONALS
# # =========================
# if age > 18:
#     print("Adult")
# elif age == 18:
#     print("Exactly 18")
# else:
#     print("Minor")

# # Ternary operator
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# # =========================
# # 11. LOOPS
# # =========================
# for fruit in fruits:
#     print(fruit)

# for i in range(3):
#     print("Counting:", i)

# count = 0
# while count < 3:
#     print("While loop:", count)
#     count += 1

# # break & continue
# for i in range(5):
#     if i == 3:
#         break
#     if i == 1:
#         continue
#     print("Loop control:", i)

# # =========================
# # 12. FUNCTIONS
# # =========================
# def greet(name="Guest"):
#     return f"Hello, {name}"

# print(greet("Alice"))
# print(greet())

# # *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Args:", args)
#     print("Kwargs:", kwargs)

# flexible_function(1, 2, 3, name="Alice", age=25)

# # Lambda function
# multiply = lambda x, y: x * y
# print(multiply(3, 4))

# # =========================
# # 13. ERROR HANDLING
# # =========================
# try:
#     result = 10 / 0
# except ZeroDivisionError as e:
#     print("Error:", e)
# finally:
#     print("This always runs")

# # =========================
# # 14. FILE HANDLING
# # =========================
# with open("sample.txt", "w") as file:
#     file.write("Hello File!")

# with open("sample.txt", "r") as file:
#     content = file.read()
#     print(content)

# # =========================
# # 15. CLASSES & OOP
# # =========================
# class Person:
#     species = "Human"  # Class variable

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hi, I'm {self.name}"

# # Inheritance
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def greet(self):
#         return f"I'm {self.name}, ID: {self.student_id}"

# p1 = Person("Bob", 30)
# s1 = Student("Charlie", 20, "S123")

# print(p1.greet())
# print(s1.greet())

# # =========================
# # 16. MODULE IMPORTING
# # =========================
# import math
# import random

# print(math.sqrt(16))
# print(random.randint(1, 10))

# # =========================
# # 17. GENERATORS
# # =========================
# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i
#         i += 1

# for number in count_up_to(3):
#     print("Generated:", number)

# # =========================
# # 18. DECORATORS
# # =========================
# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello!")

# say_hello()

# # =========================
# # 19. MAIN CHECK
# # =========================
# if __name__ == "__main__":
#     print("This runs only if script is executed directly.")

# # =========================
# # END OF OVERVIEW
# # =========================
# print("End of Python overview!")print

print('imported')
test='Test string'

def find_index(to_search,target):
    for i,value in enumerate(to_search):
        if value==target:
           return i 
        
    return -1 