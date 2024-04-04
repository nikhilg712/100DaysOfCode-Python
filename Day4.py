# Day 4 project Stone Paper Scissor
# concept learnt - Random module and Lists

import random

computerMove = random.randint(1,10)  

myMove = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))

if(myMove==0 and 1<=computerMove<=3):
    print("It's a tie")
elif(myMove==0 and 3<computerMove<=6):
    print("You won. You chose Rock Computer chose Scissors")
elif(myMove==0 and 6<computerMove<=10):
    print("You lose. You chose Rock Computer chose Paper")

if(myMove==1 and 1<=computerMove<=3):
    print("You Won. You chose Paper Computer chose Rock")
elif(myMove==1 and 3<computerMove<=6):
    print("It's a tie")
elif(myMove==1 and 6<computerMove<=10):
    print("You lose. You chose Paper Computer chose Scissors") 

if(myMove==2 and 1<=computerMove<=3):
    print("You lose. You chose Scisssors Computer chose Rock")
elif(myMove==2 and 3<computerMove<=6):
    print("You Won. You chose Scissors Computer chose Paper")
elif(myMove==2 and 6<computerMove<=10):
    print("It's a tie")            
