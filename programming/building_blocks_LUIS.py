import random

print('Welcome to the word guessing game!')

# List of words (separated by commas)
list_o_words = ['taco', 'pasta', 'apple', 'pie', 'hamburger', 'pizza', 'fries']

# Choose a random word from the list
x = random.randint(0, len(list_o_words) - 1)
secret_word = list_o_words[x]

guess_count = 0

while True:
    guess = input('Enter your guess: ')
    guess_count += 1

    if guess.lower() == secret_word:
        print(f'Congratulations! You guessed the secret word "{secret_word}" in {guess_count} tries.')
        break
    else:
        print('Your guess was not correct. Try again.')