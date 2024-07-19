import random

print("Welcome to the word guessing game!!")

#establecer variables
list = ["apple", "strawberry", "pinnaple", "watermelon", "orange"]
word = random.choice(list)
guess_count = 0
first_hint = ['_'] * len(word)
print('Your hint is:', ' '.join(first_hint))

#funciones del juego
while True:
    guess = input("What is your guess: ").lower()
    if len(guess) != len(word):
        print(f"Your guess must be {len(word)} letters long. Try again.")
        continue
    
    guess_count += 1

    second_hint = []
    for i in range(len(word)):
        if guess[i] == word[i]:
            second_hint.append(guess[i].upper())
        elif guess[i] in word:
            second_hint.append(guess[i].lower())
        else:
            second_hint.append('_')
    
    print('Current hint:', ' '.join(second_hint))
    
    if guess == word:
        print(f'You guessed the secret word "{word}" in {guess_count} tries!!!!')
        break
    else:
        print('Your guess was incorrect. Try again.')
