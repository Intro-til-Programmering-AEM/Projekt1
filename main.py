import sys
from required_funs import *

def main():
    print("Welcome to the bacterial data analysis program!")
    print("Your options:")
    while(True):
        option = menu(main_options)
        if option == 1:
            print("TODO: not implemented yet")
        elif option == 2:
            print("TODO: not implemented yet")
        elif option == 3:
            print("TODO: not implemented yet")
        elif option == 4:
            print("TODO: not implemented yet")
        elif option == 5:
            print("Thank you for using the bacterial data analysis program.")
            sys.exit()
        # No else needed, it has already been checked that the option is legal

main_options = {
    1: "Load data",
    2: "Filter data",
    3: "Display statistics",
    4: "Generate plots",
    5: "Quit",
}

def menu(options):
    # Print options with option numbers
    for n, t in options.items():
        print(str(n)+". "+t+".")
    return input_option(options)

def input_option(options):
    while(True):
        try:
            # Get number that may be a legal option
            x = int(input("Select an option: "))
            # Check if it's legal
            if x in options.keys():
                return x
            else:
                print("Not an option, please try again.")
        except ValueError:
            print("Please input a number corresponding to the option you want to select.")
            pass

main()
