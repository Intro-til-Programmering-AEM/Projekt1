import sys
from required_funs import *
from os import path

def main():
    print("Welcome to the bacterial data analysis program!")
    filters = []
    while(True):
        print_filters(filters)
        print("Your options:")
        option = menu(main_options)
        if option is None:
            pass
        elif option == 1:
            originalData = input_datafile()
            data = input_datafile()
            print("Succesfully imported "+str(len(data))+" rows of data.")
        elif option == 2:
            option = menu(filter_options)
            if option is None:
                pass
            elif option == 1: # Adding
                print("Which column would you like to filter on?")
                option = menu(column_options)
                print("Which kind of filter would you like to add?")
                if option is None:
                    pass
                elif option == 3:
                    choice = menu(categorical_options)
                    print("Which bacteria type?")
                    bacterium = menu(list(bacteria_types.values()))
                    if choice is None:
                        pass
                    elif choice == 1:
                        filters.append((lambda r: r.Bacteria != bacterium, "Exclude "+bacteria_types[bacterium]))
                    else:
                        filters.append((lambda r: r.Bacteria == bacterium, "Include only "+bacteria_types[bacterium]))
                else:
                    choice = menu(continuous_options)
                    bound = input_float("Please input your bound:")
                    def filter_fun(row):
                        col = row.Temperature if option == 1 else row.GrowthRate
                        return col > bound if choice == 1 else col < bound
                    filter_text = column_options[option]+" must be "+("greater than" if choice == 1 else "less than")+" "+str(bound)
                    filters.append((filter_fun,filter_text))
            elif option == 2: # Deleting
                print("Which filter would you like to remove?")
                filter_texts = list(map(lambda f: f[1], filters))
                filter_texts.append("All filters")
                choice = menu(filter_texts)
                if choice is None:
                    pass
                elif choice == len(filter_texts):
                    filters = []
                else:
                    del filters[choice-1]
            # Refilters data every time a filter is added or deleted, inefficient!
            data = originalData
            for f in filters:
                data = filter(f[0],data)
        elif option == 3:
            print("Please choose the kind of statistic you would like to calculate:")
            option = menu(statistic_options)
            if option is None:
                pass
            else:
                statistic = statistic_options[option]
                print(dataStatistics(data,statistic))
        elif option == 4:
            dataPlot(data)
        elif option == 5:
            print("Thank you for using the bacterial data analysis program.")
            sys.exit()
        # No else needed, it has already been checked that the option is legal

main_options = ["Load data","Filter data","Display statistics","Generate plots","Quit"]

statistic_options = ["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth Rate","Rows","Mean Cold Growth rate","Mean Hot Growth rate"]

filter_options = ["Add a filter","Remove a filter"]

column_options = ["Temperature","Growth rate","Bacteria type"]

continuous_options = ["Upper bound","Lower bound"]

categorical_options = ["Exclude a type","Exclude everything but one type"]

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)

def input_option(options):
    while(True):
        try:
            # Get number that may be a legal option
            x = input("Select an option: ")
            if x == "":
                raise EOFError
            x = int(x)
            # Check if it's legal
            if x <= len(options) and x > 0:
                return x
            else:
                print("Not an option, please try again.")
        except EOFError:
            return None
        except ValueError:
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

def print_filters(filters):
    if not filters:
        print("No active filters.")
    else:
        print("Active filter:")
        for f in filters:
            print("* "+f[1])

main()
