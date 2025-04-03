# Write a function that takes two numbers and finds the average between the two.


def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    total_sum = a + b  # Sum of the two numbers
    return total_sum / 2  # Return the average

def main():
    # Find the averages for two pairs of numbers
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    # Find the average of avg_1 and avg_2
    final = average(avg_1, avg_2)
    
    # Print the results
    print("avg_1:", avg_1)
    print("avg_2:", avg_2)
    print("final:", final)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
