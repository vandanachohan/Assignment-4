# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. 
# The list is guaranteed to be non-empty. 
# We've written some code for you which prompts the user to input the list one element at a time.


def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])  # Print the first element of the list

# There is no need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":  # Loop until the user presses Enter without entering any text
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  # Get the list from the user
    get_first_element(lst)  # Print the first element of the list

if __name__ == '__main__':
    main()  # Call the main function when the script runs
