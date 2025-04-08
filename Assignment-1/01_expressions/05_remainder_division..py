# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2



#  Division and Remainder Calculator

def main():
    print("Division and Remainder Calculator\n")

    while True:
        try:
            # Get two integer inputs
            dividend = int(input("Please enter an integer to be divided: "))
            divisor = int(input("Please enter an integer to divide by: "))

            # Check for division by zero
            if divisor == 0:
                print("Division by zero is not allowed. Please enter a nonzero divisor.\n")
                continue

            # Perform integer division
            quotient = dividend // divisor
            remainder = dividend % divisor

            # Display result using f-strings
            print(f"\nThe result of this division is {quotient} with a remainder of {remainder}\n")
            break  # Exit loop after a successful calculation

        except ValueError:
            print("Invalid input! Please enter whole numbers only.\n")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
