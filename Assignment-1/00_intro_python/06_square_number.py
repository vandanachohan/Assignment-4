# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0


def main():
    # Get input from the user and convert it to a float
    num = float(input("Type a number to see its square: "))

    # Print the result using f-string for cleaner formatting
    print(f"{num:.1f} squared is {num ** 2:.1f}")

# Required to call the main function
if __name__ == '__main__':
    main()
