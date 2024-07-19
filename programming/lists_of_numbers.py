import math
#set directions
print("Enter a list of numbers, type 0 when finished.")

#variables
numbers = []
sum_numbers = 0
count= 0
max_number = None
number=None

#set funtions set for sum
while number !=0:
    number = float(input("Enter number: "))
    if number != 0:
        numbers.append(number)
        count += 1

for number in numbers:
    sum_numbers += number

    if max_number is None or number > max_number:
        max_number = number
#results
    if count >0:
        average =sum_numbers / count
    else:
        average = 0


print(f"The sum is: {sum_numbers} ")
print(f"The average is: {average}")
print(f"The largest number is: {max_number} ")