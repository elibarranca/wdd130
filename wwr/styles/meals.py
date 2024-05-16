import math
print("Please enter the following information:")
print()
# meals prices#
child= float(input("What is the price of a child's meal?$"))
print()
adult= float(input("What is the price of an adult's meal?$"))
print()
# quantity of people#
children= int(input("How many children are there?  "))
print()
adults= int(input("How many adults are there?  "))
print()
#tax#
tax= float(input("What is the sales tax rate?%"))
print()
#subtotal#
subtotal=((child*children)+(adult*adults))
print(f"Subtotal: {subtotal}")
#totals#
tax_total=tax/100
total=(subtotal*tax_total)+subtotal
print(f"Total:${total} ")
print()
#payments#
payment= float(input("What is the payment amount?$"))
print(f"Change:$ {payment-total}")