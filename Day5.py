# Day 5 problem - Fizzbuzz

# num = int(input("Enter the number\n"))
# if(num%3==0 and num%5!=0):
#     print("fizz")
# elif(num%5==0 and num%3!=0):
#     print("buzz")
# elif(num%5==0 and num%3==0):
#     print("fizzbuzz")
# else:
#     print("Not applicable")


# Day 5 project - Password Generator

import random

alphaList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbolList = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
numList= ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


alphabets = int(input("How many alphabets do you want in your password?\n"))
symbols = int(input("How many symbols do you want in your password?\n"))
numbers = int(input("How many numbers do you want in your password?\n"))

initialPassword = ""
for alpha in range(0,alphabets):
    initialPassword+=alphaList[random.randint(0,25)]
for symbol in range(0,symbols):
    initialPassword+=symbolList[random.randint(0,len(symbolList)-1)]
for symbol in range(0,numbers):
    initialPassword+=numList[random.randint(0,len(numList)-1)]

passwordCharacterList=[]
for char in initialPassword:
    passwordCharacterList.append(char)

password=""
a = len(initialPassword)

while len(passwordCharacterList)>0:
    r=random.randint(0,a-1)
    password+=passwordCharacterList[r]
    passwordCharacterList.remove(passwordCharacterList[r])
    a=a-1

print(password)    

