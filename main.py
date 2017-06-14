import sys
from required_funs import *
from os import path

def main():
    print("Welcome to the bacterial data analysis program!")
    print("Your options:")
    filters = []
    while(True):
        option = menu(main_options)
        if option == 1:
            data = input_datafile()
            print("Succesfully imported "+str(len(data))+" rows of data.")
        elif option == 2:
            option = menu(filter_options)
            if option == 1:
                print("Which column would you like to filter on?")
                option = menu(column_options)
                print("Which kind of filter would you like to add?")
                if option == 3:
                    choice = menu(categorical_options)
                    print("Which bacteria type?")
                    bacterium = menu(bacteria_types)
                    if choice == 1:
                        filters.append((lambda r: r.Bacteria != bacterium, "Exclude "+bacteria_types[bacterium]))
                    else:
                        filters.append((lambda r: r.Bacteria == bacterium, "Include only "+bacteria_types[bacterium]))
                else:
                    choice = menu(continuous_options)
                    bound = input_float("Please input your bound:")
                    def filter_fun(row):
                        col = row.Temperature if option == 1 else row.GrowthRate
                        return col > bound if choice == 1 else col < bound
                    filters.append((filter_fun,column_options[option]+" must be "+("greater than" if choice == 1 else "less than")+" "+str(bound)))
            elif option == 2:
                print("TODO: not implemented yet")
        elif option == 3:
            print("Please choose the kind of statistic you would like to calculate:")
            statistic = statistic_options[menu(statistic_options)]
            print(dataStatistics(data,statistic))
        elif option == 4:
            dataPlot(data)
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

statistic_options = {
    1: "Mean Temperature",
    2: "Mean Growth rate",
    3: "Std Temperature",
    4: "Std Growth Rate",
    5: "Rows",
    6: "Mean Cold Growth rate",
    7: "Mean Hot Growth rate",
}

filter_options = {
    1: "Add a filter",
    2: "Remove a filter"
}

column_options = {
    1: "Temperature",
    2: "Growth rate",
    3: "Bacteria type"
}

continuous_options = {
    1: "Upper bound",
    2: "Lower bound"
}

categorical_options = {
    1: "Exclude a type",
    2: "Exclude everything but one type"
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

def input_float(request):
    while(True):
        try:
            x = float(input(request))
            return x
        except (ValueError, EOFError):
            print("Please input a real number.")
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
