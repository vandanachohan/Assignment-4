# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

# Here's a sample run (user input is in bold italics):

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!



# Mad Libs Sentence Generator

import random

# List of sentence templates for variety
SENTENCE_TEMPLATES = [
    "Panaversity is fun! I learned to program and used Python to make my ",
    "With Python, I created a ",
    "At Panaversity, we coded a ",
    "Learning Python was exciting! I built a "
]

def get_valid_input(prompt: str) -> str:
    """Gets non-empty user input and trims extra spaces."""
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        print("Oops! Please enter a valid word.")

def main():
    print("🎉 Welcome to the Panaversity Mad Libs Game! 🎉\n")

    # Get words from the user
    adjective = get_valid_input("Please type an adjective and press enter: ")
    noun = get_valid_input("Please type a noun and press enter: ")
    verb = get_valid_input("Please type a verb and press enter: ")

    # Choose a random sentence template
    sentence_start = random.choice(SENTENCE_TEMPLATES)

    # Display the final fun sentence
    print("\n" + sentence_start + f"{adjective} {noun} {verb}!")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
