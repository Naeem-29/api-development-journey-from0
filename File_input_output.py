"""file input output is used in 
logs, configs,data storage
it means reading from files and
writing to files"""
"""when create a file we need to specify the mode
r-read w-write a-append x-create a new file b-binary mode
and it is neccessary to close the file after use the file
if we use with then we don't need to close the file 
it wil automatically close the file after use the file"""
# file=open('text.txt','r')
# print(file.read())
# file.close()
# print(file.closed)
# print(file)

# with open('text.txt','r') as f:
#     content=f.read()
#     print(content)
#     print(content.upper())
#     print(content)
"""to read line by line"""
# with open('text.txt','r') as f:
#     for line in f:
#         print(line.strip())

"""read all lines as list"""
# with open('text.txt','r') as f:
#     lines=f.readlines()
#     print(lines)
"""when lines=f.readlines() runs it will run trough the whole file and the
    cursor will be at the end of the file so when i ran
    the next line l=f.readlines() it shows empty list
    now to fix this f.seek(0) will move the cursor to the
    beginning of the file """
    # f.seek(0)
    # l=f.readlines()
    # print(l)
 
""" lesson is when ever we need to convert the text files
 into a list we can use readlines() and store it in 
 a varible and we can use that variable whenever needed
 we don't need to do seek(0) it was just for the knowing 
 purpose"""

 # with open('text.txt','w') as f:
 #     f.write('hey man don't forget \n')
            
""" if we those lines f.write() it will delets
 the previous content so to add any line we use
 append mode 'a'
 'a+' is used to read and write both so when
 you need to add somthing and then u want to 
 read the whole file then u use a+ """

# with open('text.txt','a+') as f:
#     f.write('hey man don forget never \n')
#     f.seek(0)
#     content=f.read()
#     print(content)

# with open('text.txt','r') as f:
#     print(f.tell())
#     f.read(5)
#     print(f.tell())
#     f.seek(2)
#     print(f.tell())


""" to delete a file use
import os 
os.remove('filename')"""

# with open('practice.txt','r') as f:
#     data=f.read()
#     new_data=data.replace('java','python')
#     print(new_data)

# with open('practice.txt','w') as f:
#     f.write(new_data)
# word=input('enter the word you want to search:')
# with open ('practice.txt','r') as f:
#     data=f.read()
#     if(word in data):
#         print(f'{word} is found in the file')
#     else:
#        print(f'{word} is not found in the file')
   
   
   
# def search():
#     line_no=1
#     data=True
#     word=input('enter the word you want to search:')
#     with open ('practice.txt','r') as f:
    
#        while data:
#         data=f.readline()
#         if word in data:
#          print(f'{word} is found in line: {line_no}')
#          return  
#         line_no+=1
#     return -1
# search()
"""fininding even numbers from the file data"""
# count=0
# with open('practice.txt','r') as f:
#     data=f.read()
#     print(data)
#     print(type(data))
#     numbers=data.split(',')
#     print(numbers)
#     for val in numbers:
#         if(int(val)%2==0):
#             count+=1
#             print(val)
# print(f'count of even numbers is : {count} times')