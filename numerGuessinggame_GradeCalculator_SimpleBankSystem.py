"""Guessing number Game"""
# import random
# n=random.randint(1,100)
# a=0
# guess=0
# while (a!=n):
#     guess +=1
#     a=int(input("Guess the number: "))
#     if (a>n):
#         print("Lower")
#     else:
#         print("Higher")
    
# print(f"you took total {guess} attempts \n to guess the correct number which is: {n}")

"""Student Grade Calculator:

Takes 5 marks from the user

Stores them in a list

Calculates the average

Prints the grade"""

# Marks=[]
 
# for mark in range(5) :
#    mark=int(input("Enter Mark:"))
#    Marks.append(mark)
# print(Marks)

# average=sum(Marks)/5
# print(f"Average: {average}")
      
# def Grade():
#     if(average<50):
#         print("Grade : F")
#     elif(average>=50 and average <60):
#         print("Grade : D")  
#     elif(average>=60 and average <70):
#         print("Grade : C")
#     elif(average>=70 and average <80):
#         print("Grade : B")
#     else :
#         print("Grade : A")

# Grade()

"""Bank Account Simulator"""

# print("1 : To Deposite \n2 : To Withdraw \n3 : To Check_Balance \nTo Exit Engter other than 1,2,3")
# Balance=1000
# n=0
# def Deposit ():
#     global Balance
#     n=int(input("Enter amount :"))
#     Balance=Balance+n
#     print(f"Balance: {Balance}")

# def Withdraw ():
#     global Balance
#     n=int(input("Enter amount :"))
#     if n > Balance :
#        print("Error")
#     else:
#        Balance=Balance-n
#        print(f"Balance: {Balance}")

# def check_balance():
#      global Balance
#      print(Balance)
# def Exit():
#      global Balance
#      print("Exit")

# while True :
#     choice=int(input("Choice :"))
#     if(choice==1):
#       Deposit()
#     elif(choice==2):
#      Withdraw()
#     elif(choice==3):
#      check_balance()
#     else:
#       print("Exit")
#       break
