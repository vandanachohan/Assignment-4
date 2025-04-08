# Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch.
#  We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- at each number,
#  before printing the number, you should call done() and check if it returns True or not.  
#  If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(),
#  which will print "I'm done.".
#  We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.

# Here's a sample run of this program:

# I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.


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
