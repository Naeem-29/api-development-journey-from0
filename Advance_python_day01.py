"""walrus operator := it's a assignment
assigns a value to a variable and returns
that value in the same expression

"""
# data = input()
# while data != "exit":
#     print(f"You Entered {data}")
#     data=input()

# while(data := input()) != "exit":
#     print(f"you have Entered {data}")

# a=5
# name="valvalde"
# n : int =5
# nam : str="vini"
# print(type(a),type(name),type(n),type(nam))

# def sum(a: int,b: int)-> int :
#     return a+b

# print(sum(6,7))
#  # this will return int value 

"""matchcase is similar to switchcase"""

# day=int(input("Enter day:"))

# match day:
#     case 1:
#         print('sat')
#     case 2:
#         print('sun')
#     case 3:
#         print('mon')
#     case _:
#         print('invalid')

"""Error handling :
it lets us catch the error that occur and continuing
running the code . in general cases if error occurs code
stop running there.
there is syntax error and then 
there is Exceptions which is runtime error
ex: 10/0 -> zerodivisionError , int("abc") -> valueError
we can catch these error and run the code continuously 

try:
    risky code
except:
    handle_error
    
    """

# try:
#     num=int(input("Enter number:"))
#     print(100/num)
#     # so here if num =0 then except block will catch the error 
# except:
#     print("something went wrong")

# try: 
#     n =int(input("Enter the number:"))
#     print(100/n)
# except ZeroDivisionError:
#     print("Cannot divided by Zero")
#     #if n=0 this block will run
# except ValueError:
#     print("Please enter a valid number")
#     #if n= something other than integer then this block will run
"""multiple exceptions"""
# try: 
#     n =int(input("Enter the number:"))
#     print(100/n)
# except (ZeroDivisionError,ValueError):
#     print("Invalid")

"""at the end of try execpt block else is used to 
say that there was no error if no error occurs so else block
runs"""
# try:
#     num = int(input("Enter number: "))
#     result = 10 / num

# except ZeroDivisionError:
#     print("Division by zero")

# else:
#     print("Result:", result)

"""finally : always runs it is used to close the files,
database connections,cleaning resources
raise : is used to crash the program"""

# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# if(b==0):
#     raise ZeroDivisionError("Can't divided by zero")
# else:
#     print(f"Answer : {a/b}")
"""when we run a python file directly __name__="__main__"
but when we import that file as module in another file 
__name__=="<filename>" 

if __name__==__main__ is used to control what runs code inside that
runs only when the file is executed directly
code inside that if __name__==__main__ block if the file is
imported as a module"""

"""list comprehension"""
# l1=[1,2,3,4,5,6]

# l2=[]
# for i in l1 :
#     l2.append(i*i)

# print(l2)

# l3=[i*i for i in l1]

# print(l3)




