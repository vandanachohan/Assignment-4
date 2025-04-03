# In this program we show an example of using dictionaries to keep track of information in a phonebook.


def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create empty phonebook

    print("Enter names and numbers for the phonebook. Press Enter without typing a name to stop.")
    
    while True:
        name = input("Name: ")
        if name == "":  # Stop input if the user presses Enter without a name
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    print("\nPhonebook Entries:")
    for name, number in phonebook.items():
        print(f"{name} -> {number}")
    print()  # Adding an empty line for better readability


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by entering a name to get the associated number.
    """
    while True:
        name = input("Enter name to lookup (or press Enter to quit): ")
        if name == "":  # Stop looking up when the user presses Enter without a name
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")
        else:
            print(f"Phone number for {name}: {phonebook[name]}")
    print()  # Adding an empty line for better readability


def main():
    print("Welcome to the phonebook program!")
    
    # Reading phone numbers from user input
    phonebook = read_phone_numbers()

    # Print the phonebook
    print_phonebook(phonebook)

    # Allow the user to look up phone numbers
    lookup_numbers(phonebook)

    print("Goodbye!")


# Python boilerplate.
if __name__ == '__main__':
    main()
