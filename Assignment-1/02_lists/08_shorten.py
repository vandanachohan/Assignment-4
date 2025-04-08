# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long.
# If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. '
# 'For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

MAX_LENGTH = 3  # Set the maximum length of the list

def shorten(lst):
    while len(lst) > MAX_LENGTH:  # Continue removing elements until the list is MAX_LENGTH long
        last_elem = lst.pop()  # Remove the last element of the list
        print(last_elem)  # Print the element that was removed

# This function prompts the user to enter elements for the list
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list of items from the user
    shorten(lst)  # Shorten the list to MAX_LENGTH and print removed items

if __name__ == '__main__':
    main()  # Call the main function when the script runs
