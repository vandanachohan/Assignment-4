# 10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd


def main():
    for i in range(10, 20):  # Loop from 10 to 19
        if is_odd(i):
            print(f"{i} odd")
        else:
            print(f"{i} even")
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns True.
    """
    return value % 2 == 1  # Returns True if the value is odd

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
