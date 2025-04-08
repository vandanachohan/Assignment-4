
# Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

# Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, 
# the voting ages are very different:

# the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

# the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

# the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

# Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

# Here's a sample run of the program (user input is in blue):

# How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. 
# You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

PAKISTAN_AGE = 18
AUSTRIA_AGE = 16
UK_AGE = 18
COUNTRYX_AGE = 30  # New country with voting age of 30

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    eligible = False  # Flag to track if the user is eligible to vote in any country

    # Check if the user can vote in Pakistan
    if user_age >= PAKISTAN_AGE:
        print("You can vote in Pakistan where the voting age is " + str(PAKISTAN_AGE) + ".")
        eligible = True
    
    # Check if the user can vote in Austria
    elif user_age >= AUSTRIA_AGE:
        print("You can vote in Austria where the voting age is " + str(AUSTRIA_AGE) + ".")
        eligible = True
    
    # Check if the user can vote in the UK
    elif user_age >= UK_AGE:
        print("You can vote in the UK where the voting age is " + str(UK_AGE) + ".")
        eligible = True
    
    # Check if the user can vote in CountryX
    elif user_age >= COUNTRYX_AGE:
        print("You can vote in CountryX where the voting age is " + str(COUNTRYX_AGE) + ".")
        eligible = True

    # If the user is not eligible for voting in any country
    if not eligible:
        print("You are not eligible to vote in any of the listed countries.")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
