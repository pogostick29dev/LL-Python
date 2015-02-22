import random

i = -1
answer = random.randint(1, 100)

while i != answer: # while not input == answer
    try:
        i = int(input("Enter your guess.\n"))

    except ValueError:
        print("Invalid input.")
        continue

    if i > answer:
        print("Too high.")

    elif i < answer:
        print("Too low.")

print("Correct!")