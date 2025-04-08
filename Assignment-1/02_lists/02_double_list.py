# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]



def main():
    numbers = [1, 2, 3, 4]  # Creates a list of numbers
    numbers = [num * 2 for num in numbers]  # Double each element using list comprehension
    print(numbers)  # Print the updated list

if __name__ == "__main__":
    main()
