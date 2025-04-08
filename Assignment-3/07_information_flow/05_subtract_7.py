# Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the 
# subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.

def main():
    num = 7
    num = subtract_seven(num)  # Calling the helper function to subtract 7
    print("This should be zero: ", num)

def subtract_seven(num):
    return num - 7  # Subtracting 7 from the given number

if __name__ == '__main__':
    main()
