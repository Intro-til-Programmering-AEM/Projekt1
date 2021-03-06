#Menuhaandtering

from inputhandlers import input_option

# Lists of options used as input in the menu-function in the main file
main_options = ["Load data","Filter data","Display statistics","Generate plots","Quit"]

statistic_options = ["Mean Temperature","Mean Growth rate","Std Temperature","Std Growth Rate","Rows","Mean Cold Growth rate","Mean Hot Growth rate"]

filter_options = ["Add a filter","Remove a filter"]

continuous_options = ["Upper bound","Lower bound"]

categorical_options = ["Exclude a type","Exclude everything but one type"]

def menu(options):
    # Print options with option numbers
    for i in range(len(options)):
        print(str(i+1)+". "+options[i]+".")
    return input_option(options)