# name="kodhu"
# age=23
# height=5.6
# is_jobless=True
# print(type(name),type(age),type(height),type(is_jobless))

# num_str="123"
# num_int=int(num_str)
# num_float=float(num_str)
# print(num_int,num_float)

# a=10
# b=3
# print(a+b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)

# text= "python"
# print(text.lower())
# print(text.upper())
# print(text[2])
# print(text[1:4])

# wishlist=["hiking","camera","makingcinema"]
# wishlist.append("Himachalpradesh")
# # print(wishlist)
# # wishlist.remove("hiking")
# # print(wishlist.index("camera"))
# print(wishlist.reverse())
# # print(wishlist.sort())
# my_message="booby's hosue"
# m="hello i am good for nothing trying to do something" \
# "i donnno if it's gonna work for me or not ouh i can write " \
# "so fast that's a skill right " \
# "hahah making myself happy with false assumption"
# print(my_message)
# print(m)
# print(len(my_message))
# print(len(m))
# print(m[3:55])
# print(my_message[1:7])
# print(m.count('o'))
# new_m=m.replace('i','you')
# print(new_m)
# #print(help(str))

# num_1='100'
# num_2='100.45'
# n_1=int(num_1)
# n_2=float(num_2)
# print(round(n_2,1))
# print(round(n_2))

# course=['HIstory','physics','math','bal']
# print(len(course))
# print(course[-1])
# print(course)
# course.append('accounting')
# print(course)
# print(course[1:5])
# course.insert(2,'Art')
# print(course)
# couse_2=['film','media','religion']
# course.extend(couse_2)
# print(course)
# lastval=course.pop()
# print(lastval)
# course.reverse()
# print(course)
# num=[5,63,1,3,6,90]
# num.sort()
# print(num)
# course.sort()
# print(course)
# sorted=sorted(course)
# print(sorted)
# print(min(num))
# print(max(num))
# print(sum(num))
# print(3 in num)
# for index, item in enumerate(course):
#     print(index,item)

# for item in course:
#     print(item)

# for i,item in enumerate(course,start=4):
#     print(i,item)

# course_intostring='-'.join(course)
# print(course_intostring)

# backtolist=course_intostring.split('-')
# print(backtolist)

# #list are mutable
# l_1=['history','math','art','media']
# l_2=l_1
# l_1[0]='bangla'
# print(l_1,l_2)
# #tuple aren't mutable so can't be modified
# # tuple_1=('history','math','art','media')
# # tuple_2=tuple_1
# # tuple_1[0]='bangla'
# # print(tuple_1,tuple_2)

# #sets are values that are unordered and have no duplicates
# #eliminates the duplicates doesn't count them

# set_1={1,2,2,3,7,8,3,14}
# set_2={1,2,3,3,7,8,9}

# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))
# print(set_1.union(set_2))

# #empty lists
# em_list=[]
# em_list=list()
# #empty tuples
# em_tuple=()
# em_tuple=tuple()
# #empty sets
# em_set={}  # this line isn't right it will create a dic
# em_set=set() #this creates a empty set

# #Dictionaryyy--keys and values

# student={'name':'june','age':23,'subs':['art','math']}
# print(student['name'],student['subs'])

# s={1:'june',2:23,3:['art','math']}
# print(s[1],s[2],s[3])
# print(s.get(1))
# #print(s[4]) #will trow error
# s[4]='phone'
# s[1]='jane'
# print(s.get(4),s[1]) #instead of error will return none
# print(s)
# del s[4]
# print(s)
# age=student.pop('age')
# print(age)
# print(s.keys())
# print(s.values())
# print(s.items())
# print(len(s))

# for key in s:
#     print(key)
# for key,value in student.items():
#     print(key,value)

#conditionals
# lan=input('Enter lan:')
# if lan =='java':
#     print('lan is java')
# elif lan =='python':
#     print('lan is python')
# elif lan=='js':
#     print('lan is js')
# else:
#     print('invalid')

# user='Admin'
# logged_in=False
# if user=='Admin' or logged_in:
#     print('Admin page')
# else:
#     print('Bad creds')

#  for object identity use : is

# a=[1,2,3]
# b=[1,2,3]
# print(a==b) #true
# print(a is b) # false cz they are diff object in mem
# print(id(a))
# print(id(b))

# a=[1,2,3]
# b=a
# print(a==b) #true
# print(a is b) #true
# print(id(a))
# print(id(b))

#none ,false,zero,'',(),[],{} evaluates False
#input always returns strings 
#number=int(input('Enter number':)) to take integer input 
# condition= False/()/{}/[]/None
# if condition : 
#     print('True')
# else:               # this block will print False
#     print('False')

# nums=[1,2,3,4,5,6,7]

# for val in nums:
#     if val==3:
#         print('3 founded continue')
#         continue
#     if val==4:
#        print('4 founded')
#        break
#     print(val)

# for val in nums:
#     for letter in 'abc':
#         print(val,letter)

#for iteration

# for i in range(1,11):
#     print(i) 

# x=1
# while x<11:
#     print(x)
#     x+=1

# fucntions : advantage - resuability of code,keeping code dry

# def helo_func():

#     print('hello world')

# helo_func()

# def hello():
#     return 'hello'
# print(hello().upper())

# def func(greeting):
#     return f"{greeting} Fucntion"
# print(func('HI'))

# def sum(a,b):
#     return a+b
# print(sum(10,10))

# def dif(a,b):
#     print(a//b)
# dif(10,5)

# # *args collects postinal arguments stores them as tuple ()
# # **kwargs collects keyword arguments stores them as dic {}

# def st_info(*args,**kwargs):
#     print(args)
#     print(kwargs)
# st_info('math','art',name='jane',age=23)

# m=[0,31,28,31,30,31,30,31,31,30,31,30,31]

# def leapyear(year):

#  return year % 4 ==0 and (year%100 !=0 or year%400==0)


# def daysINmonth(year,month):
 
#  if not 1<=month<=12 :
#   print('invalid')

#  if month ==2 and leapyear(year):
#     return 29

#  return m[month]

# print(daysINmonth(2002,2))


"""import module"""
#import first
#import first as f 
#from first import find_index as f , test
# from first import *
# import sys
# import random
# courses=['history','math','art','compsci']

# index=find_index(courses,'art')
# print(index)
# print(test)
# print(sys.path)
# random_course = random.choice(courses)
# print(random_course)

# import math
# rads=math.radians(45)
# print(math.sin(rads))

# import datetime
# import calendar
# today=datetime.date.today()
# print(today)
# print(calendar.isleap(2024))

# import os
# print(os.getcwd())

""" os module """
# import os 
# from datetime import datetime
# #print(dir(os))

# #os.mkdir('os_module') #to create a folder
# #os.makedirs('os module/sub-os module') # to create multilevel
# #os.rmdir('os_module')
# #os.removedirs('os module/sub-os module')
# #os.rmdir('os_module')
# #os.rename('os module','lawra')
# # mod_time=os.stat('lawra').st_mtime
# # print(datetime.fromtimestamp(mod_time))


# for dirpath,dirnames,filenames in os.walk(os.getcwd()):
#     print('Current path:',dirpath)
#     print('directores',dirnames)
#     print('Files:',filenames)
#     print()

# print(os.listdir())
# lines=['hey man you got this \n '
#     'one year is lot \n ' 
#     'you can do it \n' 
#     'i mean you have got no other choice ']
# with open("text.txt",'w') as file:
#     file.writelines(lines)

