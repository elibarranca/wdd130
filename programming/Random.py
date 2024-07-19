import random
print("Random number of the day!!")

print()

number = random.randint(1, 100)

guess= -1

while guess !=number:

    guess=float(input("What is your guess?"))
    
    if guess <number: 
        print("Higher")

    elif guess >number:
        print("Lower")

    else:
        guess == number
        print("You guessed it")

print(number)

