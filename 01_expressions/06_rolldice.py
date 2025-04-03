# Simulate rolling two dice, and prints results of each roll as well as the total.


# Python Program: Dice Rolling Simulator

import random  # Import the random module

# Number of sides on each die
NUM_SIDES: int = 6  

def roll_dice() -> tuple:
    """Simulates rolling two dice and returns their values along with the total."""
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1, die2, die1 + die2

def main():
    print("🎲 Dice Rolling Simulator 🎲\n")

    while True:
        try:
            rolls = int(input("Enter the number of times to roll the dice: "))

            if rolls <= 0:
                print("Please enter a positive number!\n")
                continue

            for i in range(1, rolls + 1):
                die1, die2, total = roll_dice()
                print(f"Roll {i}: 🎲 {die1} + 🎲 {die2} = {total}")

            break  # Exit loop after successful rolls

        except ValueError:
            print("Invalid input! Please enter a valid number.\n")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
