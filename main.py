import sys
from required_funs import bacteria_types # I tvivl om hvad der skal imporeres til hvilke filer
from os import path
from filhåndtering import dataLoad, input_datafile, input_filename
from statistik import dataStatistics
from inputhandlers import input_option, input_float, input_wrapper
from filterfunktioner import print_filters, continous_filter_closure
from menuhåndtering import *
from plots import dataPlot, plotWrapper, plotNumbers, plotGrowthRates, boxPlotGrowthRates, boxPlotTemperatures
print("Welcome to the bacterial data analysis program!")
filters = []
data = None
while(True):
    print_filters(filters)
    print("Your options:")
    option = menu(main_options)
    if option is None: #the program can be exited by pressing enter
        pass
    elif option == 1:
        originalData = input_datafile()
        if originalData is not None: #If data has been uploaded the program tells the user how many rows of data that has been implementet
            data = originalData
            print("Succesfully imported "+str(len(data))+" rows of data.")
    elif option == 5:
        print("Thank you for using the bacterial data analysis program.")
        sys.exit()
    elif data is not None:
        if option == 2:
            option = menu(filter_options)
            if option is None: #By pressing enter the user is redirected to the main menu
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
                    bacterium = menu(list(bacteria_types.values())) #Henter listen af bakterietyper fra required funs
                    if choice is None:
                        pass
                    elif choice == 1:
                        filters.append((lambda r: r.Bacteria != bacterium, "Exclude "+bacteria_types[bacterium]))
                    else:
                        filters.append((lambda r: r.Bacteria == bacterium, "Include only "+bacteria_types[bacterium]))
                else:
                    choice = menu(continuous_options)
                    bound = input_float("Please input your bound: ")
                    filter_text = column_options[option-1]+" must be "+("less than" if choice == 1 else "greater than")+" "+str(bound)
                    filters.append((continous_filter_closure(choice, bound),filter_text))
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
                data = data[f[0](data)]
            print(str(len(data))+" rows left after filtering")
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
    else:
        print("Please load valid data before attempting to use this function")
    # No else needed, it has already been checked that the option is legal
