print()
print()
print("Welcome to the Adventure game!")
print("This is a decision-based game where you have to choose between the options to guide the lost camper throught the forest, choose wisely and good luck!")


print()
print(".............................")
camper=input("What is your name, camper?").lower
print()
#start
choice1=input(f"Once upon a time, as nightfall was beginning to set, {camper} got separated from the group and saw flashing lights like fireflies, do you get CLOSE or get AWAY?").lower
print()
if choice1=="CLOSE":
    choice2=input(f"You get close, {camper}, and realize that it is hundreds of fairies dancing! Do you TALK to them or DANCE with them?").lower
    if choice2=="TALK":
        print()
        choice3=input(f"You talk and tell them about your situation, the fairy queen says that you could spend the night with them or they could return you with your group now, do you spend the NIGHT or RETURN to the camp?").lower
        if choice3=="NIGHT":
            print(f"The party goes on and you get to dance all night, eat and talk with them, then you fall asleep and wake up in your camp")
            print()
            choice4=input(F"Hey camper {camper}, Did you like the game? YES or NO .").lower
            if choice4=="YES":
                print(f"Thank you {camper}!")
                print()
            elif choice4=="NO":
                print(f"Oh, too bad, bye {camper}!")
                print()
            else:
                print("Oops! That is not an option, begin the game again")
        if choice3=="RETURN":
            print("They all start leading you to the right path, but in the way, they continue partying and you start to sing and dance with them and get distracted. The party goes on and you get to dance all night, eat and talk with them, then you fall asleep and wake up in your camp")
            print()
            choice4=input(F"Hey camper {camper}, Did you like the game? YES, NO.").lower