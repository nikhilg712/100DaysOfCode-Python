# Day 7 Project - Hangman

#Step 1 

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# import random

# word_list = ["aardvark", "baboon", "camel"]
# randomWord = word_list[random.randint(0,2)]
# dashArray = []
# for i in range(0,len(randomWord)):
#     dashArray.append("_")


# while "_" in dashArray:
#     guess = input("guess a letter\n").lower()
#     print(dashArray)   

#     for i in range(0,len(randomWord)):
#         if guess==randomWord[i]:
#             dashArray[i]=guess

import random

word_list = ["aardvark", "baboon", "camel"]
randomWord = word_list[random.randint(0, 2)]
dashArray = []
correctGuess = False
lives = 6

# Initialize dashArray with underscores
for i in range(0, len(randomWord)):
    dashArray.append("_")

# Keep looping until all letters are guessed
while lives!=0:
    guess = input("\nGuess a letter: ").lower()
    

    # Check if the guessed letter matches any letter in the randomWord
    for i in range(0, len(randomWord)):
        if guess == randomWord[i]:
            dashArray[i] = guess
            correctGuess = True
                
    if correctGuess:
        for letter in dashArray:
            print(letter, end=" ")
        correctGuess=False
    else:
        lives = lives-1
        print(f"incorrect guess {lives} remaining!") 
if lives==0:
    print("Hanged")
else:
    print("\nCongratulations! You guessed the word:", randomWord)







