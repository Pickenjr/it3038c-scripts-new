import random
myNumber = random.randint(1, 100)
print("Please guess a number between 1 and 100.")
yourNumber = int(input())
while yourNumber != myNumber:
    if yourNumber > myNumber:
        print("That number is too high, please guess again.")
        yourNumber = int(input())
    elif yourNumber < myNumber:
        print("That number is too low, please guess again.")
        yourNumber = int(input())
    elif yourNumber == myNumber:
        print("That is the right number, congratulations!")
