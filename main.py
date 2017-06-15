import sys
from os import path
from filhaandtering import dataLoad, input_datafile, input_filename
from statistik import dataStatistics
from inputhandlers import input_option, input_float, input_wrapper
from filterfunktioner import print_filters, continous_filter_closure
from menuhaandtering import *
from plots import dataPlot, plotWrapper, plotNumbers, plotGrowthRates, boxPlotGrowthRates, boxPlotTemperatures
from data_descriptions import column_options, bacteria_types

print("Welcome to the bacterial data analysis program!")
filters = []
data = None
while(True):
    print_filters(filters)
    print("Your options:")
    option = menu(main_options)
    # Empty input restarts menu
    if option is None:
        pass
    # Importing
    elif option == 1:
        originalData = input_datafile()
        # originalData may be none if user cancelled
        if originalData is not None:
            # data will be filtered on, keep originalData around for resetting the filters
            data = originalData
            if len(data) == 0:
                print("No valid lines in file. Nothing imported.")
            else:
                print("Succesfully imported "+str(len(data))+" rows of data.")
    # Quitting
    elif option == 5:
        print("Thank you for using the bacterial data analysis program.")
        # Exit properly
        sys.exit()
    # If data is defined
    elif data is not None:
        # Filtering
        if option == 2:
            option = menu(filter_options)
            #By pressing enter the user is redirected to the main menu (but the data is refiltered)
            if option is None:
                pass
            # Adding a filter
            elif option == 1:
                print("Which column would you like to filter on?")
                option = menu(column_options)
                print("Which kind of filter would you like to add?")
                if option is None:
                    pass
                # elif ensures that pass returns all the way to main menu
                elif option == 3:
                    choice = menu(categorical_options)
                    print("Which bacteria type?")
                    bacterium = menu(list(bacteria_types.values()))
                    if choice is None:
                        pass
                    elif choice == 1:
                        # filters is a list of (filtering function, descriptive text) tuples
                        filters.append((lambda r: r.Bacteria != bacterium, "Exclude "+bacteria_types[bacterium]))
                    else:
                        filters.append((lambda r: r.Bacteria == bacterium, "Include only "+bacteria_types[bacterium]))
                # only two other options are 1 and 2
                else:
                    choice = menu(continuous_options)
                    bound = input_float("Please input your bound: ")
                    # Create description for continuous filter
                    filter_text = column_options[option-1]+" must be "+("less than" if choice == 1 else "greater than")+" "+str(bound)
                    # Create closure for filtering based on current choices
                    filter_fun = continous_filter_closure(choice, option, bound)
                    # Append to the list of filters
                    filters.append((filter_fun,filter_text))
            # Deleting a filter
            elif option == 2:
                print("Which filter would you like to remove?")
                filter_texts = [f[1] for f in filters]
                filter_texts.append("All filters")
                choice = menu(filter_texts)
                if choice is None:
                    pass
                # If choice is the last one, "All filters"
                elif choice == len(filter_texts):
                    filters = []
                else:
                    del filters[choice-1]
            data = originalData
            # filter every row with every filter, only accept it if all filters let it through
            # scales as number of filters * number of rows
            mask = [all([f[0](x) for f in filters]) for i, x in data.iterrows()]
            # and the filtering is done in "only" one additional pass over the data
            data = data[mask]
            if len(data) == 0:
                print("No rows left after filtering. Consider deleting one or more filters.")
            else:
                print(str(len(data))+" rows left after filtering")
        # Calculating statistics
        elif option == 3:
            print("Please choose the kind of statistic you would like to calculate:")
            option = menu(statistic_options)
            # Enter returns to main menu
            if option is None:
                pass
            else:
                # Translate choice the name of the statistic
                statistic = statistic_options[option]
                print(dataStatistics(data,statistic))
        # Plotting
        elif option == 4:
            dataPlot(data)
    else:
        print("Please load valid data before attempting to use this function")
