print("POSITIVE NUMBER")

positive=float(input("Please type a positive number:"))

while positive < 0:
    print("Sorry, that is a negative number. Please try again.")
    positive=float(input("Please type a positive number:"))

print(f"The number is {positive}")


mom =""

while mom != "yes":
    mom=input("May I have a piece of candy? ")

print ("Thank you")