# Problem Statement
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.



# Import the random library to simulate dice rolls
import random

# Number of sides on each die
NUM_SIDES = 6
# Number of times to roll the dice
NUM_ROLLS = 3

def roll_dice():
    """
    Simulates rolling two dice and returns their values.
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    return die1, die2, die1 + die2  # Returning all values for better clarity

def main():
    die1 = 10  # Variable scope demonstration
    print(f"die1 in main() starts as: {die1}\n")

    # Rolling the dice three times
    for i in range(1, NUM_ROLLS + 1):
        d1, d2, total = roll_dice()
        print(f"Roll {i}: Die 1 = {d1}, Die 2 = {d2}, Total = {total}")

    print(f"\ndie1 in main() is still: {die1}")  # Shows scope isolation

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
