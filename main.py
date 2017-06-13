import sys
from required_funs import *
from os import path
import pandas as pd

def main():
    print("Welcome to the bacterial data analysis program!")
    print("Your options:")
    while(True):
        option = menu(main_options)
        if option == 1:
            data = input_datafile()
            print("Succesfully imported "+str(len(data.index))+" rows of data.")
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
        except (ValueError, EOFError):
            print("Please input a number corresponding to the option you want to select.")
            pass

def input_datafile():
    while(True):
        filename = input_filename()
        data = dataLoad(filename)
        if data is not None:
            return data
        else:
            print("File contents are invalid, please try again.")

def input_filename():
    while(True):
        try:
            filename = input("Please input the path to your data file: ")
            if path.isfile(filename):
                return(filename)
        except EOFError:
            pass
        print("File does not exist or you do not have permission to read it. Please try again.")

main()
