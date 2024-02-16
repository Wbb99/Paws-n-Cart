# Paws n Cart

# Improvements to be made
    # 

# Create an empty list to store the contents of the cart
cart_contents = []

# Define column names for tabulating the cart contents
col_names = ["Item", "Price", "Quantity"]

# Import the 'tabulate' library for creating formatted tables
from tabulate import tabulate

# Print a welcome message
print("\nWelcome to Paws n Cart")

# Start an infinite loop that shows the menu options
while True:
    # Display the main menu options
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

    # Ask the user to choose an option
    choice = input("\nPlease enter the number of the option that you would like to choose: ")

    try:
        # If the user chooses to add an item to the cart
        if choice == "1":
            item = input("\nWhat item would you like to add to your cart: ")
            try:
                price = float(input("\nHow much does the item cost: £"))
                try:
                    quantity = int(input("\nEnter the quantity: "))
                except ValueError:
                    print("\nError: Please enter a numeric value for the quantity")
                    continue

                # Add the item and its price to the cart
                cart_contents.append((item, price, quantity))

                # Confirm that the item has been added to the cart
                print("\n{} has been added to your cart.".format(item, quantity))

            except ValueError:
                print("\nError: Please enter a numeric value for the price")
                continue

        # If the user chooses to remove an item from the cart
        elif choice == "2":
            remove = input("\nWhich item would you like to remove: ")

            # Iterate through the cart_contents list to find and remove the chosen item
            found = False
            for item, price, quantity in cart_contents:
                if item == remove:
                    cart_contents.remove((item, price, quantity))
                    found = True

                    # Confirm that the item has been removed from the cart
                    print("\n{} has been removed from your cart.".format(remove))
                    break

            # If the chosen item is not found in the cart, display an error message
            if not found:
                print("\nThat item is not in your cart.")

        # If the user chooses to view the contents of their cart
        elif choice == "3":
            print("\nThis is your cart:")
            print(tabulate(cart_contents, headers=col_names, tablefmt="heavy_grid"))

        # If the user chooses to checkout
        elif choice == "4":
            if not cart_contents:
                print("\nYour cart is empty. Please add items before checking out.")
            else:
                # Calculate the total cost of items in the cart
                total_cost = sum(price * quantity for item, price, quantity in cart_contents)

                # Display the total cost and a thank you message
                print("Total cost of your cart: £{:.2f}".format(total_cost))
                print("Thank you for shopping with Paws n Cart")

                # Exit the loop
                break

        # If the user chooses to exit the program
        elif choice == "5":
            print("\nThank you for shopping with Paws n Cart. Exiting...\n")
            break

        # Print an error message if the user chooses an invalid option
        else:
            print("\nInvalid option choice")

    # Handle potential ValueErrors
    except ValueError as ve:
        print(f"\nError: {ve}")

    # Handle general exceptions
    except Exception as e:
        print("\nAn unexpected error occurred:", e)
