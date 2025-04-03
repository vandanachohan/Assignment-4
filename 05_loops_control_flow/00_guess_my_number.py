# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48


import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    # Initialize the number of attempts
    attempts = 0
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Loop until the user guesses correctly
    while guess != secret_number:
        attempts += 1  # Increase attempt count
        
        if guess < secret_number:  # If guess is lower than the secret number
            print("Your guess is too low.")
        else:  # If guess is higher than the secret number
            print("Your guess is too high.")
        
        print()  # Empty line for a cleaner display
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
    
    attempts += 1  # Include the correct guess attempt
    print(f"Congrats! The number was: {secret_number}. You guessed it in {attempts} attempts.")

if __name__ == '__main__':
    main()
