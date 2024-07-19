#two lists of names and balances
names =[]
balances =[]

name = None

#lists
while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        names.append(name)
        balances.append(balance)

#loop throught the lists with and index and display the name of the account with the balance

print("\nAccount Information:")
total = 0

for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")

    total += balances[i]

#compute and display the total balance in all accounts and average the balance 
average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")





