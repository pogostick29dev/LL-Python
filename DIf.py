grade = input("What is your grade?\n").upper()

if grade == "A":
    print("Amazing job!")

elif grade == "B":
    print("Good job!")

elif grade == "C":
    print("Average.")

elif grade == "D":
    print("Could have done better.")

elif grade == "E":
    pass

elif grade == "F":
    print("You have failed.")

else:
    print("Invalid input.")

number = int(input())

if number == 1 or number == 2:
    print("It's 1 or 2.")

else:
    print("It's neither 1 nor 2.")