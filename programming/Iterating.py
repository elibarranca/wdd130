word = "commitment"

favorite= input("What is your favorite letter? ")

for letter in word:

    if letter.lower() == favorite.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:

    if letter.lower() == favorite.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()