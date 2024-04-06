# concept learnt- Function with inputs

# def greet(name):
#     return name+1

# print(greet(123))  


# Day 8 Project - Caesar Cipher

def encrypt():
    word = input("Enter the word you want to cipher\n").lower()
    shift = int(input("enter the amount of shift\n"))
    initialLetterList = []

    for letter in word:
        initialLetterList.append(ord(letter))

    for i in range(len(initialLetterList)):
        initialLetterList[i] += shift

    wordArray = []
    for ascii in initialLetterList:
        wordArray.append(chr(ascii))

    word = "".join(wordArray)    
    print("the ciphered word is:",word)

def decrypt():
    word = input("Enter the word you want to cipher\n").lower()
    shift = int(input("enter the amount of shift\n"))
    initialLetterList = []

    for letter in word:
        initialLetterList.append(ord(letter))

    for i in range(len(initialLetterList)):
        initialLetterList[i] -= shift

    wordArray = []
    for ascii in initialLetterList:
        wordArray.append(chr(ascii))

    word = "".join(wordArray)    
    print("the ciphered word is:",word)



wish = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")

if wish == "encode":
    encrypt()
else:
    decrypt()    

