print('Welcome to the Shopping Cart Program!')

#list
shopping_list = []
options = 0

#loop
def display_menu():
    print('\nPlease select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')

def add_item_with_price():
    item = input('What item would you like to add? ')
    price = float(input(f"What is the price of '{item}'? "))
    shopping_list.append((item, price))
    print(f"'{item}' with price ${price:.2f} has been added to the cart.")

while True:
    display_menu()
    options = int(input('Please enter an action (1-5): '))

    if options == 1:
        add_item_with_price()

    elif options == 2:
        print('\nYour shopping cart contains:')
        if len(shopping_list) == 0:
            print('Your shopping cart is empty.')
        else:
            for index, (item, price) in enumerate(shopping_list, start=1):
                print(f"{index}. {item} - ${price:.2f}")

    elif options == 3:
        if len(shopping_list) == 0:
            print('Your shopping cart is empty.')
        else:
            print('\nCurrent items in your shopping cart:')
            for index, (item, price) in enumerate(shopping_list, start=1):
                print(f"{index}. {item} - ${price:.2f}")

            try:
                remove_index = int(input('Which item would you like to remove? Enter item number: '))
                if 1 <= remove_index <= len(shopping_list):
                    removed_item = shopping_list.pop(remove_index - 1)
                    print(f"'{removed_item[0]}' has been removed from the cart.")
                else:
                    print('Invalid item number. Please try again.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    elif options == 4:
        if len(shopping_list) == 0:
            print('Your shopping cart is empty. No total to compute.')
        else:
            total = sum(item[1] for item in shopping_list)  
            print(f'\nThe total price of items in your shopping cart is: ${total:.2f}')

    elif options == 5:
        print('Thank you for using the shopping cart program. Goodbye!')
        break

    else:
        print('Invalid option. Please enter a number between 1 and 5.')

print()