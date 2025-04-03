# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily you wrote down what fruits were available and how much one of each fruit costs.

# Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.

# Here is an example run of the program (user input is in bold italics):

# How many (apple) do you want?: 2

# How many (durian) do you want?: 0

# How many (jackfruit) do you want?: 1

# How many (kiwi) do you want?: 0

# How many (rambutan) do you want?: 1

# How many (mango) do you want?: 3

# Your total is $99.5


def main():
    # Dictionary of fruits and their prices per unit
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize total cost variable
    
    print("Fruit shop - Let's shop!")
    
    # Iterate through the fruits
    for fruit_name, price in fruits.items():
        # Display the price of each fruit
        print(f"\nPrice of {fruit_name}: ${price:.2f} per unit.")
        
        while True:
            user_input = input(f"How many {fruit_name}s do you want to buy? (Type 'skip' to skip, 'exit' to stop): ").strip().lower()
            
            # Exit condition: stop the whole program if user types 'exit'
            if user_input == 'exit':
                print("Thank you for visiting the fruit shop!")
                print(f"Your total cost is: ${total_cost:.2f}")
                return  # Exit the program immediately
            
            # Skip condition: move to next fruit if user types 'skip'
            if user_input == 'skip':
                print(f"You skipped {fruit_name}.")
                break
            
            # Try to convert the user input to an integer
            try:
                amount_bought = int(user_input)
                if amount_bought < 0:
                    print("Please enter a non-negative number.")
                else:
                    break  # Exit the loop if valid input
            except ValueError:
                print("Invalid input. Please enter a valid integer for the quantity.")
        
        # Calculate the cost and add it to the total
        if amount_bought > 0:
            fruit_cost = price * amount_bought
            total_cost += fruit_cost
            print(f"You selected {amount_bought} {fruit_name}(s) for ${fruit_cost:.2f}")
    
    # Ask if the user wants to continue shopping
    while True:
        continue_shopping = input("\nWould you like to continue shopping for more fruits? (yes/no): ").strip().lower()
        if continue_shopping == 'yes':
            print("Let's continue shopping!")
            main()  # Restart the shopping process
            return
        elif continue_shopping == 'no':
            print("Thank you for shopping with us!")
            print(f"Your total cost is: ${total_cost:.2f}")
            return  # Exit the program
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    main()
