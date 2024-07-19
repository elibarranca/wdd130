
print("\nAccount Information:")
for i in range(len(names)):
    print(f"{names[i]} - ${balances[i]}")

    total += balances[i]

average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
#quit to stop
