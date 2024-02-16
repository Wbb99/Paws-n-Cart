# Paws_n_Cart.py

# Function to display the main menu options
from tabulate import tabulate

def display_menu():
    print("\n")
    print("-" * 80)
    print("Paws n Cart Shopping Cart: ")
    print("-" * 80)
    print("Would you like to: ")
    print("1. Add an item to your cart")
    print("2. Remove an item from your cart")
    print("3. View your cart")
    print("4. Checkout")
    print("5. Exit")

# Function to add item to the cart
def add_item(cart_contents):
    item = input("\nWhat item would you like to add to your cart: ")
    price = float(input("\nHow much does the item cost: £"))
    quantity = int(input("\nEnter the quantity: "))
    cart_contents.append((item, price, quantity))
    print("\n{} has been added to your cart.".format(item, quantity))

# Function to remove an item from the cart
def remove_item(cart_contents):
    remove = input("\nWhich item would you like to remove: ")
    found = False
    for item_info in cart_contents:
        if item_info[0] == remove:
            cart_contents.remove(item_info)
            found = True
            print("\n{} has been removed from your cart.".format(remove))
            break
    if not found:
        print("\nThat item is not in your cart.")

# Function to view the contents of the cart
def view_cart(cart_contents, col_names):
    print("\nThis is your cart:")
    print(tabulate(cart_contents, headers=col_names, tablefmt="heavy_grid"))

# Function to checkout and calculate the total cost of the cart
def checkout(cart_contents):
    if not cart_contents:
        print("\nYour cart is empty. Please add items before checking out.")
        return False
    else:
        total_cost = sum(price * quantity for _, price, quantity in cart_contents)
        print("Total cost of your cart: £{:.2f}".format(total_cost))
        print("Thank you for shopping with Paws n Cart")
        return True

# Main function to start the program
def start():
    # Initialise an empty list to store the contents of the cart
    cart_contents = []
    # Define column names for tabulating the cart contents
    col_names = ["Item", "Price", "Quantity"]
    print("\nWelcome to Paws n Cart")
    # Start an infinite loop to show the menu options
    while True:
        # Display the main menu
        display_menu()
        # Ask the user to choose an option
        choice = input("\nPlease enter the number of the option that you would like to choose: ")
        # Perform actions bases on the users choice
        if choice == "1":
            add_item(cart_contents)
        elif choice == "2":
            remove_item(cart_contents)
        elif choice == "3":
            view_cart(cart_contents, col_names)
        elif choice == "4":
            if checkout(cart_contents):
                break
        elif choice == "5":
            print("\nThank you for shopping with Paws n Cart. Exiting...\n")
            break
        else:
            print("\nInvalid option choice")

# Entry point of the program
if __name__ == "__main__":
    start()
