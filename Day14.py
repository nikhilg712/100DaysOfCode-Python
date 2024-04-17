# Day 14 Project - Higher or Lower Game

import random

indian_celebrities = [
    "Shah Rukh Khan",
    "Salman Khan",
    "Virat Kohli",
    "Akshay Kumar",
    "Deepika Padukone",
    "Amitabh Bachchan",
    "Ranveer Singh",
    "Priyanka Chopra",
    "Aamir Khan",
    "MS Dhoni",
    "Hrithik Roshan",
    "Shahid Kapoor",
    "Alia Bhatt",
    "Kareena Kapoor Khan",
    "Ajay Devgn",
    "Anushka Sharma",
    "Rohit Sharma",
    "Katrina Kaif",
    "Varun Dhawan",
    "Ranbir Kapoor"
]

decreA = 19
decreB = 19

indexA = random.randint(0,decreA)
indexB = random.randint(0,decreB)

while indexB == indexA:
    indexB = random.randint(0, 19)


compareA = indian_celebrities[indexA]
compareB = indian_celebrities[indexB]

A = f"compare {compareA}'s instagram followers"

B = f"compare {compareB}'s instagram followers"

print(A)
print("v/s")
print(B)

input("type A or B")

