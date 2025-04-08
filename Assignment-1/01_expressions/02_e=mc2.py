# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

# E = m * c**2

# Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

# Here's a sample run of the program (user input is in bold italics):

# Enter kilos of mass: 100

# e = m * C^2...

# m = 100.0 kg

# C = 299792458 m/s

# 8.987551787368176e+18 joules of energy!


# Define the speed of light in meters per second
C: int = 299792458  

def calculate_energy(mass: float) -> float:
    """Calculate energy using Einstein's equation: E = m * c^2"""
    return mass * (C ** 2)

def main():
    while True:
        try:
            # Ask for user input
            mass_in_kg = float(input("\nEnter kilos of mass (negative to exit): "))

            # Exit condition
            if mass_in_kg < 0:
                print("Exiting program. Goodbye!")
                break

            # Calculate energy
            energy_in_joules = calculate_energy(mass_in_kg)

            # Display results
            print("\ne = m * C^2...\n")
            print(f"m = {mass_in_kg} kg")
            print(f"C = {C} m/s")
            print(f"{energy_in_joules:.2e} joules of energy!\n")  # Scientific notation

        except ValueError:
            print("Invalid input! Please enter a numeric value.")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
