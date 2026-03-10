print('type : nakki \n  dua \n  tia \n pura')
import random
computer = random.choice([1,2,3,4])
users=input('Enter you choice:')
userdir={"nakki":1,"dua":2,"tia":3,"pura":4}
reverseuserdir={1:"nakki",2:"dua",3:"tia",4:"pura"}

user=userdir[users]

print(f"you chose: {reverseuserdir[user]}\n computer chose : {reverseuserdir[computer]}")

if (computer==user):
    print('You win')
else :
    print('you lose')