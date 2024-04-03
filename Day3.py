# Day 3 Project- Finding the treasure

print("Welcome to the treasure island\nYour mission is to find the treasure\nYou are on a cross road where would you want to go type 'left' or 'right'")
leftOrRight = input()
if leftOrRight=='right':
    swimOrWait=input("Swim or Wait?\n")
    if swimOrWait=='Swim':
        print("game over")
    elif swimOrWait=="Wait":
        door=input("Which Door?\n")
        if door=="red":
            print("game over")
        elif door=="green":
            print("game over")
        elif door=="yellow":
            print("won")
        else:
            print("game over")
else:
    print("game over")                        


