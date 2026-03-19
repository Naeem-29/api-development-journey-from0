"""An iterator is an obejct that 
returns value one by one """
# numbers=[1,2,3,5,6,7]
# it=iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for i in numbers:
#     print(i)

"""return: stops function
yield: pauses function """

# n=int(input("Enter Range:"))
# def count(n):
#     i=1
#     while n>i :
#         yield i
#         i+=1
# for x in count(n):
#     print(x)

# num=[x*x for x in range(10)] #it's a list
# print(num) 
# num_2=(x*x for x in range(10)) #it's a generator it doesn't store everything in memory 
# print(num_2)
# print(type(num_2))