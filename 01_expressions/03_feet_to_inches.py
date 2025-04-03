# Conversion factor: 12 inches in 1 foot
INCHES_IN_FOOT: int = 12  

def convert_feet_to_inches(feet: float) -> float:
    """Converts feet to inches."""
    return feet * INCHES_IN_FOOT

def main():
    print("Feet to Inches Converter\n")

    while True:
        try:
            # Ask for user input
            feet = float(input("Enter number of feet (negative to exit): "))

            # Exit condition
            if feet < 0:
                print("Exiting program. Goodbye!")
                break

            # Perform the conversion
            inches = convert_feet_to_inches(feet)

            # Proper singular/plural formatting
            unit = "foot" if feet == 1 else "feet"
            print(f"{feet} {unit} is equal to {inches} inches!\n")

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
