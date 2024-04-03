# a = str(123)
# print(type(a))

# Day 2 Project: tip Calculator

print("Welcome to the Tip Calculator")
totalBill = int(input("What was the Total Bill?\n₹"))
Tip = int(input("What is the tip amount you want to give?\n₹"))
People = int(input("What is the total number of people?\n"))
print(f"Each person has to pay: ₹{((totalBill+Tip)/People)}")
