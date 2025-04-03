# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!



# Ask the user for their favorite animal
favorite_animal = input("What's your favorite animal? ")

# Respond with the user's input
print(f"My favorite animal is also {favorite_animal}!")






# """✅ Advanced Version (Special Cases Fix)"""


# # User input Favorite Animal
# favorite_animal = input("What's your favorite animal? ").strip()

# # Special case handling for multiple words
# if favorite_animal:
#     formatted_animal = " ".join(word.capitalize() for word in favorite_animal.split())
#     print(f"My favorite animal is also {formatted_animal}!")
# else:
#     print("You didn't enter any animal!")
