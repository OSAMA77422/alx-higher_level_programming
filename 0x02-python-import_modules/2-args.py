#!/usr/bin/python3
# Check if the script is being run as the main program
if __name__ == "__main__":
    import sys
    # Get the number of arguments
    num_args = len(sys.argv) - 1  # subtract 1 to exclude the script name

    # Print the number of arguments and whether it's singular or plural
    print("{} argument{}".format(num_args, "s" if num_args != 1 else ""), end="")

    # Check if there are any arguments
    if num_args > 0:
        print(":")  # Print a colon before listing the arguments

        # Iterate through the arguments and print their position and value
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print(".")
