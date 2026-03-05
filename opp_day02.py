"""create student class that takes
name & marks of 3 subjects as
arguments in constructor
then create a method to print the average
"""
class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
    
    def average(self):
        avg=(self.sub1+self.sub2+self.sub3)/3
        print(f"Average marks of {self.name} is {round(avg)}")

Students=[]
while True:
    Name=input("Enter name/exit:")

    if Name.lower()=='exit':
     break

    sub1=int(input('Marks of sub1: '))
    sub2=int(input('Marks of sub2: '))
    sub3=int(input('Marks of sub3: '))
    student=Student(Name,sub1,sub2,sub3)
    Students.append(student)

for student in Students:
   student.average()
