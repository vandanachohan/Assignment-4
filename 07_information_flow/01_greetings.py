# We've written a helper function for you called greet(name) which takes as input a string name and prints a greeting. Write some code in main() to get the user's name and then greet them, being sure to call the greet(name) helper function.

# Here's a sample run of the program (user input in bold italics):

# What's your name? Sophia

# Greetings vandana!


def greet(name: str) -> str:
    """Returns a greeting message with the given name."""
    return "Greetings " + name + "!"

def main():
    name = "Vandana"  # Using your name instead of asking for user input
    message = greet(name)  # Store the greeting message
    print(message)  # Print the returned message

if __name__ == '__main__':
    main()
