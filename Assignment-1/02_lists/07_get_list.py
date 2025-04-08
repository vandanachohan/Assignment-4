# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Here's a sample run (user input is in blue):

# Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']



def main():
    lst = []  # Make an empty list to store the values

    val = input("Enter a value: ")  # Get an initial value from the user
    while val:  # Continue asking for input until the user presses Enter without typing anything
        lst.append(val)  # Add the entered value to the list
        val = input("Enter a value: ")  # Prompt the user for the next value

    print("Here's the list:", lst)  # Print the list when the user stops entering values


# This line is required to call the main function
if __name__ == '__main__':
    main()
