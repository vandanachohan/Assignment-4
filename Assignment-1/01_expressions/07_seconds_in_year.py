# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):

# There are 5 seconds in a year!

# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# Useful constants to make calculations easy
DAYS_PER_YEAR: int = 365
DAYS_PER_LEAP_YEAR: int = 366  # Leap years have 366 days
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def calculate_seconds(days: int) -> int:
    """Calculates the number of seconds in a given number of days."""
    return days * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

def main():
    print("📅 Seconds in a Year Calculator 📅\n")

    # Calculate seconds for a normal year and a leap year
    seconds_normal_year = calculate_seconds(DAYS_PER_YEAR)
    seconds_leap_year = calculate_seconds(DAYS_PER_LEAP_YEAR)

    # Display results
    print(f"There are {seconds_normal_year:,} seconds in a normal year!")
    print(f"There are {seconds_leap_year:,} seconds in a leap year! 🌟")

# Calls the main function when the script is executed
if __name__ == '__main__':
    main()
